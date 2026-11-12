// FastAPI 서버 주소 (AppStart.py 실행 후 사용)
// 페이지를 연 주소(localhost / 127.0.0.1)와 같은 호스트로 요청 , 파일로 직접 열면(file://) 127.0.0.1
const API_URL = `http://${location.hostname || '127.0.0.1'}:8000/api`;
const PYEONG_TO_SQM = 3.3058; // 1평 = 3.3058㎡

let range = null; // 선택한 동의 실제 거래 범위 (서버에서 받아옴)

const $ = (selector) => document.querySelector(selector);
const round1 = (value) => Math.round(value * 10) / 10; // 소수 첫째 자리 반올림

// 1) 페이지 열리면 법정동 목록 불러와 드롭다운 채우기 , GET /api/dongs
async function loadDongs() {
    const select = $('#dong');
    try {
        const response = await axios.get(`${API_URL}/dongs`);
        select.innerHTML = '<option value="">동을 선택하세요</option>';
        response.data.forEach((dong) => {
            select.innerHTML += `<option value="${dong}">${dong}</option>`;
        });
    } catch (error) {
        select.innerHTML = '<option value="">서버 연결 실패</option>';
        showError('서버에 연결할 수 없어요. AppStart.py 가 실행 중인지 확인하세요.');
    }
}

// 2) 동 선택 --> 그 동의 거래 범위 받아와 입력 제한 , GET /api/ranges?dong=여의도동
async function selectDong() {
    const dong = $('#dong').value;
    hideError();
    $('#result').hidden = true;
    if (!dong) {
        setInputsEnabled(false);
        $('#dongInfo').textContent = '동을 먼저 선택하세요';
        return;
    }
    try {
        const response = await axios.get(`${API_URL}/ranges`, { params: { dong } });
        range = response.data;
        applyRange(dong);
        setInputsEnabled(true);
    } catch (error) {
        showError('동 정보를 불러오지 못했어요.');
    }
}

// 3) 범위를 입력칸(min / max)과 안내 문구에 반영
function applyRange(dong) {
    const pyeongMin = round1(range.area_min / PYEONG_TO_SQM);
    const pyeongMax = round1(range.area_max / PYEONG_TO_SQM);

    // 3-1) 평수
    const pyeong = $('#pyeong');
    pyeong.min = pyeongMin;
    pyeong.max = pyeongMax;
    pyeong.placeholder = `${pyeongMin} ~ ${pyeongMax}`;
    pyeong.value = pyeongMin === pyeongMax ? pyeongMin : ''; // 범위가 한 값뿐이면 자동 입력
    $('#areaRange').textContent =
        `선택 가능 : ${pyeongMin}평 ~ ${pyeongMax}평 (전용 ${range.area_min}㎡ ~ ${range.area_max}㎡)`;
    updateSqm();

    // 3-2) 층
    const floor = $('#floor');
    floor.min = range.floor_min;
    floor.max = range.floor_max;
    floor.placeholder = `${range.floor_min} ~ ${range.floor_max}`;
    floor.value = range.floor_min === range.floor_max ? range.floor_min : '';
    $('#floorRange').textContent = `선택 가능 : ${range.floor_min}층 ~ ${range.floor_max}층`;

    // 3-3) 건축년도 : 동별 중앙값을 기본값으로
    const buildYear = $('#buildYear');
    buildYear.min = range.build_min;
    buildYear.max = range.build_max;
    buildYear.value = Math.round(range.build_median);
    $('#buildRange').textContent = `${range.build_min}년 ~ ${range.build_max}년`;

    // 3-4) 평형 버튼 : 범위 밖이면 비활성화
    document.querySelectorAll('.chip').forEach((chip) => {
        const sqm = Number(chip.dataset.sqm);
        chip.disabled = sqm < range.area_min || sqm > range.area_max;
    });

    $('#dongInfo').textContent = `${dong} 실거래 ${range.count.toLocaleString()}건 기준 범위로 입력할 수 있어요`;
}

// 4) 입력칸 활성 / 비활성
function setInputsEnabled(enabled) {
    ['#pyeong', '#floor', '#buildYear', '#submitBtn'].forEach((selector) => {
        $(selector).disabled = !enabled;
    });
    if (!enabled) {
        ['#areaRange', '#floorRange', '#buildRange'].forEach((selector) => { $(selector).textContent = ''; });
        document.querySelectorAll('.chip').forEach((chip) => { chip.disabled = true; });
    }
}

// 5) 평 입력할 때마다 ㎡ 환산값 표시
function updateSqm() {
    const pyeong = Number($('#pyeong').value);
    $('#sqmText').textContent = `= ${(pyeong * PYEONG_TO_SQM).toFixed(1)}㎡`;
}

// 6) 평형 버튼 클릭 --> 전용면적(㎡)을 평으로 바꿔 입력칸에 채우기
function selectChip(event) {
    const sqm = Number(event.currentTarget.dataset.sqm);
    $('#pyeong').value = round1(sqm / PYEONG_TO_SQM);
    updateSqm();
}

// 7) 예측 요청 , POST /api/predict
// 범위 밖 값은 form 의 min / max 검사에서 먼저 막힘 (브라우저가 안내 표시)
async function predict(event) {
    event.preventDefault(); // form 기본 제출(새로고침) 막기
    hideError();

    // 평 --> ㎡ 변환 , 반올림 오차로 범위를 살짝 벗어나지 않도록 범위 안으로 맞춤
    let area = Number($('#pyeong').value) * PYEONG_TO_SQM;
    area = Math.min(Math.max(area, range.area_min), range.area_max);

    // 서버(모델) 입력 규격과 같은 키 이름
    const item = {
        dong: $('#dong').value,
        area: Number(area.toFixed(2)),
        floor: Number($('#floor').value),
        build_year: Number($('#buildYear').value),
        contract_year: Number($('#contractYear').value)
    };

    const button = $('#submitBtn');
    button.disabled = true;
    button.textContent = '예측 중...';
    try {
        const response = await axios.post(`${API_URL}/predict`, item);
        if (response.data.error) {          // 서버 범위 검사에서 걸린 경우
            showError(response.data.error);
        } else {
            renderResult(item, response.data);
        }
    } catch (error) {
        showError('예측에 실패했어요. 입력값과 서버 상태를 확인하세요.');
    } finally {
        button.disabled = false;
        button.textContent = '예상 가격 보기';
    }
}

// 8) 결과 화면에 렌더링
function renderResult(item, data) {
    const pyeong = round1(item.area / PYEONG_TO_SQM);
    $('#priceText').textContent = data.price > 0 ? data.price_text : '예측 범위를 벗어난 입력이에요';
    $('#summaryText').textContent =
        `${item.dong} · 전용 ${pyeong}평(${item.area}㎡) · ${item.floor}층 · ${item.build_year}년 준공`;
    $('#r2Text').textContent = data.r2;
    $('#result').hidden = false;
}

function showError(message) {
    $('#errorText').textContent = message;
    $('#errorText').hidden = false;
}

function hideError() {
    $('#errorText').hidden = true;
}

// 9) 이벤트 연결
$('#predictForm').addEventListener('submit', predict);
$('#dong').addEventListener('change', selectDong);
$('#pyeong').addEventListener('input', updateSqm);
document.querySelectorAll('.chip').forEach((chip) => chip.addEventListener('click', selectChip));
loadDongs();

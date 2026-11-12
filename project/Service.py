# 비지니스 로직 = AI 모델 예측 (영등포구 아파트 실거래가)
import pandas as pd
import joblib
class AptService :
    # 생성자 : 서버 시작 시 1번만 실행 --> 모델 / 성능지표 불러오기 (재학습 X)
    def __init__(self):
        self.model = joblib.load('./project/apt_model.pkl')     # 최적 파이프라인 모델
        self.metrics = joblib.load('./project/apt_metrics.pkl') # { 'r2' : 결정계수 , 'dong_list' : 법정동 목록 }
    # 1) 법정동 목록 반환 (프론트 드롭다운용)
    def dongs(self):
        return self.metrics['dong_list']
    # 2) 법정동별 실제 거래 범위 반환 (프론트 입력 제한용)
    def ranges(self, dong):
        return self.metrics['dong_ranges'].get(dong) # 없는 동이면 None --> null 반환
    # 3) 예측
    def predict(self, item):
        # 0. 범위 검사 : 해당 동의 실제 거래 범위를 벗어나면 예측하지 않음
        r = self.ranges(item.get('dong'))
        if r is None :
            return {'error' : '학습 데이터에 없는 법정동입니다.'}
        if not (r['area_min'] <= float(item['area']) <= r['area_max']) :
            return {'error' : f"전용면적은 {r['area_min']}㎡ ~ {r['area_max']}㎡ 범위만 가능합니다."}
        if not (r['floor_min'] <= int(item['floor']) <= r['floor_max']) :
            return {'error' : f"층은 {r['floor_min']}층 ~ {r['floor_max']}층 범위만 가능합니다."}
        if not (r['build_min'] <= int(item['build_year']) <= r['build_max']) :
            return {'error' : f"건축년도는 {r['build_min']}년 ~ {r['build_max']}년 범위만 가능합니다."}
        # 1. 입력받은 딕셔너리 --> 모델 입력 규격(DataFrame) 변환 , 학습 때와 같은 컬럼명 / 순서
        sample = pd.DataFrame([item])
        sample = sample[['dong', 'area', 'floor', 'build_year', 'contract_year']]
        # 2. 프론트 입력값이 문자열("84")로 와도 숫자로 변환
        sample = sample.astype({'area' : float, 'floor' : int, 'build_year' : int, 'contract_year' : int})
        # 3. 예측 , 파이프라인이 원핫 / 다항 / 스케일링 자동 수행
        price = float(self.model.predict(sample)[0]) # numpy 실수 --> 파이썬 실수 (JSON 반환 위해)
        price = round(price)                         # 단위 : 만원
        # 4. 예측값 + 성능지표 반환
        return {
            'price' : price,                                         # 229654
            'price_text' : f'{price // 10000}억 {price % 10000:,}만 원', # 22억 9,654만 원
            'r2' : round(self.metrics['r2'], 4)                      # 0.887
        }

######################################################
# 서비스 객체 생성
apt_service = AptService()

# Practice8: API 데이터 수집
# 1. 개요 및 대상 API 정보
# API 이름: 행정안전부_착한가격업소 현황
# API URL: https://www.data.go.kr/data/3045247/fileData.do 

import httpx
import pandas as pd
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 1) 일반 인증키 
service_key = "4d3b7acdab259108dc759f80a738b36fb91261c4b62276956bb055b4b7b82fbf"

# 목표: httpx를 통해 공공데이터 API를 호출하고, pandas를 활용해 업소명, 주소, 가격 데이터를 
# 구조화한 뒤 통계 분석을 수행합니다.

# 본 행은 2026년 09월 30일 기준 현황임을 명시. 
# https://api.odcloud.kr/api/3045247/v1/uddi:0d236000-b33f-41ad-9227-ee0efa3ec6c8?page=1&perPage=10&serviceKey=4d3b7acdab259108dc759f80a738b36fb91261c4b62276956bb055b4b7b82fbf

# 2. 상세 요구사항
# 2-1 (API 호출 및 파라미터 설정):
# 지정된 API URL에 인증키(serviceKey)를 포함하여 요청합니다.
# 임의의 100건의 데이터를 수집
# 응답 결과를 Json 형식으로 파싱. 

def test1():
    url = "https://api.odcloud.kr/api/3045247/v1/uddi:0d236000-b33f-41ad-9227-ee0efa3ec6c8"
    url += "?page=1"
    url += "&perPage=100" # 100건의 데이터 수집. 
    url += f"&serviceKey={service_key}"

    response = httpx.get(url)
    print(response)
    response_json = response.json()

    # 2-2 (데이터프레임 적재):
    # 응답받은 JSON 데이터 중 실제 행 목록인 data 배열을 추출하여 pandas.DataFrame으로 변환합니다.

    df = pd.DataFrame(response_json['data'])
    df.info()

    # 2-3 (데이터 전처리 및 분석):
    # 가격1 컬럼의 데이터를 숫자형(pd.to_numeric)으로 변환합니다.
    # 수집된 100건 데이터 기준 가격1의 평균값을 산출하여 출력합니다.

    df['가격1'] = pd.to_numeric(df['가격1'])
    print(df['가격1'].dtype) 
    a = df['가격1']
    print(np.mean(a))

    # 2-4 (업종별 평균 가격 집계 및 시각화):
    # groupby('업종')을 사용하여 업종별 가격1의 평균 가격을 계산합니다.
    new_df = df.groupby('업종')['가격1'].mean().reset_index()
    # seaborn의 barplot 활용하여 업종별 평균 가격 비교 막대그래프를 시각화합니다.
    sns.barplot(data=new_df , x='업종' , y='가격1')
    plt.title("업종별 가격 비교")
    plt.show()

test1()
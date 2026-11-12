# [1] 라우터 : 특정 도메인(주소) 묶어주는 역할
from fastapi import APIRouter
# router = APIRouter (prefix = "공통URL")
router = APIRouter(prefix="/api")

# [2] 서비스 불러오기 # from 파일명 import 변수명
from Service import apt_service

# 1) 법정동 목록 조회 , http://127.0.0.1:8000/api/dongs
@router.get("/dongs")
async def dongs():
    return apt_service.dongs()

# 2) 법정동별 거래 범위 조회 , http://127.0.0.1:8000/api/ranges?dong=여의도동
@router.get("/ranges")
async def ranges( dong:str ):
    return apt_service.ranges( dong )

# 3) 예측 , http://127.0.0.1:8000/api/predict
# body 예시 : {"dong" : "여의도동" , "area" : 84 , "floor" : 10 , "build_year" : 2000 , "contract_year" : 2026}
@router.post("/predict")
async def predict( item:dict ):
    return apt_service.predict( item )

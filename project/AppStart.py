# 파이썬 파일 분리
# AppStart.py : FastAPI 실행 파일
# Controller.py : HTTP REST 파일
# Service.py : 로직 파일 (AI 모델 예측)

# 1) 서버 실행
import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("AppStart:app" , host="127.0.0.1" , port=8000 , reload=True)

# [2] CORS 설정 : 프론트(HTML)에서 axios 로 다른 주소의 서버 호출 허용
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 모든 주소 허용 (실습용)
    allow_methods=["*"],   # GET / POST 등 모든 메소드 허용
    allow_headers=["*"]
)

# [3] 컨트롤러에 라우터 연결
import Controller # import 파일명
# app.include_router(라우터) # 파일명.변수명
app.include_router(Controller.router)
# http://127.0.0.1:8000/docs

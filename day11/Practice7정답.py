# Practice7 문제 [ 씨네21(Cine21) 영화 평점 및 핵심 정보 수집 ]
# 출처 및 대상: 씨네21 영화 평점 페이지,  https://cine21.com/movie/point
# 제목 ,  이미지링크 , 전문가 평점 = "list_with_upthumb_item"
# p.title , .img_wrap>img , .star_wrap > p.num
# 4.  클릭이벤트 : dom.click() , pagination .page a

# [1. 목표]
# Playwright의 비동기 제어와 동적 페이지네이션(click)을 활용해 여러 페이지를 순회한다.
# 영화 아이템 카드에서 제목, 이미지 링크, 전문가 평점 3가지 핵심 데이터를 정확히 추출하여 구조화한다.

url = "https://cine21.com/movie/point"

# 1]
import asyncio
from playwright.async_api import async_playwright 

async def run( ) :
    item_list = [ ]
    # 2-1) async_playwright() 실행 하고 종료 되기 전까지 동기화 처리 지원 
    async with async_playwright() as p : 
        # 2-2) 크로미움( 구글 회사 제공 하는 백그라운드용 오픈소스 브라우저 )
        # await p.chromim.launch( headless = True백그라운드모드 /False뷰모드 ) 
        browser = await p.chromium.launch( headless = False )
        # 2-3) 현재 실행된 크로미움의 새로운 페이지(빈 페이지) 열기 , .new_page() 
        페이지 = await browser.new_page() 
        # 2-4) 빈 페이지에 특정한 URL 주소 대입/이동 , .goto( url )
        await 페이지.goto( url )
        await 페이지.wait_for_timeout( 3000 )
        # ======================================================= #

        # 7] 반복문 이용하여 버튼 하나씩 클릭 .click()
        for i in range(1, 4) :  # 1부터 3까지 등록
            # 8] query_select_all(식별자) : 여러개 dom 반환 , query_select(식별자) : 한개 dom 반환
            페이지버튼리스트 = await 페이지.query_selector_all('.pagination .page a')
            await 페이지버튼리스트[ i -1].click() # 0 인덱스부터 a 마크업 클릭이벤트
            await 페이지.wait_for_timeout(2000)
# [2. 데이터 수집 요구사항]
# 2-1 (페이지 순회): 1페이지부터 3페이지까지 반복문을 통해 동적으로 페이지를 이동한다.
# 2-2 (요소 추출): 각 영화 카드 내부에서 아래 3가지 요소를 각각 수집한다.
# 영화 제목 # 이미지 # 전문가 평점
            # 9] 
            items = await 페이지.query_selector_all('.list_with_upthumb_item')
            for item in items:
                영화제목 = await item.query_selector(' .title')
                영화제목 = await 영화제목.inner_text() if 영화제목 else "제목없음"
                이미지링크 = await item.query_selector(' .img_wrap>img')
                이미지링크 = await 이미지링크.get_attribute('src') if 이미지링크 else "이미지없음"
                전문가평점 = await item.query_selector(' .star_wrap > p.num')
                전문가평점 = await 전문가평점.inner_text() if 전문가평점 else "평점없음"
                print(영화제목 , 이미지링크 , 전문가평점)
                # 2-3 (데이터 적재): 수집된 데이터를 딕셔너리로 묶어 리스트에 저장하고 최종 출력한다.    
                item_list.append({"영화제목" : 영화제목 , "이미지링크" : 이미지링크 , "전문가평점" : 전문가평점})

    return item_list

items_list = asyncio.run( run() ) # 함수 실행 
for item in items_list:
    print(item)
# Practice7 문제 [ 씨네21(Cine21) 영화 평점 및 핵심 정보 수집 ]
# 출처 및 대상: 씨네21 영화 평점 페이지,  https://cine21.com/movie/point

import asyncio
from playwright.async_api import async_playwright 

url = "https://cine21.com/movie/point"



# [1. 목표]
# Playwright의 비동기 제어와 동적 페이지네이션(click)을 활용해 여러 페이지를 순회한다.
# 영화 아이템 카드에서 제목, 이미지 링크, 전문가 평점 3가지 핵심 데이터를 정확히 추출하여 구조화한다.

async def run( ) :
    item_list = [ ]
    # 2-1) async_playwright() 실행 하고 종료 되기 전까지 동기화 처리 지원 
    async with async_playwright() as p : 
        # 2-2) 크로미움( 구글 회사 제공 하는 백그라운드용 오픈소스 브라우저 )
        # await p.chromim.launch( headless = True백그라운드모드 /False뷰모드 ) 
        browser = await p.chromium.launch( headless = False )
        # 2-3) 현재 실행된 크로미움의 새로운 페이지(빈 페이지) 열기 , .new_page() 
        page = await browser.new_page() 
        # 2-4) 빈 페이지에 특정한 URL 주소 대입/이동 , .goto( url )
        await page.goto( url )

        # 3) 페이지 순회 , 1페이지부터 3페이지까지
        for page_no in range( 1 , 4 ) :
            # 3-1) 1페이지는 처음 접속했을 때 이미 보이므로 클릭 x 
            if page_no > 1 :
                # 페이지 번호 버튼 : <a href="javascript:fetch_point_list(2)">2</a>
                # a[href='값'] : href 속성값이 정확히 '값' 인 a 마크업 선택 ( c-04 의 href^ 와 같은 속성 선택자 )
                button = await page.query_selector( f"a[href='javascript:fetch_point_list({ page_no })']" )
                # 응답받은 HTML 로 #point_list_holder 안의 내용만 바뀐다 ( URL 주소는 그대로 )
                # page.expect_response( 조건 ) : with 안의 클릭 후 'list_items' 응답이 올때까지 대기상태
                async with page.expect_response( lambda res : "list_items" in res.url ) :
                    await button.click()                  # 특정한 마크업 클릭 이벤트 실행
                await page.wait_for_timeout( 3000 )   # 

            # 4) 특정 마크업 가져오기 , 영화 카드 여러개
            items = await page.query_selector_all( ".list_with_upthumb_item" )

            # 5) 반복문 이용한 영화 제목 / 이미지 / 전문가 평점
            for item in items :
                title = await item.query_selector( '.title' )
                title = await title.inner_text() if title else '제목없음'  # 마크업 사이 텍스트 추출
                img = await item.query_selector( 'img.img_thumb' )
                img = await img.get_attribute( 'src' ) if img else '이미지없음'  # 마크업의 속성값 추출
                # 평점( .star_wrap )은 '전문가' , '관객' 2개가 있을 수 있으므로
                # 평점 제목( .star_title )이 '전문가' 인 것의 점수( .num )만 추출
                score = '평점없음'
                stars = await item.query_selector_all( '.star_wrap' )
                for star in stars :
                    star_title = await star.query_selector( '.star_title' )
                    star_title = await star_title.inner_text() if star_title else ''
                    if star_title.strip() == '전문가' :
                        score = await star.query_selector( '.num' )
                        score = await score.inner_text() if score else '평점없음'
                # 6) 딕셔너리로 묶어 리스트에 담기
                item_list.append( { '페이지' : page_no , '제목' : title , '이미지링크' : img , '전문가평점' : score } )

            print( f"{ page_no }페이지 완료 : { len( items ) }개" )

        # 7) 안전하게 직접 브라우저 종료
        await browser.close()
    return item_list

# [2. 데이터 수집 요구사항]
# 2-1 (페이지 순회): 1페이지부터 3페이지까지 반복문을 통해 동적으로 페이지를 이동한다.
# 2-2 (요소 추출): 각 영화 카드 내부에서 아래 3가지 요소를 각각 수집한다.
# 영화 제목 # 이미지 # 전문가 평점

# 2-3 (데이터 적재): 수집된 데이터를 딕셔너리로 묶어 리스트에 저장하고 최종 출력한다.
item_list = asyncio.run( run() )
print( f"총 { len( item_list ) }개" )
for item in item_list :
    print( item )
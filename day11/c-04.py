import asyncio  # 비동기 라이브러리 (async/await 실행을 담당)
from playwright.async_api import async_playwright  # 비동기 방식의 playwright (브라우저 자동 조작)

# 예제4] 동적 크롤링
# 1) 중고나라 홈페이지 제품 크롤링
#   검색 주소 : https://web.joongna.com/search/검색어
#   상품 박스 : a 태그 중 href가 "/product/숫자" 로 시작하는 것
#   제목      : 상품 박스 안의 p 태그
#   가격      : 상품 박스 안의 span.typo-title-lg-semibold-18

# 사용자에게 검색어와 가격 범위 입력받기 (input은 항상 문자열로 받음)
keyword = input("중고 제품명 : ")
min_price = input("최소 가격 : ")
max_price = input("최대 가격 : ")

url = f"https://web.joongna.com/search/{keyword}"

async def run() :
    # 2) async_playwright() 실행하고 끝날때까지 대기상태
    async with async_playwright() as p :
        # 3) 크로미움 실행 (중고나라는 headless=True 이면 접속이 차단되므로 False 유지)
        browser = await p.chromium.launch( headless=False )
        # 4) 빈 페이지 열기
        page = await browser.new_page()
        # 5) 특정 페이지 이동
        await page.goto( url )
        # 해당 내용까지는 웬만하면 고정, 복붙해서 사용해도 무방함. 


        # 6) 3초 대기상태 (페이지가 다 그려질 때까지)
        await page.wait_for_timeout( 3000 )

        # 7) 입력받은 값으로 웹페이지 채우기
        #    get_by_placeholder : 입력칸에 흐리게 적힌 안내문구(placeholder)로 입력칸 찾기
        #    fill : 입력칸에 글자 채우기
        await page.get_by_placeholder( "최소 가격" ).fill( min_price )
        await page.get_by_placeholder( "최대 가격" ).fill( max_price )

        # 8) '적용' 버튼 클릭 → 가격 필터가 적용된 검색 결과로 바뀜
        #    get_by_role("button", name="적용") : 글자가 '적용'인 버튼 찾기
        await page.get_by_role( "button", name="적용" ).click()
        # 9) 필터 결과가 로딩될 때까지 3초 대기
        await page.wait_for_timeout( 3000 )

        # 10) 상품 박스 전부 가져오기
        #     a[href^="/product/"] : href 속성이 "/product/" 로 시작하는 a 태그
        items = await page.query_selector_all( 'a[href^="/product/"]' )

        # 결과를 담을 빈 리스트
        product_list = []

        # 11) 여러개 상품 박스에서 제목, 가격, 링크 하나씩 꺼내기
        for item in items :
            # 11-1) 제목 태그(p)와 가격 태그(span) 찾기
            title_tag = await item.query_selector( 'p' )
            price_tag = await item.query_selector( 'span.typo-title-lg-semibold-18' )

            # 11-2) 제목이나 가격이 없는 a 태그(예: '판매하기' 버튼)는 상품이 아니므로 건너뛰기
            if not title_tag or not price_tag :
                continue

            # 11-3) 태그에서 글자와 링크 꺼내기
            title = await title_tag.inner_text()                # 상품 제목
            price = await price_tag.inner_text()                # 가격 (예: 149,000)
            link = await item.get_attribute( 'href' )           # 상세페이지 주소 (예: /product/232979771)

            # 11-4) 딕셔너리로 만들어 리스트에 담기
            product_list.append( { "제목" : title , "가격" : price + "원" , "링크" : "https://web.joongna.com" + link } )

        # 12) 브라우저 닫기
        await browser.close()

        # 13) 결과 출력
        print( f"총 {len(product_list)}개" )
        for product in product_list :
            print( product )

# 비동기 함수 실행
asyncio.run(run())
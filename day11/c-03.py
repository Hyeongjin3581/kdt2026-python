# 예제] 네이버 이미지 검색 결과 크롤링 (동적 페이지 + 스크롤)

import asyncio  # 비동기 라이브러리 (async/await 실행을 담당)
from playwright.async_api import async_playwright  # 비동기 방식의 playwright (브라우저 자동 조작)

# 크롤링할 주소: https://search.naver.com/search.naver?where=image&query=메이플스토리 렌
#   where=image : 이미지 검색 탭
#   query=메이플스토리 렌  : 검색어
# 개발자도구(F12)로 찾은 클래스명
#   박스(이미지 1개 단위) : tile_item
#   이미지               : _fe_image_tab_content_thumbnail_image
#   제목                 : info_title


async def naverRun():  # async def : 비동기 함수 선언 (안에서 await 사용 가능)
    # async_playwright() 실행 → with 블록이 끝나면 playwright 자동 종료
    async with async_playwright() as p:
        # 1) 크로미움 브라우저 실행 (headless=False : 브라우저 창을 눈으로 보이게 실행)
        browser = await p.chromium.launch(headless=False)

        # 2) 크롤링할 페이지 주소
        url = 'https://search.naver.com/search.naver?where=image&query=메이플스토리 렌'

        # 3) 새로운 페이지(탭) 열기
        page = await browser.new_page()

        # 4) 해당 url로 이동
        await page.goto(url)

        # 5) 스크롤 2번 내리기
        #    네이버 이미지는 스크롤을 내려야 다음 이미지가 추가로 로딩되는 동적 페이지
        for i in range(2):
            await page.wait_for_timeout(3000)  # 3초 대기 (이미지가 로딩될 시간 주기)
            # 자바스크립트 실행 : 페이지 맨 아래(전체 높이)까지 스크롤
            await page.evaluate("window.scrollTo( 0 , document.body.scrollHeight )")

        # 6) 이미지 박스(.tile_item) 전부 가져오기 → 리스트로 반환
        items = await page.query_selector_all('.tile_item')

        # 결과를 담을 빈 리스트
        image_list = []

        # 7) 여러 개의 박스(item)에서 제목과 이미지 주소 하나씩 꺼내기
        for item in items:
            # 7-1) 제목 태그 찾기 (.info_title 안의 .txt)
            title_tag = await item.query_selector('.info_title .txt')
            # 제목 태그가 있으면 글자를 가져오고, 없으면 '제목없음'
            image_title = await title_tag.inner_text() if title_tag else '제목없음'

            # 7-2) 이미지 태그 찾기 (img 태그 중 해당 클래스를 가진 것)
            image_tag = await item.query_selector('img._fe_image_tab_content_thumbnail_image')
            # 이미지 태그가 있으면 src(이미지 주소) 속성값을 가져오고, 없으면 '링크없음'
            image_link = await image_tag.get_attribute('src') if image_tag else '링크없음'

            # 7-3) 딕셔너리로 만들어 리스트에 담기
            image_list.append({'제목': image_title, '링크': image_link})

        # 8) 브라우저 닫기
        await browser.close()

        # 9) 결과 출력
        print(image_list)


# 비동기 함수 실행 (asyncio.run : 일반 파이썬 코드에서 async 함수를 실행하는 입구)
asyncio.run(naverRun())
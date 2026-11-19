import pandas as pd
# 리뷰 데이터셋
url = "https://raw.githubusercontent.com/bab2min/corpus/master/sentiment/naver_shopping.txt"
df = pd.read_table(url, names=['rating', 'review'])
df = df[df['rating'] != 3]
df['label'] = (df['rating'] >= 4).astype(int)
# 전체 데이터셋에서 특정 n개 샘플링
df_sample = df.sample(n=10000, random_state=42).reset_index(drop=True)
print(df_sample.shape)  # (5000,3)
print(df_sample.head(3) )
# 1) 텍스트에서 전처리 = 정규표현식 자주 사용됨. vs 리액트/JS 입력 유효성검사
import re   # 정규표현식 함수
cleaned_list = []    # 정규표현식 통과한 목록
for text in df_sample['review']:    # 리뷰들을 반복
    # re.sub(r'[표현식]', '치환문자', str() )
    text = re.sub(r'[^가-힣a-zA-Z0-9\s]',' ', str(text) )
    # .join() vs .split() : 하나의 문자열내 특정문자로 분리하여 리스트 반환
    cleaned_text = ' '.join( text.split() ) # '대한 민국' -> ['대한','민국 ]
    cleaned_list.append(cleaned_text)
df_sample['cleand_review'] = cleaned_list
print(df_sample.head(3))

# 2) 한국어 형태소 분석기, kiwi
from kiwipiepy import Kiwi # 0.설치 : pip install kiwipiepy  
kiwi = Kiwi()   # 1. 한국어 형태소 분석기 객체 생성
for word in ['가성비', '내돈내산', '총알배송']:  # 3. 사전 학습에 없는 단어 추가
    # kiwi.add_user_word('새로운단어','품사키워드')
    kiwi.add_user_sord(word,'NNG')
# 4. 불용어 : 핵심 의미가 없는 형태소를 1차적으로 걸러내기 위해
from kiwipiepy.utils import Stopwords
kiwi_stopwords = Stopwords()
custom_stopwords = {'기미끼히잉' , '예?' , '티~원'}
# 5. kiwi 이용한 형태소 분석 함수
def tokenize_kiwi ( text ):
    # kiwi.tokenize( 분석할 문장 , stopwords=불용어객체)
    tokens = kiwi.tokenize( text , stopwords=kiwi_stopwords ) 
    # 추출할 품사 키워드 , NNG 일반명사 , NNP고유명사 , VV동사 VA 형용사 MAG일반부사
    target_tags = { 'NNG' , 'NNP' , 'VV' , 'VA' , 'MAG' }
    result=[]
    for t in tokens : # 토큰나이즈가 된 리스트에서 원하는것만 필터링 / 추출
        # t.tag : 품사 , t.form 형태소문자열 반환
        if t.tag in target_tags and t.form not in custom_stopwords : # 내가 원하는 품사에 포함된 단이어면, 
            if len( t.form) > 1 or t.form in { '못' , '잘' } :  # 일부 제외한 한단어 제외
                # 동사와 형용사어간 뒤에 다 붙인다. 좋고 / 좋아서 / 좋네요 -> 좋다
                # 파이썬 삼항연산자 ( if 조건 else 거짓 )
                word = t.form + '다' if t.tag in { 'VV' , 'VA' } else t.form
                result.append(word) 



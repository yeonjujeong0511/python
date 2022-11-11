import googletrans
# 설치한 모듈 가져오기
translate_worker = googletrans.Translator()
# 설치한 모듈 사용법 : googletrans.Translator()
# 설치한 모듈의 생성자 함수에 접근한 데이터를 translate_worker 라는 변수에 가리킴
input_data = input('영어로 번역하고 싶은 한글을 입력하세요 >> ')
# REPL 환경에서 입력 데이터를 받음
result_value = translate_worker.translate(input_data, dest="en")
# 엑세스한 생성자함수에 내장된 translate() 메서드 호출
print(result_value.text)
#결과물 출력



# 영어로 번역하고 싶은 한글을 입력하세요 >> 안녕
# hi
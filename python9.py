import json

# 자바스크립트와는 다르게 json 모듈을 파일 내에 가져와야 지원된다.
pokemon_dict = {
  "id" : 1,
  "name" : "이상해씨",
  "type" : "풀"
}

with open ("./pokemon_dict.json", "w", encoding="UTF-8") as file:
    json.dump(pokemon_dict,file,indent=2,ensure_ascii=False)

# 파이썬은 기본적으로 런타임에서 실행하는 언어이기 때무에
# 역으로 자바스크립트가 file system을 불러들여오는 과정이 필요없는 것이 특징

# 파일을 열고 닫는 개념으로 독특한 파일시스템 문법을 지원하는데
# with as 문법으로, 술어로 표현하면 다음과 같다.
# "파일을 열게, 이런 방식으로 이것을 할 거야, 이런 규칙이야"
# "실행구문이 끝나면 파일을 닫아줘"

# json.dump()가 자바스크립트에서의 JSON.stringify()역할을 하며,
# 인코딩 방식 중 영어만 사용할 수 있는 ascii코드를 막아둔것이 차이점이다.


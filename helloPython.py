print("hello world")
# 파이썬 출력 방법

monday_end_price = 10000 - ( 10000 * 0.3)
print(monday_end_price)
tuesday_end_price = monday_end_price - (monday_end_price * 0.3)
print(tuesday_end_price)
# 파이썬 변수 선언

x = 100
y = 100
print(id(x)) 
# 1909301185872
print(id(y))
# 1909301185872
z = 1000
print(id(z))
# 2462092075248

print(id(monday_end_price)) 
# 1660227789264
# 파이썬 바인딩


# 정숫값(Integer) 중 자주 사용할 것 같은 범위의 정숫값은 메모리에 한번 만 올려주고 가리키게 함으로써 메모리를 효과적으로 사용
# 숫자 256까지

mystring = 'hello world'
print(len(mystring))
# 11 공백도 문자로 인식
print(mystring[0:5])
# hello

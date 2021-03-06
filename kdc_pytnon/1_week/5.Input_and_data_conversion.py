'''
입력과 자료형 변환
input 입력함수
사용자로부터 데이터를 입력 받는 함수
'''

# x = input("입력하세요 :")
# 할당 연산자 (=) 오른쪽부터 실행
# input 함수 실행 시 입력을 기다린다  + 메세지를 넣으면 메세지를 출력하고 입력을 기다림
#사용자가 데이터를 입력하고 엔터를 치면
# input 함수 자리에 데이터가 들어간다

a = input('첫번쨰 숫자를 입력하세요') # 20을 넣어보세요
b = input('두번쨰 숫자를 입력하세요') # 40을 넣어보세요
result = a + b
print(result)   # str 형식이여서 더해지지않음  (str 은 문자열 이라고함)
print(type(result))

# int (숫자 정수형으로 변환 해주어야함)
result2 = int(a) + int(b)
print(type(result2))
print(result2)  # 60이 나오게 출력하세요


''' 실습문제 
사용자로부터 태어난 연도를 입력 받으면  현제 나이 출력하기
입력 :태어난 연도를 입력하세요 -> 1994 
출력 : 현재나이는 28살입니다
'''

year =int(input(" 태어난 연도를 입력하세요 >>>"))
age = 2022 - year + 1 # 한국은 태어날 때 부터 1살
print('현재 나이는', age,"세 입니다")


'''
정리
1.사용자로 부터 입력 받기
    input ("입력할 시 출력할 메세지")

2.자료형 변환
    숫자형으로 변환
    int(데이터)
'''
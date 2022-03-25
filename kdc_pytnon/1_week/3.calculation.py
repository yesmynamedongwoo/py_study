'''
연산이란?
수나 식을 일정한 규칙에 따라 계산하는것

대표적으로 4개로 나눌수있음
대입연산  산술연산  비교연산   논리연산

대입연산
    변수이름 = 데이터   대입연산자 또는 할당연산자

산술연산
    연산자  + 더하기 - 뺴기 * 곱하기 / 나누기 // 몫 % 나머지 **제곱

'''

# 1. 대입연산
# 변수이름 = 데이터

#2. 산술연산
#  - 숫자연산
x = 5
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) # 몫
print(x % y) # 나머지
print(x ** y) # 제곱

# -문자열 연산

tag1 = "#내꺼하자"
tag2 = "#오늘부터 1일"
tag3 = "# 여친생김"

tag = tag1 + tag2 + tag3
print(tag)
message = "우린 모두 파이썬을 사랑합니다. \n " * 5  # \n 줄바꿈
print(message)

#복합 할당 연산자
level = 10 # 레벨 1 증가)
# level = level + 1
level += 1

health = 2000 # 체력 300 감소
health -= 300 # health = health -300

attack = 300 # 공격력 1.5 배 증가
attack *= 1.5

speed = 420 # 이동속도 절반 감소
speed /=2 # speed = speed / 2

print(level,health,attack,speed)
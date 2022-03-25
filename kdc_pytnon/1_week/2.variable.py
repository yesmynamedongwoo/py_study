'''
변수란?
    데이터를 저장할 공간
    언제든지 데이터를 변경할 수 있다.

    변수이름 = 데이터

    = <- 할당 연산자   : 데이터를 변수이름에 저장한다

    변수 이름 짓는 규칙
            데이터를 표현할수있는 이름으로 짓는다
            문자부터 시작해야 한다
            대소문자는 구분한다
            _로 시작할수있다
            미리 예약된 키워드는 사용할 수 없다
'''

#변수
#변수이름 = 데이터

# 탐 켄치 챔피언 데이터를 변수에 저장

name = "탐 켄치"
level = 6
health = 1000
attack = 90
print(name,level,health,attack)

#  변수에 저장된 데이터를 변경하기

level = level + 1  # 6 + 1
health = health + 50 # 1000 + 50
attack = 100

print(name,level,health,attack)
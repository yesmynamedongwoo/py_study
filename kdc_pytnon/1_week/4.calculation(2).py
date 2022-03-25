'''
비교연산
    > 크다
    < 작다
    >= 크거나 같다
    <= 작거나 같다
    == 같다
    != 다르다

논리연산
    A and B      A,B 모두 참이라면 True
    A or B       A,B 중 하나라도 참이면 True
    not A       A 가 참이라면 False
    in          포함되어있다
    not in      포함되어있지않다

'''

# 1. 비교연산
print('비교연산 문제')
print( 2 > 3) #False
print(15 < 30) #True
print(1.5 >= 0) #True
print(3<= 3) #True
print("팙팔팙" == "팙팙팙") #False
print("111111111111111111" !="1111111111111111111") #True

# 2. 논리연산
print('논리연산 문제')
print(4 < 6 and  10 >=10) #True
print("포기하지말아요" != "포기하지말아요" or "나는 할 수 있다" =="나는 할 수 있다") #True
print(not 5==5) #False

#3. 멤버십 연산
print("멤버십 연산 문제")
print("A" in "ABC") #True
print("d" not in "abc") #True

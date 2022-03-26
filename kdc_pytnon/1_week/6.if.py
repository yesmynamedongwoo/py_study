'''
제어문을 사용하는 이유
    프로그램은 기본적으로 위에서 아래로 순차적으로 실행
    명령 a,b 한개만 실행하고 싶을때 - 조건문    치킨 or 피자
    명령들을 반복해서 실행하고 싶을떄 - 반복문   유튜브 영상보기

'''


origin_pass = "1234"
input_pass = input('패스워드를 입력하세요 >>>')
if origin_pass == input_pass: #조건 A
    print('로그인 성공!')
    print('반갑습니다.')

elif input_pass == '': #조건 B
    print('아무것도 입력하지 않았습니다')


else: # 그 외외
    print('실패')
    print('비밀번호를 확인하세요')
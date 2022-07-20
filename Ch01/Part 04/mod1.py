def add(a,b):
    return a + b

def sub(a,b):
    return a - b

#if__name__=="__main__":의 의미
#add(1,4)와 sub(4,2)의 결과를 출력하는 문장을 추가하였다.
#그런데 이 mod1.py 파일의 add와 sub 함수를 사용하기 위해 mod1 모듈을 import 할 때는 좀 이상한 문제가 생긴다.
#엉뚱하게도 import mod1을 수행하는 순간 mod1.py가 실행되어 결괏값을 출력한다. 우리는 단지 mod1.py 파일의 add와 sub 함수만 사용하려고 했는데 말이다.
#이러한 문제를 방지하려면 mod1.py 파일을 다음처럼 변경해야 한다.

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

if __name__ == "__main__":
    print(add(1,4))
    print(sub(6,2))

#if __name__ == "__main__"을 사용하면 직접 이 파일을 실행했을 때는 __name__=="__main__"이 참이 되어 if문 다음 문장이 수행된다. 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.

#점프 투 파이썬 __name__ 변수란?
#파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다. 만약 mod1.py처럼 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.
#하지만 파이썬 셀이나 다른 파이썬 모듈에서 mod1을 import할 경우에는 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.

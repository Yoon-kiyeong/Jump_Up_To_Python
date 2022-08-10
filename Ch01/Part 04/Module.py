#2022.07.20
#모듈
#모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일이다.
#모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 할 수 있다.
#우리는 파이썬으로 프로그램을 할 때 굉장히 많은 모듈을 사용한다.
#다른 사람이 이미 만들어 놓은 모듈을 사용할 수도 있고, 우리가 직접 만들어서 사용할 수도 있다.

#모듈 만들기
#모듈에 대해 자세히 살펴보기 전에 간단한 모듈을 만들어 보자.
#mod1.py
# def add(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

#위와 같이 add와 sub 함수만 있는 파일 mod1.py를 만들고 저장했다. 이 mod1.py 파일이 바로 모듈이다.

#모듈 불러오기
#우리가 만든 mod1.py파일, 즉 모듈을 파이썬에서 불러와 사용하려면 어떻게 해야 할까?
#다음과 같이 따라 해 보자.
import mod1
print(mod1.add(3,4))
print(mod1.sub(6,2))
#mod1.py를 불러오기 위해 import mod1이라고 입력하였다. 실수로 import mod1.py로 입력하지 않도록 주의하자.
#import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어이다.
#mod1.py파일에 있는 add함수를 사용하기 위해서는 위 예와 같이 mod1.add처럼 모듈 이름 뒤에 '.'(도트 연산자)를 붙이고 함수 이름을 쓰면 된다.

#import의 사용 방법은 다음과 같다.
#import 모듈 이름
#여기에서 모듈 이름은 mod1.py에서 .py확장자를 제거한 mod1만 가리킨다.
#때로는 mod1.add,mod1.sub처럼 쓰지 않고, add,sub처럼 모듈 이름 없이 함수 이름만 쓰고 싶은 경우도 있을 것이다. 이럴 때는 'from 모듈 이름 import 모듈 함수'를 사용하면 된다.
#from 모듈 이름 import 함수 이름
#위 형식을 사용하면 위와 같이 모듈 이름을 붙이지 않고 바로 해당 모듈의 함수를 쓸 수 있다.
#다음과 같이 따라해 보자
from mod1 import add
print(add(3,4))

#그런데 위와 같이 하면 mod1.py파일의 add함수만 사용할 수 있다. add 함수와 sub 함수를 둘 다 사용하고 싶다면 어떻게 해야 할까?
#2가지 방법이 있다.
#from mod1 import add,sub
#첫 번재 방법은 위와 같이 from 모듈 이름 import 모듈 함수1, 모듈 함수2 처럼 사용하는 것이다. 콤마로 구분하여 필요한 함수를 불러올 수 있다.

#from mod1 import * 
#두번째 방법은 위와 같이 * 문자를 사용하는 방법이다. * 문자는 '모든 것'이라는 뜻인데, 파이썬에서도 마찬가지 의미로 사용한다. 따라서 from mod1 import *는 mod1.py의 모든 함수를 불러서 사용하겠다는 뜻이다.\
#mod1.py 파일에는 함수가 2개밖에 없기 때문에 위 2가지 방법은 동일하게 적용된다.

#클래스나 변수 등을 포함한 모듈
#지금까지 살펴본 모듈은 함수만 포함했지만 클래스나 변수 등을 포함할 수도 있다. 다음 프로그램을 작성해 보자
import mymod.mod2 as mod2
print(mod2.PI)

#위 예에서 볼 수 있듯이 mod2.PI처럼 입력해서 mod2.py 파일에 있는 PI 변수 값을 사용할 수 있다.
a = mod2.Math()
print(a.solv(2))
#위 예는 mod2.py에 있는 Math 클래스를 사용하는 방법을 보여 준다. 위 예처럼 모듈 안에 있는 클래스를 사용하려면 '.'(도트 연산자)로 클래스 이름 앞에 모듈 이름을 먼저 입력해야 한다.
print(mod2.add(mod2.PI, 4.4))
#mod2.py에 있는 add함수 역시 당연히 사용할 수 있다.

#나 혼자 코딩 mod2.py 모듈을 사용해 반지름이 5인 원의 넓이를 계산해 보자.
import mymod.mod2 as mod2
a = mod2.Math()
print(a.solv(5))
print()
#다른 파일에서 모듈 불러오기
#여기서는 다른 파이썬 파일에서 이전에 만들어 놓은 모듈을 불러와서 사용하는 방법에 대해 알아보자.
#여기에서는 조금 전에 만든 모듈인 mod2.py 파일을 다른 파이썬 파일에서 불러와 사용할 것이다.
#modtest.py
# import mod2
# result = mod2.add(3,4)
# print(result)

#위에서 볼 수 있듯이 다른 파이썬 파일에서도 improt mod2로 mod2 모듈을 불러와서 사용할 수 있다.
#위 예제가 정상적으로 실행되기 위해서는 modtest.py 파일과 mod2.py 파일이 동일한 디렉터리에 있어야 한다.

#점프 투 파이썬 모듈을 불러오는 또 다른 방법
#우리는 지금껏 명령 프롬프트 창을 열고 모듈이 있는 디렉터리로 이동한 다음에 모듈을 사용할 수 있었다.
#이번에는 모듈을 저장한 디렉터리로 이동하지 않고 모듈을 불러와서 사용하는 방법에 대해 알아보자.
#먼저 다음과 같이 이전에 만든 mod2.py파일을 이동시킨다.
#그리고 다음 예를 따라 해 보자.

#1. sys.path.append(모듈을 저장한 디렉터리) 사용하기
import sys
#sys 모듈은 파이썬을 설치할 때 함께 설치되어 있는 라이브러리 모듈이다. 이 sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다.
#다음과 같이 입력해 보자.
print(sys.path)
#sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여 준다. 만약 파이썬 모듈이 위 디렉터리에 들어 있다면 모듈이 저장되어 있는 디렉터리로 이동할 필요 없이 바로 불러서 사용할 수 있다.
#그렇다면 sys.path에 mymod 디렉터리를 추가하면 아무 곳에서나 불러 사용할 수 있지 않을까?
#당연하다. sys.path의 결괏값이 리스트이므로 우리는 다음과 같이 사용할 수 있다.
print(sys.path.append("C:/doit/mymod"))
#sys.path.append를 사용해서 C:/doit/mymod라는 디렉터리를 sys.path에 추가한 후 다시 sys.path를 보면 가장 마짐가 요소에 C:/doit/mymod라고 추가된 것을 확인할 수 있다.
#자, 실제로 모듈을 불러와서 사용할 수 있는지 확인해 보자.
import mod2
print(mod2.add(3,4))
#이상 없이 불러와서 사용할 수 있다.

#2. PYTHONPATH 환경 변수 사용하기
#모듈을 불러와서 사용하는 또 다른 방법으로는 PYTHONPATH 환경 변수를 사용하는 방법이 있다.
#set 명령어를 사용해 PYTHONPATH 환경 변수에 mod2.py 파일이 있는 C:/doit/mymod 디렉터리를 설정한다. 그러면 디렉터리 이동이나 별도의 모듈 추가 작업 없이 mod2 모듈을 불러와서 사용할 수 있다.
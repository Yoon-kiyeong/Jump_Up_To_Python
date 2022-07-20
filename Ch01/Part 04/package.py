#2022.07.20
#패키지
#패키지란 무엇인가?
#패키지(package)는 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다.
#예를 들어 모듈 이름이 A.B인 경우에 A는 패키지 이름이 되고 B는 A 패키지의 B 모듈이 된다.

#파이썬 패키지는 디렉터리와 파이썬 모듈로 이루어지며 구조는 다음과 같다
# game/
#     __init__.py
#     sound/
#         __init__.py
#         echo.py
#         wav.py
#     graphic/
#         __init__.py
#         screen.py
#         render.py
#     play/
#         __init__.py
#         run.py
#         test.py
#game,sound,graphic,play는 디렉터리 이름이고 확장자가 .py인 파일은 파이썬 모듈이다. game 디렉터리가 이 패키지의 루트 디렉터리이고 sound,graphic,play는 서브 디렉터리이다.

#간단한 파이썬 프로그램이 아니라면 이렇게 캐피지 구조로 파이썬 프로그램을 만드는 것이 공동 작업이나 유지 보수 등 여러 면에서 유리하다.
#또한 패키지 구조로 모듈을 만듦녀 다른 모듈과 이름이 겹치더라도 더 안전하게 사용할 수 있다.

#패키지 만들기
#이제 위 예와 비슷한 game 패키지를 직접 만들어 보며 패키지에 대해서 알아보자.

#패키지 기본 구성 요소 준비하기
#1.C:/doit 디렉터리 밑에 game 및 기타 서브 디렉터리르 생성하고 .py 파일들을 다음과 같이 ㅁ나들어 보자
#2.각 디렉터리에 __init__.py 파일을 만들어 놓기만 하고 내용은 일단 비워둔다.
#3.echo.py 파일은 다음과 같이 만든다.
# def echo_test():
#     print("echo")
#4.render.py 파일은 다음과 같이 만든다.
#def render_test():
    # print("render")
#5.다음 예제를 수행하기 전에 우리가 만든 game 패키지를 참조할 수 있도록 명령 프롬포트 창에서 set 명령어로 PYTHONPATH 환경 변수에 C:/doit 디렉터리를 추가한다.

#패키지 안의 함수 실행하기
#자, 이제 패키지를 사용하여 echo.py 파일의 echo_test 함수를 실행해 보자. 패키지 안의 함수를 실행하는 방법은 다음 3가지가 있다. 다음 예제는 import 예제이므로 하나의 예제를 실행하고 나서 다음 예제를 실행할 때에는 반드시 인터프리터를 종료하고 다시 실행해야 한다.
#인터프리터를 다시 시작하지 않을 경우 이전에 import한 것들이 메모리에 남아 있어 엉뚱한 결과가 나올 수 있다.
#첫 번쨰는 echo 모듈을 import하여 실행하는 방법으로, 다음과 같이 실행한다
import game.sound.echo
print(game.sound.echo.echo_test())

#두 번째는 echo 모듈이 있는 디렉터리까지를 from ... import하여 실행하는 방법이다.
from game.sound import echo
print(echo.echo_test())

#세 번째는 echo 모듈의 echo_test 함수를 직접 import 하여 실행하는 방법이다.
from game.sound.echo import echo_test
print(echo_test())

#도트 연산자(.)를 사용해서 improt a.b.c처럼 import 할 때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 한다.
print()
#__init__.py의 용도
#__init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. 만약 game,sound,graphic 등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.
#특정 디렉터리의 모듈을 *을 사용하여 import 할 때에는 다음과 같이 해당 디렉터리의 __init__.py 파일에 __all__변수를 설정하고 import 할 수 있는 모듈을 정의해 주어야 한다.
#C:/doit/game/sound/__init__.py
#__all__ = ['echo']
#여기에서 __all__이 의미하는 것은 sound 디렉터리에서 * 기호를 사용하여 import 할 경우 이곳에 정의된 echo 모듈만 import 된다는 의미이다.
#위와 같이 __init__.py 파일을 변경한 후 위 예제를 수행하면 원하는 결과가 출력되는 것을 확인할 수 있다.
from game.sound import *
print(echo.echo_test())

#relative 패키지
#만약 graphic 디렉터리의 render.py 모듈이 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면 어떻게 해야 할까?
#다음과 같이 render.py를 수정하면 가능하다.
#from game.sound.echo import echo_test()
#def render_test():
#   print("render")
#   echo_test()

#from game.sound.echo import echo_test 문장을 추가하여 echo_test 함수를 사용할 수 있도록 수정했다.
#이렇게 수정한 후 다음과 같이 수행해 보자
from game.graphic.render import echo_test, render_test
print(render_test())
#이상없이 잘 수행된다.

#위 예제처럼 from game.sound.echo import echo_test를 입력해 전체 경로를 사용하여 import 할 수도 있지만 다음과 같이 relative하게 import 하는 것도 가능하다.
# from ..sound.echo import echo_test

# def render_test():
#     print("render")
#     echo_test()
#from game.sound.echo import echo_test가 from ..sound.echo import echo_test로 변경되었다. 여기에서 .. 부모 디렉터리를 의미한다.
#graphic과 sound 디렉터리는 동일한 깊이(depth)이므로 부모 디렉터리(..)를 사용하여 위와 같은 import가 가능한 것이다.

#..과 같은 relative한 접근자는 render.py처럼 모듈 안에서만 사용해야 한다. 파이썬 인터프리터에서 relative한 접근자를 사용하면 'SystemError: cannot perform relative import' 오류가 발생한다.

#relative한 접근자에는 다음과 같은 것이 있다.
#..-부모 디렉터리
#.-현재 디렉터리
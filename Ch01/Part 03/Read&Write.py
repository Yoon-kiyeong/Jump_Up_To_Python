#2022.06.29
#파일 읽고 쓰기

#파일 생성하기
#다음 소스 코드를 에디터로 작성해서 저장한 후 실행해 보자. 프로그램을 실행한 디렉터리에 새로운 파일이 하나 생성된 것을 확인할 수 있다.
f = open("새파일.txt",'w')
f.close()

# 파일을 생성하기 위해 우리는 파이썬 내장 함수 open을 사용했다. open 함수는 다음과 같이 '파일 이름'과 '파일 열기 모드'를 입력값으로 받고 결괏값으로 파일 객체를 돌려준다.
# 파일 객체 = open(파일이름, 파일 열기 모드)

#파일 열기 모드에는 다음과 같은 것들이 있다.
#파일 열기 모드             설명
#r                  읽기 모드 - 파일을 읽기만 할 때 사용
#w                  쓰기 모드 - 파일에 내용을 쓸 때 사용
#a                  추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용

#파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성된다.
#위 예에서는 디렉터리에 파일이 없는 상태에서 새파일.txt를 쓰기 모드인 'w'로 열었기 때문에 새파일.txt라는 이름의 새로운 파일이 현재 디렉터리에 생성되는 것이다.

#만약 새 파일.txt 파일을 C:/doit 디렉터리에 생성하고 싶다면 다음과 같이 작성해야 한다.
#f = open("C:/doit/새파일.txt",'w')
#f.close()

#위 예에서 f.close()는 열려 있는 파일 객체를 닫아 주는 역할을 한다. 사실 이 문장은 생략해도 된다. 프로그램을 종료할 때 파이썬 프로그램이 열려 있는 파일의 객체를 자동으로 닫아주기 때문이다.
#하지만 close()를 사용해서 열려 있는 파일을 직접 닫아 주는 것이 좋다. 쓰기 모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생하기 때문이다.

#나 혼자 코딩! 복습.txt파일을 C:/doit 디렉터리에 만들어 보자.
f = open("C:/doit/복습.txt",'w')
f.close()

#파일을 쓰기 모드로 열어 출력값 얻기
#위 예에서는 파일을 쓰기 모드로 열기만 했지 정작 아무것도 쓰지는 않았다. 이번에는 프로그램의 출력값을 파일에 직접 써보자.
f = open("C:/doit/새파일.txt",'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#위 프로그램을 다음 프로그램과 비교해 보자.
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)
print()
#두 프로그램의 다른 점은 data를 출력하는 방법이다. 두 번째 방법은 우리가 계속 사용해 왔던 모니터 화면에 출력하는 방법이고, 첫 번째 방법은 모니터 화면 대신 파일에 결괏값을 적는 방법이다.
#두 방법의 차이점은 print 대신 파일 객체 f의 write 함수를 사용한 것 말고는 없으니 바로 눈에 들어올 것이다.

#프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
#파이썬에는 외부 파일을 읽어 들여 프로그램에서 사용할 수 있는 여러 가지 방법이 있다. 이번에는 그 방법에 대해 자세히 알아 보자.

#readline 함수 사용하기
#첫 번째 방법은 readline 함수를 사용하는 방법이다. 다음 예를 보자.
f = open("C:/doit/새파일.txt",'r')
line = f.readline()
print(line)
f.close()
#위 예는 f.open("새파일.text",'r')로 파일을 읽기 모드로 연 후 readline()을 사용해서 파일의 첫 번째 줄을 읽어 출력하는 경우이다. 앞에서 만든 새파일.txt를 수정하거나 지우지 않았다면 위 프로그램을 실행했을 때 새파일.txt의 가장 첫 번째 줄이 화면에 출력될 것이다.

#만약 모든 줄을 읽어서 화면에 출력하고 싶다면 다음과 같이 작성하면 된다.
f = open("C:/doit/새파일.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#즉 while True: 무한 루프 안에서 f.readline()을 사용해 파일을 계속해서 한 줄씩 읽어 들인다. 만약 더 이상 읽을 줄이 없으면 break를 수행한다. (readline()은 더 이상 읽을 줄이 없을 경우 None을 출력한다.)

#앞의 프로그램을 다음 프로그램과 비교해 보자.
while 1:
    data = input()
    if not data: break
    print(data)
    
#위 예는 사용자의 입력을 받아서 그 내용을 출력하는 경우이다. 파일을 읽어서 출력하는 예제와 비교해 보자. 입력을 받는 방식만 다르다는 것을 바로 알 수 있을 것이다.
#두 번째 예는 키보드를 사용한 입력 방법이고, 첫 번째 예는 파일을 사용한 입력 방법이다.

#readlines 함수 사용하기
#두 번째 방법은 readline 함수를 사용하는 방법이다. 다음 예를 보자
f  = open("C:/doit/새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다. 따라서 위 예는 lines는 리스트 ["1번째 줄입니다.", "2번째 줄입니다.",...,"10번째 줄입니다."]가 된다.
#f.readlines()에서 f.readlines()과는 달리 s가 하나 더 붙어 있음에 유의하자.

#read 함수 사용하기
#세 번째 방법은 read함수를 사용하는 방법이다. 다음 예를 보자
f = open("C:/doit/새파일.txt",'r')
data = f.read()
print(data)
f.close()

#f.read()는 파일의 내용 전체를 문자로 돌려준다. 따라서 위 예의 data는 파일의 전체 내용이다.

#파일에 새로운 내용 추가하기
#쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다. 하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우도 있다.
#이런 경우에는 파일을 추가 모드 ('a')로 열면 된다.
f = open("C:/doit/새파일.txt",'a')
for i in range(11,20): #11부터 19까지 i에 대입
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

#위 예는 새파일.txt파일을 추가 모드('a')로 열고 write를 사용해서 결괏값을 기존 파일에 추가해 적는 예이다.
#여기에서 추가 모드로 파일을 열었기 때문에 새파일.txt이 원래 가지고 있던 내용 바로 다음부터 결괏값을 적기 시작한다.

#with문과 함께 사용하기
#지금까지 살펴본 예제를 보면 항상 다음과 같은 방식으로 파일을 열고 닫아 왔다.
#f.write("Life is too short, you need python")
#f.close()

#파일을 열면 위와 같이 항상 close해 주는 것이 좋다. 하지만 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까?
#파이썬의 with문이 바로 이런 역할을 해준다.
#다음 예는 with문을 사용해서 위 예제를 다시 작성한 모습이다.
with open("foo.text",'w') as f:
   f.write("Life is too short, you need python")
#위와 같이 with문을 사용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close되어 편리하다.

#점프 투 파이썬 sys 모듈로 매개변수 주기
#명령 프롬포트(DOS)를 사용해 본 독자라면 다음과 같은 명령어를 사용해 봤을 것이다.
#C:/>type a.txt
#위 type 명령어는 바로 뒤에 적힌 파일 이름을 인수로 받아 그 내용을 출력해 주는 명령 프롬프트 명령어이다.
#대부분의 명령 프롬프트 명령어는 다음과 같이 명령행(명령 프롬프트 창)에서 매개변수를 직접 주어 프로그램을 실행하는 방식을 따른다.
#이러한 기능을 파이썬 프로그램에도 적용할 수가 있다.

#명령 프롬프트 명령어 [인수1, 인수2, ...]

#파이썬에서는 sys 모듈을 사용하여 매개변수를 직접 줄 수 있다. sys 모듈을 사용하려면 아래 예의 import sys처럼 import 명령어를 사용해야 한다.
import sys

args = sys.argv[1:]
for i in range:
    print(i)

#위 예는 입력받은 인수를 for문을 사용해 차례대로 하나씩 출력하는 예이다. sys 모듈의 argv는 명령 창에서 입력한 인수를 의미한다.
#즉 다음과 같이 입력했다면 argv[0]은 파일 이름 sys1.py가 되고 argv[1]부터는 뒤에 따라오는 인수가 차례로 argv의 요소가 된다.

#이 프로그램을 C:/doit 디렉터리에 저장한 후 매개변수를 함께 주어 실행하면 다음과 같은 결괏값을 얻을 수 있다.
#C:/doit>python sys1.ps aaa bbb ccc
#aaa
#bbb
#ccc

#위 예를 사용해서 간단한 스크립트를 하나 만들어 보자
import sys
args = sys.argv[1:]
for i in range:
    print(i.upper(), end=' ')

#문자열 관련 함수인 upper()를 사용해서 명령 행에 입력된 소문자를 대문자로 바꾸어 주는 간단한 프로그램이다.

#이 프로그램을 cL/doit 디렉터리에 저장한 후 매개변수를 함께 주어 실행해보자
#C:/doit>python sys2.py life is too short, you need python
#결과는 다음과 같다
#LIFE IS TOO SHORT, YOU NEED PYTHON


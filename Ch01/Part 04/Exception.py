#2022.07.25
#예외 처리
#프로그램을 만들다 보면 수없이 많은 오류를 만나게 된다. 물론 오류가 발생하는 이유는 프로그램이 잘못 동작하느 것을 막기 위한 파이썬의 배려이다.
#하지만 때때로 이러한 오률르 무시하고 싶을 때도 있다. 이를 위해 파이썬은 try, except를 사용해서 예외적으로 오류를 처리할 수 있게 해준다.

#오류는 어떨 떄 발생하는가?
#오류를 처리하는 방법을 아리 전에 어떤 상황에서 오류가 발생하는지 한번 알아보자. 오타를 입력했을 때 발생하는 구문 오류 같은 것이 아닌 실제 프로그램에서 자주 발생하는 오류를 중심으로 살펴본다.
#먼저 디렉터리 안에 없는 파일을 열려고 시도했을 때 발생하는 오류이다.
# f = open("나 없는 파일",'r')
#     f = open("나 없는 파일",'r')
# FileNotFoundError: [Errno 2] No such file or directory: '나 없는 파일'
#위 예에서 볼 수 있듯이 없는 파일을 열려고 시도하면 FileNotFoundError 오류가 발생한다.

#이번에는 0으로 다른 숫자를 나누는 경우를 생각해 보자. 이 역시 자주 발생하는 오류이다.
# 4 / 0
#     4 / 0
# Traceback (most recent call last):
# ZeroDivisionError: division by zero
#4를 0으로 나누려니까 ZeroDivisionError 오류가 발생한다.

#마지막으로 한 가지 예를 더 들어보자. 다음 오류는 정말 빈번하게 일어난다.

# a = [1,2,3]
# print(a[4])
# Traceback (most recent call last):
#     print(a[4])
# IndexError: list index out of range
#a는 리스트 [1,2,3]인데 a[4]는 a 리스트에서 얻을 수 없는 값이다. 따라서 IndexError 오류가 발생한다. 파이썬은 이런 오류가 발생하면 프로그램을 중단하고 오류 메시지를 보여준다.

#오류 예외 처리 기법
#자, 이제 유연한 프로그래밍을 위한 오류 처리 기법에 대해 살펴보자.

#try,except문
#다음은 오류 처릴르 위한 try,except문의 기본 구조이다. try 블록 수행 중 오류가 발생하면 except 블록이 수행된다.
#하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.
#try:
# ...
#except [발생 오류 [as 오류 메시지 변수]]:
#...

#except 구문을 자세히 살펴보자.
#except [발생오류 [as 오류 메시지 변수]]:
#위 구문을 보면 [] 기호를 사용하는데, 이 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이다. 즉 except 구문은 다음 3가지 방법으로 사용할 수 이다.

#1. try,except만 쓰는 방법
#이 경우는 오류 종류에 상관없이 오류가 발생하면 except블록을 수행한다.
#try:
#...
#except:
#...

#2. 발생 오류만 포함한 except문
#이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행한다는 뜻이다.

#3. 발생 오류와 오류 메시지 변수까지 포함한 except문
#이 경ㅇ는 두 번쨰 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법이다.
#try:
#...
# except 발생 오류 as 오류 메시지 변수:
#...

#이 방법의 예를 들어 보면 다음과 같다.
from ast import Index


try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

#나 혼자 코딩! 앞에서 나온 3번 방법을 사용해 IndexError가 발생할 때 오류 메시지를 출력하는 소스를 작성해 보자.
a = [1,2,3]
try:
    a[3]
except IndexError as i:
    print(i)
    
#try ... finally
#try 문에는 finnaly 절을 사용할 수 있다. finally 절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 보통 finally절은 사용한 리소스를 close해야 할 때 많이 사용한다.
#다음 예를 보자.
# f = open('foo.txt','w')
# try:
#     # 무언가를 수행한다.
# finally:
#     f.close()
#foo.txt 파일을 쓰기 모드로 연 후에 try문을 수행한 후 예외 발생 여부와 상관없이 finally절에서 f.close()로 열린 파일을 닫을 수 있다.
print()
#여러 개의 오류 처리하기
# #try문 안에서 여러 개의 오류를 처리하기 위해 다음 구문을 사용한다.
# try:
#     ...
# except 발생 오류 1:
#     ...
# except 발생 오류 2:
#     ...
#즉 0으로 나누는 오류와 인덱싱 오류를 다음과 같이 처리할 수 있다.
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 ㅇ벗습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")
#a는 2개의 요솟값을 가지고 있기 때문에 a[3]는 IndexError를 발생시키므로 '인덱싱할 수 없습니다' 라는 문자열이 출력될 것이다.
#인덱싱 오류가 먼저 발생했으므로 4/0으로 발생되는 ZeroDivisionError 오류는 발생하지 않았다.
print()
#앞에서 알아본 것과 마찬가지로 오류 메시지도 다음과 같이 가져올 수 있다.
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
#프로그램을 실행하면 list index out of range 오류 메시지가 출력될 것이다.
print()
#다음과 같이 ZeroDivisionError와 Index를 함께 처리할 수도 있다.
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
#2개 이상의 오류를 동시에 처리하기 위해서는 위와 같이 괄호를 사용하여 함께 묶어 처리하면 된다.

#오류 회피하기
#프로그래밍을 하다 보면 특정 오류가 발생할 경우 그냥 통과시켜야 할 때가 있다. 다음 예를 보자
try:
    f = open("나 없는 파일",'r')
except FileNotFoundError: #파일이 없더라도 오류를 발생시키지 않고 통과한다.
    pass
#try문 안에서 FileNotFoundError가 발생할 경우에 pass를 사용하여 오류를 그냥 회피하도록 작성한 예제이다.

#오류 일부러 발생시키기
#이상하게 들리겠지만 프로그래밍을 하다 보면 종종 오류를 일부러 발생시켜야 할 경우도 생긴다.
#파이썬은 raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다.

#예를 들어 Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우(강제로 그렇게 하고 싶은 경우)가 있을 수 있다. 다음 예를 보자.
class Bird:
    def fly(self):
        raise NotImplementedError
#위 예제는 Bird 클래스를 상속받는 자식 클래스는 반드시 fly 함수를 구현해야 한다는 의지를 보여 준다.
#만약 자식 클래스가 fly 함수를 구현하지 않은 상태로 fly 함수를 호출한다면 어떻게 될까?
# class Eagle(Bird): #Eagle 클래스는 Bird 클래스를 상속 받음
#     pass

# eagle = Eagle()
# eagle.fly()
#Eagle 클래스는 Bird 클래스를 상속받는다. 그런데 Eagle 클래스에서 fly 함수를 구현하지 않았기 때문에 Bird 클래스의 fly 함수가 호출된다. 그리고 raise문에 의해 NotImplementedError가 발생할 것이다.
# Traceback (most recent call last):
#   File "c:\Users\Yoon\Desktop\Github Desktop\Jump_Up_To_Python\Ch01\Part 04\Exception.py", line 150, in <module>
#     eagle.fly()
#   File "c:\Users\Yoon\Desktop\Github Desktop\Jump_Up_To_Python\Ch01\Part 04\Exception.py", line 143, in fly
#     raise NotImplementedError
# NotImplementedError

#상속받는 클래스에서 함수를 재구현하는 것을 메소드 오버라이딩이라고 부른다.
print()
#NotImplementedError가 발생되지 않게 하려면 다음과 같이 Eagle 클래스에 fly함수를 반드시 구현해야 한다.
class Eagle(Bird):
    def fly(self):
        print("very fast")
        
eagle=Eagle()
eagle.fly()
#위 예처럼 fly 함수를 구현한 후 프로그램을 실행하면 오류 없이 다음 문장이 출력된다.
#very fast

#예외 만들기
#프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 예외를 만들어서 사용한다. 직접 예외를 만들어 보자.
#예외는 다음과 같이 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.
class MyError(Exception):
    def __str__ (self):
        return "허용되지 않는 별명입니다."
#그리고 별명을 출력해 주는 함수를 다음과 같이 작성한다.
def say_nick(nick):
    if nick == '이디엇':
        raise MyError()
    print(nick)
# #그리고 다음과 같이 say_nick 함수를 호출해 보자
# print(say_nick("천사"))
# print(say_nick("이디엇"))
# #저장한 뒤 프로그램을 실행해 보면ㄴ 다음과 같이 '천사'가 한 번 출력된 후 My Error가 발생한다.
# 천사
# None
# Traceback (most recent call last):
#   File "c:\Users\Yoon\Desktop\Github Desktop\Jump_Up_To_Python\Ch01\Part 04\Exception.py", line 184, in <module>
#     print(say_nick("이디엇"))
#   File "c:\Users\Yoon\Desktop\Github Desktop\Jump_Up_To_Python\Ch01\Part 04\Exception.py", line 180, in say_nick
#     raise MyError()
# __main__.MyError
print()
#이번에는 예외 처리 기법을 사용하여 MyError 발생을 예외 처리해 보자.
try:
    say_nick("천사")
    say_nick("이디엇")
except MyError:
    print("허용되지 않는 별명입니다.")
#프로그램을 실행하면 다음과 같이 출력된다
#천사
#허용되지 않는 별명입니다.

#만약 오류 메시지를 사용하고 싶다면 다음처럼 예외 처리를 하면 된다.
try:
    say_nick("천사")
    say_nick("이디엇")
except MyError as e :
    print(e)
    
#하지만 프로그램을 실행해 보면 print(e)로 오류 메시지가 출력되지 않는 것을 확인할 수 있다. 오류 메시지를 출력했을 떄 오류 메시지가 보이게 하려면 오류 클래스에 다음과 같은 __str__ 메소드를 구현해야 한다.
#__str__ 메소드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메소드이다.
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
#프로그램을 다시 실행해 보면 "허용되지 않는 별명입니다."라는 오류메시지가 출력되는 것을 확인할 수 있다.


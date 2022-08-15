#2022.08.15
#Q1. 다음은 Calcutalor 클래스이다.
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
#위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메소드를 추가해 보자.
#즉 다음과 같이 동작하는 클래스를 만들어야 한다.
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
    
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)    #10에서 7을 뺀 3을 출력

#Q2. 객체변수 Value가 100 이상의 값은 가질 수 없도록 제헌하는 MaxLimitCalculator 클래스를 만들어 보자. 즉 다음과 같이 동작해야 한다.

#Calculator 클래스를 상속하고 add 메소드를 오버라이딩하여 다음과 같은 클래스를 만든다.
class MaxLimitCalculator(Calculator):
    def add(self,val):
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)     #50 더하기
cal.add(50)     #60 더하기

print(cal.value)    #100 출력

#단 반드시 다음과 같은 Calculator 클래스를 상속해서 만들어야 한다.
# class Calculator:
#     def __init__(self):
#         self.value = 0

#     def add(self, val):
#         self.value += val

#Q3. 다음 결과를 예측해 보자.
#1. all([1, 2, abs(-3)-3])
#False
#abs(-3)은 -3의 절댓값이므로 3이 되어 all([1,2,0])이 되고, 리스트의 요솟값 중 0이 있기 때문에 all 내장 함수의 결과는 False가 된다.

#2. chr(ord('a')) == 'a'
#True
#ord('a')의 결과는 97이 되어 chr(97)로 치환된다. chr(97)의 결과는 다시 'a'가 되므로 'a' == 'a'가 되어 True를 돌려 준다.

#Q4. filter와 lambda를 사용하여 리스트 [1,-2,3,-5,8-,3]에서 음수를 모두 제거해 보자.
#음수를 제거하기 위한 filter의 함수로 lambda 함수를 다음과 같이 만들어 실행한다.
print(list(filter(lambda x:x>0,[1,-2,3,-5,8,-3])))

#Q5.234라는 10진수의 16진수는 ㄷ음과 같이 구할 수 있다.
print(hex(234))
#이번에는 반대로 16진수 문자열 0xea를 10진수로 변경해 보자.
print(int('0xea',16))

#Q6.Map과 lambda를 사용하여 [1,2,3,4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3,6,9,12]를 만들어 보자.
#입력에 항상 3을 곱하여 돌려 주는 lambda 함수를 다음과 같이 만들고 map과 조합하여 실행한다.
print(list(map(lambda x:x*3,[1,2,3,4])))

#Q7.다음 리스트의 최댓값과 최솟값의 합을 구해보자.
a = [-8,2,7,5,-3,5,0,1]
print(max(a) + min(a))

#Q8. 17 / 3 의 결과는 다음과 같다.
print(17 / 3 )
#5.666666666666667
#위와 같은 결괏값 5.666666666666667을 소숫점 4자리까지만 반올림하여 표시해 보자.
print(round(17/3,4))

#Q9. 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트(C:/doit/myargv.py)를 작성해 보자.
#C:>cd doit
#C:/doit>python myargv.py 1 2 3 4 5 6 7 8 9 10
#55

#다음처럼 sys모듈의 argv를 사용하여 명령 행 입력값 모두를 차례로 더해 준다.
import sys

numbers = sys.argv[1:]  #파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)
print(result)

#Q10. os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
#1. C:>doit 디렉터리로 이동한다.
#다음처럼 os 모듈의 chdir을 사용하여 C:/doit 이라는 디렉터리로 이동한다.
import os
print(os.chdir("c:/doit"))
#2. dir 명령을 실행하고 그 결과를 변수에 담는다.
#그리고 다음처럼 os 모듈의 popen을 사용하여 시스템 명령어인 dir을 수행한다.
result = os.popen("dir")
#3. dir 명령의 결과를 출력한다.
#opoen의 결과를 출력하기 위해 다음과 같이 수행한다.
print(result.read())

#Q11. glob 모듈을 사용하여 C:/doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.
#다음과 같이 glob 모듈을 사용한다.
import glob
print(glob.glob("c:/doit/*.py"))

#Q12. time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
#2018/04/03 17:20:32
#time 모듈의 strftime을 사용하여 다음과 같이 작성한다.
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))   #%Y:년, %m:월, %d:일, %H:시, %M:분, %S:초

#Q13. random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자.
#random 모듈의 randint를 사용하여 다음과 같이 작성한다.
import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)     #1부터 45까지의 난수 발생
    if num not in result:
        result.append(num)
        
print(result)
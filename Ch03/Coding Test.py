#2022.09.21
#Q1. 문자열 바꾸기
#다음과 같은 문자열이 있다.
#a:b:c:d
#문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오
#a#b#c#d
from typing import Type
from unittest import result


a = 'a:b:c:d'
b = a.split(':')
print(b)
c = "#".join(b)
print(c)

#Q2. 딕셔너리 값 추출하기
#다음은 딕셔너리의 a에서 'C'라는 key에 해당하는 value를 출력하는 프로그램이다.
a = {'A' : 90, 'B' : 80}
print(a.get('C', 70))


#Q3. 리스트의 더하기와 extend 함수
#다음과 같은 리스트 a가 있다.
a = [1,2,3]
#리스트 a에 [4,5]를 + 기호를 사용하여 더한 결과는 다음과 같다.
a = [1,2,3]
a = a + [4,5]
print(a)
#리스트 a에 [4,5]를 extend를 사용하여 더한 결과는 다음과 같다.
a = [1,2,3]
a.extend([4,5])
print(a)
#+ 기호를 사용하여 더한 것과 extend한 것의 차이점이 있을까? 있다면 그 차이점을 설명하시오.
#+ 기호를 사용하여 더할 경우 a 리스트의 주소값이 바뀌어 다른 위치에 저장되지만, extend를 사용하면 동일한 주솟값에 저장된다.

#Q4. 리스트 총합 구하기
#다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상 점수의 총합을 구하시오.
a = [20,55,67,82,45,33,90,87,100,25]
sum = 0
for i in a:
    if i >=50:
        sum += i
        
print(sum)

result = 0
while a:
    mark = a.pop()
    if mark >= 50:
        result += mark

print(result)

#Q5. 피보나치 함수
#첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 이전의 두 항을 더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.
#0,1,1,2,3,5,8,13,...
#입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.
def fib(n):
    if n == 0:                  #n이 0일 때는 0을 변환
        return 0
    if n == 1:                  #n이 1일 때는 1을 변환
        return 1
    return fib(n-2) + fib(n-1)  #n이 2 이상일 때는 그 이전의 두 값을 더하여 변환
for i in range(20):
    print(fib(i))

#Q6. 숫자의 총합 구하기
#사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오
#(단 숫자는 콤마로 구분하여 입력한다.)
#65,45,2,3,45,8
user_input = input("숫자를 입력하시오 : ")
numbers = user_input.split(',')
total = 0
for n in numbers:
    total += int(n)             #입력은 문자열이므로 숫자로 변환해야 한다.
print(total)

#Q7. 한 줄 구구단
#사용자로부터 2 ~ 9의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한 줄로 출력하는 프로그램을 작성하시오
#실행 예)
#구구단을 출력할 숫자를 입력하세요 (2~9) : 2
#2 4 6 8 10 12 14 16 18
user_input = input("구구단을 출력할 숫자를 입력하세요 (2~9) : ")
dan = int(user_input)           #입력할 문자열을 숫자로 변환
for i in range(1,10):
    print (i * dan, end= ' ')   #한 줄로 출력하기 위해 줄 바꿈 문자 대신 공백 문자를 마지막에 출력한다.
print()
#Q8. 역순 저장
#다음과 같은 내용의 파일 abc.txt가 있다.
# AAA
# BBB
# CCC
# DDD
# EEE
#이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.
# EEE
# DDD
# CCC
# BBB
# AAA
# f = open('abc.txt','r')
# lines = f.readlines()           #모든 라인을 읽음
# f.close()

# lines.reverse()                 #읽은 라인을 역순으로 정렬

# f = open('abc.txt','r')
# for line in lines:          
#     line = line.strip()         #포함되어 있는 줄 바꿈 문자 제거
#     f.write(line)
#     f.write('\n')               #줄 바꿈 문자 삽입
# f.close()

#Q9. 평균값 구하기
#다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오
# 70
# 60
# 55
# 75
# 95
# 90
# 80
# 80
# 85
# 100
# f = open("sample.txt")
# line = f.readlines()            #sample.txt를 줄 단위로 모두 읽는다.
# f.close()

# total = 0
# for line in lines:
#     score = int(line)           #줄에 적힌 점수를 숫자형으로 변환한다.
#     total += score
# average = total / len(lines)
# f = open("result.txt","w")
# f.write(str(average))
# f.close()
#sample.txt의 점수를 모두 읽기 위해 파일을 열고 readlines를 사용하여 각 줄의 점수 값을 모두 읽어 들여 총 점수를 구한다.
#총 점수를 sample.txt 파일의 라인(Line) 수로 나누어 평균 값을 구한 후 그 결과를 result.txt 파일에 쓴다.
#숫자 값은 result.txt 파일에 바로 쓸 수 없으므로 str 함수를 사용하여 문자열로 변경한 후 파일에 쓴다.

#Q10. 사직연산 계산기
#다음과 같이 동작하는 클래스 Calculator를 작성하시오
class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList
    
    def add(self):
        result = 0
        for num in self.numberList:
            result += num
        return result
    
    def avg(self):
        total = self.add()
        return total / len(self.numberList)
    
cal1 = Calculator([1,2,3,4,5])
print(cal1.add()) 
print(cal1.avg())

cal2 = Calculator([6,7,8,9,0])
print(cal2.add())
print(cal2.avg())

#Q11. 모듈 사용 방법
#C:/doit 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자. 명령 프롬프트 창에서 파이썬 셀을 열어 이 모듈을 import해서 사용할 수 있는 방법을 모두 기술하시오.
#(즉 다음과 같이 import mymod를 수핼할 때 오류가 없어야 한다.)
# import mymod
#파이썬 셀에서 mymod.py 모듈을 인식하기 위해서는 다음과 같은 3가지 방법이 있다.
#1)sys 모듈 사용하기
#다음과 같이 sys.path에 c:\doit 이라는 디렉터리를 출가하면 C:\doit 이라는 디렉터리에 있는 mymod 모듈을 사용할 수 있게 된다.
# import sys
# sys.path.append("C:\doit")
# import mymod

#2)PYTHONPATH 환경 변수 사용하기
#다음처럼 PYTHONPATH 환경 변수에 C:\doit 디렉터리를 지정하면 C:\doit 디렉터리에 있는 mymod 모듈을 사용할 수 있게 된다.
#C:\Users\home>set PYTHONPATH=C:\doit
#C:\Users\home>PYTHON

#3)현재 디렉터리 사용하기
#파이썬 셀을 mymod.py가 있는 위치로 이동하여 실행해도 mymod 모듈을 사용할 수 있게 된다 왜냐하면 sys.path에는 현재 디렉터리인 .이 항상 포함되어 있기 때문이다.
#C:\Users\home>cd C:\doit
#C:\doit>python

#Q12. 오류와 예외 처리
#다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오
result = 0
try:
    [1,2,3,][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
#7이 출력된다.

#1. result의 초깃값은 0이다
#2. try문 안의 [1,2,3][3]이라는 문장 수행 시 IndexError가 발생하여 except IndexError: 구문으로 이동하게 되어 result에 3이 더해져 3이 된다.
#3. 최종적으로 finally 구문이 실행되어 result에 4가 더해져 7이 된다.
#4. print(result)가 수행되어 7이 출력된다.

#Q.13 DashInsert 함수
#DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수 사이에 ~ 를 추가하고, 짝수가 연속되면 *를 추가하는 기능을 갖고 있다. DashInsert 함수를 완성하시오
#입력예시 : 4546793
#출력예시 : 454*67-9-3

data = "4546793"

numbers = list(map(int, data))                  #숫자 문자열을 숫자 리스트로 변경
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:                      #다음 수가 있다면
        is_odd = num % 2 == 1                   #현재 수가 홀수
        is_next_odd = numbers[i + 1] % 2 == 1   #다음 수가 홀수
        if is_odd and is_next_odd:              #연속 홀수
            result.append("-")
        elif not is_odd and is_next_odd:        #연속 짝수
            result.append("*")
            
print("".join(result))

#Q.14 문자열 압축하기
#문자열을 입력받아 같은 문자가 연속으로 반복되는 경우에는 그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.
#입력 예시:aaabbcccccca
#출력 예시:a3b2c6a1
def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1
    if cnt: result += str(cnt)
    return result

print(compress_string("aaabbcccccca"))                

#Q.15 Duplicate Numbers
#0 ~ 9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0 ~ 9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.
#입력예시 : 0123456789 01234 01234567890 6789012345 012322456789
#출력예시 : true false false true false
def chkDupnum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10
print(chkDupnum("0123456789"))      #True 리턴
print(chkDupnum("01234"))           #False 리턴
print(chkDupnum("01234567890"))     #False 리턴
print(chkDupnum("6789012345"))      #True 리턴
print(chkDupnum("012322456789"))    #False 리턴
#리스트 자료형을 사용하여 중복된 값이 있는지 먼저 조사한다. 중복된 값이 있을 경우는 False를 리턴한다.
#최종적으로 중복된 값이 없을 경우 0 ~ 9 까지의 숫자가 모두 사용되었는지 판단하기 위해 입력 문자열의 숫자 값을 저장한 리스트 자료형의 총 개수가 10인지를 조사하여 10일 경우는 True, 아닐 경우는 False를 리턴한다.
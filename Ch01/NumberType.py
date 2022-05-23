#정수형
#정수형(Integer)이란 말 그대로 정수를 뜻하는 자료형을 말한다.
from re import A


a = 123
print(a)
a = -178
print(a)
a = 0
print(a)

#실수형
#파이썬에서 실수형(floating-point)은 소수점이 포함된 숫자를 말한다.
a = 1.2
print(a)
a = -3.45
print(a)

a = 4.24E10
print(a)
a = 4.24e-10
print(a)
#위 방식은 '컴퓨터식 지수 표현 방식'으로 파이썬에서는 4.24e10또는 4.24E10처럼 표한한다(e와 E 둘 중 어느 것을 사용해도 무방하다)
#여기에서 4.24E10은 4.24*10^10, 4.24e-10은 4.24*10^-10을 의미한다.

#8진수와 16진수
#8진수(Octal)를 만들기 위해서는 숫자가 0o 또는 0O(숫자 0 + 알파벳 소문자 o 또는 숫자 0 + 알파벳 대문자 O)로 시작하면 된다
a = 0o177
print(a)

#16진수(Hexadecimal)를 만들기 위해서는 0x로 시작하면 된다.
a = 0x8ff
print(a)
a = 0xABC
print(a)
#8진수나 16진수는 파이썬에서 잘 사용하지 않는 형태의 숫자 자료형이니 간단히 눈으로 익히고 넘어가자

#숫자형을 활용하기 위한 연산자
#사칙연산
a = 3 
b = 4
print(a + b)
print(a * b)
print(a / b)

#x와 y제곱을 나타내는 **연산자
#다음으로 알아야 할 연산자로 **연산자가 있다. 이 연산자는 x ** y 처럼 사용했을 때 x의 y제곱(x^y)값을 돌려준다
a = 3 
b = 4
print(a**b)

#나눗셈 후 나머지를 반환하는 % 연산자
#%는 나눗셈의 나머지 값을 돌려주는 연산자이다.
a = 7
b = 3
print(a % b)
print(b % a)

#나눗셈 후 몫을 반환하는 // 연산자
a = 7 
b = 4
print(a / b)
#이번에는 나눗셈 후 몫을 반환하는 // 연산자를 사용한 경우를 보자
print (a // b)
#1.75에서 몫에 해당하는 정수 값 1만 돌려주는 것을 확인할 수 있다

#나 혼자 코딩
#방금 배운 연산자를 사용해서 숫자 14를 3으로 나누었을 때 몫과 나머지를 확인해 보자
a = 14
b = 3
print(a // b)
print(a % b)

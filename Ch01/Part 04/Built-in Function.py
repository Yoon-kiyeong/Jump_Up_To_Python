#2022.07.28
#내장 함수
#지금까지 파이썬으로 프로그래밍하기 위해 알아야 하는 것들을 대부분 공부헀다.
#이번에는 우리가 만드려는 프로그램이 이미 만들어져 있는지 살펴봐야 한다, 물론 공부를 위해서라면 누군가 만들어 놓은 프로그램을 또 만들 수도 있다.
#하지만 그런 목적이 아니라면 이미 만들어진 것을 다시 만드는 것은 불필요한 행동이다. 그리고 이미 만들어진 프로그램은 테스트 과정을 수 없이 거쳤기 때문에 충분히 검증되어 있다.
#따라서 무엇인가 새로운 프로그램을 만들기 전에는 이미 만들었던 것들, 그 중에서도 특히 파이썬 배포본에 함게 들어 있는 파이썬 라이브러리를 살펴보는 것이 매우 중요하다.

#라이브러리를 살펴보기 전에 파이썬 내장 함수를 먼저 살펴보자. 우리는 이미 몇 가지 내장 함수를 배웠다.
#print,del,type 등이 바로 그것이다. 이러한 내장 함수는 외부 모듈과 달리 import가 필요하지 않기 때문에 아무런 설정 없이 바로 사용할 수 있다.

#abs
#abs(x)는 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수이다.
print(abs(3))
print(abs(-3))
print(abs(-1.2))

#all
#all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
print(all([1,2,3]))
#리스트 자로형 [1,2,3]은 모든 요소가 참이므로 True를 돌려준다.

print(all([1,2,3,0]))
#리스트 자료형[1,2,3,0]중에서 요소 0은 거짓이므로 False를 돌려준다.

#any
#any(x)는 x중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대이다.
print(any([1,2,3,0]))
#리스트 자료형[1,2,3,0] 중에서 1,2,3이 참이므로 True를 돌려준다.
print(any([0,""]))
#리스트 자료형(0,"")의 요소 0과 ""은 모두 거짓이므로 False를 돌려준다.

#chr
#chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
print(chr(97))
print(chr(48))

#dir
#dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다. 다음 예는 리스트와 딕셔너리 객체 관련 함수(메소드)를 보여주는 예이다.
print(dir([1,2,3]))
print(dir({'1':'a'}))

#divmod
#divmod(a,b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
print(divmod(7,3))
#몫을 구하는 연산자//와 나머지를 구하는 % 연산자를 각각 사용한 결과를 비교해 보자.
print(7 // 3)
print(7 % 3)

#enumerate
#enumerate의 뜻은 '열거하다'라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트,튜플,문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려 준다.
for i, name in enumerate(['body','foo','bar']):
    print(i,name)
#순서 값과 함께 body,foo,bar가 순서대로 출력되었다. 즉 위 예제와 같이 enumerate를 for문과 함께 사용하면 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.
#for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려 주는 인덱스 값이 필요할 때 enumerate 함수를 사용하면 매우 유용하다.

#eval
#eval(expression)은 실행 가능한 문자열 (1+2,'hi'+'a' 같은 것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다.
print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4,3)'))
#보통 eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.

#filter
#filter란 무엇인가를 걸러낸다는 뜻으로 filter 함수도 동일한 의미를 가진다.
#filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶여서(걸러 내서) 돌려준다.
def positive(l):
    result = [] # 반환 값이 참인 것만 걸러내서 저장할 변수
    for i in l:
        if i > 0:   #i가 0보다 클 때
            result.append(i)    #리스트에 i 추가
    return result
    
print(positive([1,-3,2,0,-5,6]))
#즉 위에서 만든 positive 함수는 리스트를 입력값으로 받아 각각의 요소를 판별해서 양수 값만 돌려주는 함수이다.
#filter 함수를 사용하면 위 내용을 다음과 같이 간단하게 작성할 수 있다.
def positive(x):
    return x > 0
print(list(filter(positive,[1,-3,2,0,-5,6])))
#여기에서는 두 번째 인수인 리스트의 요소들이 첫 번째 인수인 positive 함수에 입력되었을 때 반환 값이 참인 것만 묶어서 돌려준다. 앞의 예에서는 1,2,6만 양수여서 x > 0 문장이 참이 되므로 [1,2,6]이라는 결괏값을 돌려주게 된다.
#앞의 함수는 lambda를 사용함녀 더욱 간편하게 코드를 작성할 수 있다.
print(list(filter(lambda x:x > 0 ,[1,-3,2,0,-5,6])))

#hex
#hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로  변환하여 돌려주는 함수이다.
print(hex(234))
print(hex(3))

#id
#id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)를 돌려주는 함수이다.
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
#위 예의 3,a,b는 고유 주소 값이 모두 2219296582000이다. 즉 3,a,b가 모두 같은 객체를 가리키고 있다.
#만약 id(4)라고 입력하면 4는 3,a,b와 다른 객체이므로 당연히 다른 고유 주소 값이 출력된다.
print(id(4))

#input
#input([prompt])은 사용자 입력을 받는 함수이다.
#매개변수로 문자열을 주면 다음 세 번째 예에서 볼 수 있듯이 그 문자열은 프롬프트가 된다.
a = input() #사용자가 입력한 정보를 변수 a에 저장
print(a)
b = input("Enter: ")    #Enter: 프롬프트를 띄우고 사용자 입력을 받음
#위에서 입력받은 문자열을 확인해 보면 다음과 같다.
print(b)

#int
#int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.
print(int('3')) #문자열 형태 '3'
print(int(3.4)) #소수점이 있는 숫자 3.4
#int(x,radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.

#2진수로 표현된 11의 10진수 값은 다음과 같이 구한다.
print(int('11',2))

#16진수로 표현된 1A의 10진수 값은 다음과 같이 구한다.
print(int('1A',16))

#isinstance
#isinstance(object,class)는 첫 번째 인수로 인스턴스, 두 번쨰 인수로 클래스 이름을 받는다.
#입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
class Person : pass #아무 기능이 없는 Person 클래스 생성
a = Person()    #Person 클래스의 인스턴스 a 생성
print(isinstance(a,Person)) #a가 Person 클래스의 인스턴스인지 확인
#위 예는 a가 Person 클래스가 만든 인스턴스임을 확인시켜 준다.
b = 3
print(isinstance(b,Person))
#b는 Person 클래스가 만든 인스턴스가 아니므로 False를 돌려준다.

#2022.08.10
#len
#len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.
print(len("python"))
print(len([1,2,3]))
print(len((1,'a')))

#list
#list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
print(list("python"))
print(list((1,2,3)))
#list 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.
a = [1,2,3]
b  = list(a)
print(b)

#map
#map(f,iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력 받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4,])
print(result)
#two_times 함수는 리스트 요소를 입력받아 각 요소에 2를 곱한 결괏값을 돌려준다.

#위 예제는 map 함수를 사용하면 다음처럼 바꿀 수 있다.
def two_times(x): 
    return x * 2
print(list(map(two_times,[1,2,3,4])))
#앞 예제를 해석해 보자. 먼저 리스트의 첫 번째 요소인 1이 two_times 함수의 입력값으로 들어가고 1 * 2의 과정을 거쳐서 2가 된다.
#다음으로 리스트의 두 번째 요소인 2가 2 * 2의 과정을 거쳐 4가 된다. 따라서 결괏값 리스트는 이제 [2,4]가 된다.
#총 4개의 요솟값이 모두 수행되면 마지막으로 [2,4,6,8]을 돌려준다. 이것이 map 함수가 하는 일이다.

#앞의 예는 lambda를 사용하면 다음처럼 간략하게 만들 수 있다.
print(list(map(lambda a:a * 2, [1,2,3,4])))

#max
#max(iterable)은 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수이다.
print(max([1,2,3]))
print(max("python"))

#min
#min(iterable)은 max 함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수이다.
print(min([1,2,3]))
print(min("python"))

#oct
#oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
print(oct(34))
print(oct(12345))

#open
#open(filename,[mode])은 '파일 이름'과 '읽기 방법'을 입력받아 파일 객체를 돌려주는 함수이다.
#읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.
#   모드            설명
#   w           쓰기 모드로 파일 열기
#   r           읽기 모드로 파일 열기
#   a           추가 모드로 파일 열기
#   b           바이너리 모드로 파일 열기
#b는 w,r,a와 함께 사용한다.
# f = open("binary_file","rb")
#위 예제의 rb는 '바이너리 읽기 모드'를 의미한다.

#다음 예의 fread와 fread2는 동일한 방법이다.
# fread = open("read_mode.txt",'r')
# fread2 = open("read_mode.txt")
#즉 모드 부분을 생략하면 기본값으로 읽기 모드 r를 갖게 된다.

#다음은 추가 모드(a)로 파일을 여는 예이다.
# fappend = open("apeend_mode.txt",'a')

#ord
#ord(c)는 문자의 아스키 코드 값을 돌려주즌 함수이다.
#ord 함수는 chr 함수와 반대이다.
print(ord('a'))
print(ord('0'))

#pow
#pow(x,y)는 x의 y 제곱한 결괏값을 돌려주는 함수이다.
print(pow(2,4))
print(pow(3,3))

#range
#range([start,]stop[,stop])는 for문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.

#인수가 하나인 경우
#시작 숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다.
print(list(range(5)))

#인수가 2개인 경우
#입력으로 주어지는 2개의 인수는 시작 숫자와 끝 숫자를 나타낸다. 단 끝 숫자는 해당 범위에 포함되지 않는다는 것에 주의하자.
print(list(range(5,10)))#끝 숫자 10은 포함하지 않음

#인수가 3개인 경우
#세 번째 인수는 숫자 사이의 거리를 말한다.
print(list(range(1,10,2)))  #1부터 9까지, 숫자 사이의 거리는 2
print(list(range(0,-10,-1)))    #0부터 -9까지, 숫자 사이의 거리는 -1

#round
#round(number[,ndigits])함수는 숫자를 입력받아 반올림해 주는 함수이다.
#[,ndigits]는 ndigits가 있을 수도 있고 없을수도 있다는 의미이다.
print(round(4.6))
print(round(4.2))

#다음과 같이 실수 5.678을 소수점 2자리까지만 반올림하여 표시할 수 있다.
print(round(5.678,2))
#round 함수의 두 번째 매개변수는 반올림하여 표시하고 싶은 소수점의 자릴수(ndigits)이다.

#sorted
#sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
print(sorted([3,1,2]))
print(sorted(['a','c','b']))
print(sorted("zero"))
print(sorted((3,2,1)))
#리스트 자료형에도 sort 함수가 있다. 하지만 리스트 자료형의 sort 함수는 리스트 객체 그 자체를 정렬만 할 뿐 정렬된 결과를 돌려주지는 않는다.

#str
#str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수이다.
print(str(3))
print(str('hi'))
print(str('hi'.upper()))

#sum
#sum(iterable)은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.
print(sum([1,2,3]))
print(sum((4,5,6)))

#tuple
#tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다.
#만약 튜플이 입력으로 들어오면 그대로 돌려준다.
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

#type
#type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수이다.
print(type("abc"))
print(type([]))
print(type(()))
print(type(open("test",'w')))

#zip
#zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
#여기서 사용한 *iterable은 반복 가능(iter-able)한 자료형 여러 개를 입력할 수 있다는 의미이다.
print(list(zip([1,2,3,],[4,5,6])))
print(list(zip([1,2,3,],[4,5,6,],[7,8,9])))
print(list(zip("abc","def")))
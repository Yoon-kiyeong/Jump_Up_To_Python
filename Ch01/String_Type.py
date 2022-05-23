#문자열 자료형
#문자열(String)이란 문자, 단어 등으로 구성된 문자들의 집합을 의미한다.

print("Life is too short, You need Python")
print("a")
print("123")
print()
#위 문자열 예문을 보면 모두 큰따옴표("")로 둘러싸여 있다. '123은 숫자인데 왜 문자열이지? 라는 의문이 들 수도 있는데, 따옴표로 둘러싸여 있음녀 모두 문자열이라 보면 된다.

#문자열은 어떻게 만들고 사용할까?
#위 예에서는 문자열을 만들 떄 큰따옴표("")만을 사용했지만 이 외에도 문자열을 만드는 방법은 3가지가 더 있다. 파이썬에서 파이썬에서 문자열을 만드는 방법은 총 4가지 이다.

#1. 큰따옴표(")로 양쪽 둘러싸기
print("Hello World")
print()

#2. 작은 따옴표(')로 양쪽 둘러싸기
print('python is fun')
print()

#3. 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
print("""Life is too short, You need Python""")
print()

#4. 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
print('''Life is too short, You Need python''')
print()

#단순함이 자랑인 파이썬이 문자열을 만드는 방법은 왜 4가지나 있을까? 그 이유에 대해 알아보자

#문자열 안에 작은 따옴표나 큰 따옴표를 포함시키고 싶을 때
#문자열을 만들어 주는 주인공은 작은따옴표(')와 큰따옴표(")이다. 그런데 문자열 안에도 작은따옴표와 큰따옴표가 들어 있어야 할 경우가 있다. 이떄는 좀 더 특별한 기술이 필요하다.

#1. 문자열에 작은따옴표(') 포함시키기
print("Python's favorite food is perl")
print()
#위와 같은 문자열을 food 변수에 저장하고 싶다고 가정하자. 문자열 중 Python's에 작은 따옴표(')가 포함되어 있다.
#이럴 때는 다음과 같이 문자열을 큰따옴표(")로 둘러싸야 한다. 큰따옴표 안에 들어 있는 작은 따옴표는 문자열을 나타내기 위한 기호로 인식되지 않는다.
food = "Python's favorite food is perl"
#food를 입력해서 결과를 확인하자. 변수에 저장된 문자열이 그대로 출력되는 것을 볼 수 있다.
print(food)
print()

#시험 삼아 다음과 같이 큰따옴표가 아닌 작은따옴표로 문자열을 둘러싼 후 다시 실행해보자. 'Python'이 문자열로 인식되어 구문 오류(SyntaxError)가 발생할 것이다.
#food = 'Python's favorite food is perl'
#print(food)

#2. 문자열에 큰따옴표 포함시키기
print("Python is very easy." "he says")
print()
#위와 같이 큰따옴표가 포함된 문자열이라면 어떻게 해야 큰따옴표가 제대로 표현될까?
#다음과 같이 문자열을 작은 따옴표로 둘러싸면 된다.
say = '"Python is very easy." he says.'
print(say)
print()
#이렇게 작은따옴표 안에 사용된 큰따옴표는 ㅁ누자열을 만드는 기호로 인식되지 않는다

#3. 백슬래시(\)를 사용해서 작은따옴표 안에 큰따옴표를 문자열에 포함시키기
food = 'python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say)
print()
#작은따옴표나 큰따옴표를 문자열에 포함시키는 또 다른 방법은 백슬래시를 사용하는 것이다.
#즉 백슬래시를 작은따옴표나 큰따옴표 앞에 삽입하면 백슬래시 뒤의 작은따옴표나 큰따옴표는 문자열을 둘러싸는 기회의 의미가 아니라 문자 ('), (") 그 자체를 뜻하게 된다.

#어떤 방법을 사용해서 문자열 안에 작은따옴표와 큰따옴표를 포함시킬지는 각자의 선택이다.

#여러 줄인 문자열을 변수에 대입하고 싶을 떄
#문자열이 항상 한 줄짜리만 있는 것은 아니다. 다음과 같이 여러 줄의 문자열을 변수에 대입하려면 어떻게 해야 할 까?
#Life is too short
#You need python

#1. 줄을 바꾸는 이스케이프 코드 '\n' 삽입하기
multiline = "Life is too short\nYou need Python"
print(multiline)
#위 예처럼 줄바꿈 문자'\n'을 삽입하는 방법이 있지만 읽기에 불편하고 줄이 길어지는 단점이 있다.

#2. 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 사용하기
#위 1번의 단점을 극복하기 위해 파이썬에서는 다음과 같이 작은 따옴표 3개 또는 큰따옴표 3개를 사용한다
multiline = '''
Life is too Short 
You need Python
'''
print(multiline)

multiline = """
Life is too short
You need Python
"""
print(multiline)
#두 경우 모두 결과는 동일하다. 위 예에서도 확인할 수 있듯이 문자열이 여러 줄인 경우 이스케이프 코드를 쓰는 것보다 따옴표를 연속해서 쓰는 거시 훨씬 깔끔하다.

#문자열 연산하기
#파이썬에서는 문자열을 더하거나 곱할 수 있다. 다른 언어에서는 쉽게 찾아볼 수 없는 재미있는 기능으로, 우리 생각을 그대로 반영해 주는 파이썬만의 장점이라고 할 수 있다.
#문자열을 더하거나 곱하는 방법에 대해 알아보자.

#1. 문자열 더해서 연결하기 (Concatenation)
head= "Python"
tail = "is fun!"
print(head + tail)
print()
#위 소스 코드에서 세번쨰 줄을 보자. "Python"이라는 head 변수와 "is fun!" 이라는 tail 변수를 더한 것이다. 결과는 'Python is fun!'이다. 즉 head와 tail 변수가 +에 의해 합쳐지는 것이다.

#2. 문자열 곱하기
a = 'python'
print(a*2)
print()
#위 소스코드에서 *의 의미는 우리가 일반적으로 사용하는 숫자 곱하기의 의미와는 다르다.
#위 소스코드에서 a * 2 문장은 a를 두 번 반복하라는 뜻이다. 즉 *는 문자열의 반복을 뜻하는 의미로 사용되었다. 굳이 코드의 의미를 설명할 필요가 없을 정도로 직관적이다

#3. 문자열 곱하기 응용
#문자열 곱하기를 좀 더 응용해 보자.
print("=" * 50)
print("My Program")
print("=" * 50)
print()

#4. 문자열 길이 구하기
#문자열의 길이는 다음과 같이 len 함수를 사용하면 구할 수 있다. len 함수는 print 함수처럼 파이썬의 기본 내장 함수로 별 다른 설정 없이 바로 사용할 수 있다.
a = "Life is Too short"
print(len(a))
print()

#나 혼자 코딩
#'You need python' 문장를 문자열로 만들고 길이를 구해 보자
a = 'You need python'
print(a)
print(len(a))
print()


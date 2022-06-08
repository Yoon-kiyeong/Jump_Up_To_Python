#2022.05.31
#리스트는 어떻게 만들고 사용할 까?
#리스트를 사용하면 1,3,5,7,9 숫자 모음을 다음과 같이 사용할 수 있다.
odd = [1,3,5,7,9]
#리스트를 만들 때는 위에서 보는 것과 같이 대활고([])로 감싸 주고 요솟값은 쉼표(,)로 구분해 준다
#리스트 명 = [요소1, 요소2, 요소3, 요소4, 요소5, ...]

#여러가지 리스트의 생김새를 살펴보면 다음과 같다.
a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1,2,'Life','is']
e = [1,2, ['Life', 'is']]
#리스트 a처럼 아무것도 포함하지 않아 비어 있는 리스트([])일 수도 있고 b처럼 숫자를 요솟값으로 가질 수도 있고 c처럼 ㅁ누자열을 요솟값으로 가질 수도 있다.
# 또한 d처럼 숫자와 문자열을 함께 요솟값으로 가질 수도 있으며 e처럼 리스트 자체를 요솟값으로 가질 수도 있도. 즉 리스트 안에는 어떠한 자료형도 포함시킬 수 있다.

#리스트의 인덱싱과 슬라이싱
#리스트도 문자열처럼 인덱싱과 슬라이싱이 가능하다.

#리스트의 인덱싱
#리스트 역시 문자열처럼 인덱싱을 적용할 수 있다.
a = [1,2,3,]
print(a)
#a[0]은 리스트 a의 첫 번째 요솟값을 말한다.
print(a[0])
#다음 예는 리스트의 첫 번째 요소인 a[0]과 세 번째 요소인 a[2]의 값을 더한 것이다.
print(a[0] + a[2])
#문자열을 공부할 때 이미 살펴보았지만 파이썬은 숫자를 0부터 세기 때문에 a[1]이 리스트 a의 첫번째 요소가 아니라 a[0]이 첫번째 요소임을 명심하자.
# a[-1]은 문자열에서와 마찬가지로 리스트 a의 마지막 요솟값을 말한다.
print(a[-1])
print()

#이번에는 다음 예처럼 리스트 a를 숫자 1,2,3과 또 다른 리스트인 ['a','b','c']를 포함하도록 만들어 보자
a = [1,2,3,['a','b','c']]
print(a)

#다음 예를 따라해 보자
print(a[0])
print(a[-1])
print(a[3])
#예상한 대로 a[-1]은 마지막 요솟값 ['a','b','c']를 나타낸다. a[3]은 리스트 a의 네 번째 요소를 나타내기 때문에 마지막 요소를 나타내는 a[-1]과 동일한 결괏값을 보여 준다.
#그렇다면 여기에서 리스트 a에 포함된 ['a','b','c']리스트에서 'a' 값을 인덱싱을 사요해 끄집어 낼 수 있는 방법은 없을까? 다음 예를 보자
print(a[-1][0])
#위와 같이 하면 'a'를 끄집어 낼 수 있다. a[-1]이 ['a','b','c']리스트라는 것은 이미 말했다. 바로 이 리스트에서 첫 번째 요소를 불러오기 위해 [0]을 붙여 준 것이다.

#다음 예도 마찬가지 경우이므로 어렵지 않게 이해 될 것이다.
print(a[-1][1])
print(a[-1][2])
print()

#삼중 리스트에서 인덱싱 하기
a = [1, 2, ['a', 'b', ['Life','is']]]
#리스트 안에 ['a', 'b', ['Life','is']] 리스트가 포함되어 있고, 그 리스트 안에 다시 ['Life', 'is'] 리스트가 포함되어 있다. 삼중 구조의 리스트이다.
#이 경우 'Life' 문자열만 끄집어 내려면 다음과 같이 해야 한다.
print(a[2][2][0])
#위 예는 리스트 a의 세 번째 요소인 리스트 ['a', 'b', ['Life', 'is]]에서 세 번째 요소인 ['Life', 'is']의 첫 번째 요소를 나타낸다.
#이렇듯 리스트를 삼중으로 중첩해서 쓰면 혼란스럽기 때문에 자주 사용하지는 않지만 알아두는 것이 좋다.

#리스트의 슬라이싱
#문자열과 마찬가지로 리스트에서도 슬라이싱 기법을 적용할 수 있다. 슬라이싱은 '나눈다'는 뜻이라고 했다.
a = [1,2,3,4,5]
print(a[0:2])
# 앞의 예를 문자열에서 슬라이싱했던 것과 비교해 보자.
a = "12345"
print(a[0:2])
#2가지가 완전하게 동일하게 사용되었다. 문자열에서 했던 것과 사용법이 완전히 동일하다

a = [1,2,3,4,5]
b = a[:2] #처음부터 a[1]까지
c = a[2:] #a[2]부터 마지막까지
print(b)
print(c)
#b 변수는 리스트 a의 첫 번째 요소부터 두 번째 요소인 a[1]까지 나타내는 리스트이다. 물론 a[2]값인 3은 포함되지 않는다. c라는 변수는 리스트 a의 세 번째 요소부터 끝까지 나타내는 리스트이다.

#나 혼자 코딩
#a = [1,2,3,4,5]리스트에서 슬라이싱 기법을 사용하여 리스트 [2,3]를 만들어 보자
a = [1,2,3,4,5]
result = a[1:3]
print(result)

print()

#2022.06.08
# 점프 투 파이썬 중첩된 리스트에서 슬라이싱 하기
# 리스트가 포함된 중첩 리스트 역시 슬라이싱 방법은 똑같이 적용된다.
a = [1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])
print()
# 위에서 a[3]은 ['a','b','c']를 나타낸다. 따라서 a[3][:2]는 ['a','b','c']의 첫 번째 요소부터 세 번째 요소 직전까지의 값, 즉 ['a','b']를 나타내는 리스트가 된다.
print()
# 리스트 연산하기
# 리스트 역시 + 기호를 사용해서 더할 수 있고, * 기호를 사용해서 반복할 수 있다.
#1. 리스트 더하기(+)
a = [1,2,3]
b = [4,5,6]
print(a+b)
# 리스트 사이에서 + 기호는 2개의 리스트를 합치는 기능을 한다. 문자열에서 "abc" + "def" = "abcdef"가 되는 것과 같은 이치이다.
#2. 리스트 반복하기(*)
a = [1,2,3]
print(a * 3)
# 위에서 볼 수 있듯이 [1,2,3] 리스트가 세 번 반복되어 새로운 리스트를 만들어 낸다. 문자열에서 "abc" * 3 = "abcabcabc"가 되는 것과 같은 이치이다.
# 3. 리스트 길이 구하기
#리스트 길이를 구하기 위해서는 len 함수를 사용해야 한다.
a = [1,2,3]
print(len(a)) 
#len 함수는 문자열, 리스트 외에 튜블과 딕셔너리에도 사용할 수 있는 함수이다.
print()

#점프 투 파이썬 초보자가 실수하기 쉬운 리스트 연산 오류
#다음 소스 코드를 입력했을 때 결괏값은 어떻게 나올까?
# a = [1,2,3]
# print(a[2] + "hi")
#a[2]의 값인 3과 문자열 hi가 더해져서 3hi가 출력될 것이라고 생각할 수 있다.
#하지만 다음 결과를 보자. 형 오류(TypeError)가 발생했다. 오류의 원인은 무엇일까?
#Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#TypeError : unsupported operand type(s) for +: 'int and 'str'
#a[2]에 저장된 값은 3이라는 정수인데 "hi"는 문자열이다. 정수와 문자열은 당연히 서로 더할 수 없기 때문에 형 오류가 발생한 것이다.
#만약 숫자와 문자열을 더해서 '3hi'처럼 만들고 싶다면 숫자 3을 문자 '3'으로 바꾸어 주어야 한다.

#다음과 같이 할 수 있다.
#str(a[2]) + "hi"
#str함수는 ㅈ어수나 실수를 문자열의 형태로 바꾸어 주는 파이썬의 내장 함수이다.
print()

#리스트의 수정과 삭제
#리스트는 값을 수정하거나 삭제할 수가 있다.
#리스트에서 값 수정하기
a = [1,2,3]
a[2] = 4
print(a)
#a[2]의 요솟값 3이 4로 바뀌었다.
#del 함수 사용해 리스트 요소 삭제하기
a = [1,2,3]
del a[1]
print(a)
#del a[x]는 x번째 요솟값을 삭제한다. 여기에서는 a리스트에서 a[1]을 삭제하는 방법을 보여준다.
#del 함수는 파이썬이 자체적으로 가지고 있는 삭제 함수이며 다음과 같이 사용된다.
#del 객체 -> 객체란 파이썬에서 사용되는 모든 자료형을 말한다.

#다음처럼 슬라이싱 기법을 사용하여 리스트의 요소 여러 개를 한꺼번에 삭제할 수도 있다.
a = [1,2,3,4,5]
del a[2:]
print(a)
#a[2:]에 해당하는 리스트의 요소들이 삭제되었다.
#리스트의 요소를 삭제하는 방법에는 2가지가 더 있다. 그것은 리스트의 remove와 pop 함수를 사용하는 방법이다.
print()

#리스트 관련 함수
#문자열과 마찬가지로 리스트 변수 이름 뒤에 '.'를 붙여서 여러 가지 리스트 관련 함수를 사용할 수 있다. 유용하게 사용되는 리스트 관련 함수 몇 가지에 대해서만 알아보기로 하자

#리스트에 요소 추가(append)
#append를 사전에서 검색하면 '덧붙이다, 첨부하다'라는 뜻이 있다. 이 뜻을 안다면 바로 이해가 될 것이다. append(x)는 리스트의 맨 마지막에 x를 추가하는 함수이다.
a = [1,2,3]
a.append(4)
print(a)
#리스트 안에는 어떤 자료형도 추가할 수 있다.
print()
#다음 예는 리스트에 다시 리스트를 추가한 결과이다.
a.append([5,6])
print(a)

#리스트 정렬(sort)
#sort함수는 리스트의 요소를 순서대로 정렬해 준다.
a = [1,2,3,4]
a.sort()
print(a)

#문자 역시 알파벳 순서로 정렬할 수 있다.
a = ['a','c','b']
a.sort()
print(a)

#리스트 뒤집기(reverse)
#reverse 함수는 리스트를 역순으로 뒤집어 준다. 이때 리스트 요소들을 순서대로 정렬한 다음 다시 역순으로 정렬하는 것이 아니라 그저 현재의 리스트를 그대로 거꾸로 뒤집는다.
a = ['a','c','b']
a.reverse()
print(a)

#위치 반환(index)
#index(X) 함수는 리스트에 x값이 있으면 x의 위치 값을 돌려준다.
a = [1,2,3]
print(a.index(3))
print(a.index(1))
#위 예에서 리스트 a에 있는 숫자 3의 위치는 a[2]이므로 2를 돌려주고, 숫자 1의 위치는 a[0]이므로 0을 돌려준다.
#다음 예에서 값 0은 a 리스트에 존재하지 않기 때문에 값 오류(ValueError)가 발생한다.
# a.index(0)

#리스트에 요소 삽입(insert)
#insert(a,b)는 리스트의 a번째 위치에 b를 삽입하는 함수이다. 파이썬에서는 숫자를 0부터 샌다는 것을 기억할 것
a = [1,2,3]
a.insert(0,4)
print(a)
#위 예에서는 0번째 자리, 즉 첫 번째 요소(a[0]) 위치에 값 4를 삽입하라는 뜻이다.
a.insert(3,5) #a[3] 위치에 5 삽입
print(a)
#위 예는 리스트 a의 a[3], 즉 네 번째 요소 위치에 값 5를 삽입하라는 뜻이다.

#리스트 요소 제거(remove)
#remove(x)는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수이다.
a = [1,2,3,1,2,3]
a.remove(3)
print(a)
#a가 3이라는 값을 2개 가지고 있을 경우 첫 번째 3만 제거되는 것을 알 수 있다.
a.remove(3)
print(a)
#remove(3)을 한 번 더 실행하면 다시 3이 삭제된다.

#리스트 요소 끄집어내기(pop)
#pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
a = [1,2,3]
print(a.pop(1))
print(a)
#a.pop(1)은 a[1]의 값을 끄집어낸다. 다시 a를 출력해 보면 끄집어낸 값이 삭제된 것을 확인할 수 있다.

#리스트에 포함된 요소 x의 개수 새기(count)
#count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 돌려주는 함수이다.
a = [1,2,3,1]
print(a.count(1))
#1이라는 값이 리스트 a에 들어 있으므로 2를 돌려준다.

#리스트 확장(extend)
#extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다.
a = [1,2,3]
a.extend([4,5])
print(a)
b = [6,7]
a.extend(b)
print(a)
#a.extend([4,5])는 a += [4,5]와 동일하다
# +=는 계산한 값을 원래 값에 할당한다고 해서 할당 연산자라고 부른다. 즉 i += 1은 i = i + 1과 같다.
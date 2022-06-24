#2022.06.16
#Practice
#Q1. 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해보자.
#국어 : 80
#영어 : 75
#수학 : 55
a = 80
b = 75
c = 55
print(a+b+c/3)
print()

#Q2.자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해보자.
a = 13
print(a % 2)
if a % 2 == 0:
    print(True)
else: 
    print(False)
print()

#Q3. 홍길동 씨의 주민번호는 831120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해보자
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
print()

#Q4. 주민등록번호 뒷자리의 맨 첫 번쨰 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해보자.
pin = "881120-1068234"
print(pin[7])
print()

#Q5. 다음과 같은 문자열 a:b:c:d가 있다. replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해보자
a = "a:b:c:d"
b = a.replace(":","#")
print(b)
print()

#Q6. [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어 보자.
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)
print()

#Q7. ['Life','is','too','short]리스트를 Life is too short 문자열로 만들어 출력해 보자.
a =['Life','is','too','short']
result = " ".join(a)
print(result)
print()

#Q8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
a = (1,2,3)
a = a + (4,)
print(a)
print()

#Q9. 다음과 같은 딕셔너리 a가 있다.
a = dict()
print(a)
#다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
#1.a['name'] = 'python'
#2.a[('a',)] = 'python'
#3.a[[1]] = 'python'
#4.a[250] = 'python'
#답 : 3
#오류가 발생하는 이유는 딕셔너리의 키로는 변하는(mutable) 값을 사용할 수 없기 때문이다. 위 예에서 키로 사용된 [1]은 리스트이므로 변하는 값이다. 다른 예에서 키로 사욛된 문자열, 튜플, 숫자는 변하지 않는(immutable) 값이므로
#딕셔너리의 키로 사용이 가능하다.
print()

#Q10. 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자/
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)
print()

#Q11. a 리스트에서 중복 숫자를 제거해 보자.
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)
print()

#Q12. 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a,b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까?
#그리고 이런 결과가 나오는 이유에 대해 설명해 보자.
a = b = [1,2,3]
a[1] = 4
print(b)
#결과는 [1,4,3]으로 출력된다.
#a와 b 변수는 동일한 리스트 객체를 갖고 있기 때문에 두 번째 요솟값을 변경하면 똑같이 4로 변경이 된다.
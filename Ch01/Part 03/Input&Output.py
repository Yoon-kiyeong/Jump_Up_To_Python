#사용자 입력과 출력
#우리들이 사용하는 대부분의 완성된 프로그램은 사용자 입력에 따라 그에 맞는 출력을 내보낸다.
#대표적인 예로 게시판에 글을 작성한 후 '확인' 버튼을 눌러야만(입력) 우리가 작성한 글이 게시판에 올라가는(출력) 것을 들 수 있다.
#우리는 이미 함수 부분에서 입력과 출력이 어떤 의미를 가지는지 알아보았다. 지금부터는 좀 더 다양하게 사용자의 입력을 받는 방법과 출력하는 방법을 알아보자.

#사용자 입력
#사용자가 입력한 값을 어떤 변수에 대입하고 싶을 때는 어떻게 해야 할까?

#input의 사용
a = input()
#Life is too short, you need python #사용자가 입력한 문장을 a에 대입
a
#input은 입력되는 모든 것을 문자열로 취급한다.

#프롬프트 값을 띄워서 사용자 입력받기
#사용자에게 입력받을 때 '숫자를 입력하세요' 라든지 '이름을 입력하세요'라는 안내 문구 또는 질문이 나오도록 하고 싶을 때가 있다.
#그럴 때는 input()의 괄호 안에 짊누을 입력하여 프롬프트를 띄워줌녀 된다.
input("질문 내용")

#다음 예를 직접 입력해 보자
number = input("숫자를 입력하세요: ")
print(number)
#위와 같은 질문을 볼 수 있을 것이다
#숫자를 입력하라는 프롬프트에 3을 입력하면 변수 number에 3이 대입된다. print(number)로 출력해서 제대로 입력되었는지 확인해 보자.

#print 자세히 알기
#지금껏 print문이 수행해 온 일은 우리가 입력한 자료형을 출력하는 것이었다. print의 사용에는 다음과 같다
a = 123
print(a) #숫자 출력하기
a = "python"
print(a) #문자열 출력하기
a = [1,2,3]
print(a) #리스트 출력하기

#이제 print문으로 할 수 있는 일에 대해서 조금 더 자세하게 알아보자.

#큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("Life" "is" "too short") #1
print("Life"+"is"+"too short") #2
#위 예에서 1과 2는 완전히 동일한 결괏값을 출력한다. 즉 따옴표로 둘러싸인 문자열을 연속해서 쓰면 + 연산을 한 것과 같다.

#문자열 띄어쓰기는 콤마로 한다.
print("Life","is","too short")
#콤마(.)를 사용하면 문자열 사이에 띄어쓰기를 할 수 있다.

#한 줄에 결괏값 출력하기
#for문을 배울 때 만들었던 구구단 프로그램에서 보았듯이 한 줄에 결괏값을 계속 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정해야 한다.
for i in range(10):
    print(i,end=' ')
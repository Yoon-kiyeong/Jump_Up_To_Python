#while문
#while문의 기본 구조
#반복해서 문장을 수행해야 할 경우 while문을 사용한다. 그래서 while문을 반복문이라고도 부른다.
#다음은 while문의 기본 구조이다.
#while 조건문:
#   수행할 문장1
#   수행할 문장2
#   수행할 문장3
#   수행할 문장4
#   수행할 문장5
#   ...

#while문은 조건문이 참인 동안에 while문 아래의 문장이 반복해서 수행된다.

#'열 번 찍어 안 넘어가는 나무 없다'는 속담을 파이썬 프로그램으로 만든다면 다음과 같이 될 것이다.
treeHit = 0 #나무를 찍은 횟수 
while treeHit < 10: #나무를 찍은 횟수가 10보다 작은 동안 반복
    treeHit = treeHit + 1 #나무를 찍은 횟수 1씩 증가
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10: #나무를 열 번 찍으면
        print("나무 넘어갑니다")
print()

#위 예에서 while문의 조건문은 treeHit < 10이다. 즉 treeHit가 10보다 작은 동안에 while문 안의 문장을 계속 수행한다. while문 안의 문장을 보면 제일 먼저 treeHit = treeHit + 1로 treeHit값이 계속 1씩 증가한다.
#그리고 나무를 treeHit번만큼 찍었음을 알리는 문장을 출력하고 treeHit가 10이 되면 '나무 넘어갑니다'라는 문장을 출력한다. 그러고 나면 treeHit < 10 조건문이 거짓이 되므로 while문을 빠져나가게 된다.

#while문 만들기
#이번에는 여러 가지 선택지 중 하나를 선택해서 입력받는 예제를 만들어 보자. 먼저 다음과 같이 여러 줄짜리 문자열을 입력한다.
prompt = """
1. Add
2. Del
3. List
4. Quit
...
Enter number: """

#이어서 number 변수에 0을 먼저 대입한다. 이렇게 변수를 먼저 설정해 놓지 않으면 다음에 나올 while문의 조건문인 number != 4에서 변수가 존재하지 않는다는 오류가 발생한다.
number = 0 #번호를 입력받을 변수
while number != 4: #입력받은 번호가 4가 아닌 동안 반복한다.
    print(prompt)
    number = int(input())

#while문을 보면 number가 4가 아닌 동안 prompt를 출력하고 사용자로부터 번호를 입력받는다. 다음 결과 화면처럼 사용자가 값 4를 입력하지 않으면 계속해서 prompt를 출력한다.
#여기에서 number = int(input())는 사용자의 숫자 입력을 받아들이는 것이라고만 알아두자.

#Enter number:
#1 <- 1 입력

#1.Add
#2.Del
#3.List
#4.Quit
#4를 입력하디 않으면 계속해서 prompt 출력

#4를 입력하면 조건문이 거짓이 되어 while문을 빠져나가게 된다.
#Enter number:
#4 <- 4 입력
print()
#while문 강제로 빠져나가기
#while문은 조건문이 참인 동안 계속해서 while문 안의 내용을 반복적으로 수행한다. 하지만 강제로 while문을 빠져나가고 싶을 때가 있다.
#예를 들어 커피 자판기를 생각해보자. 자판기 안에 커피가 충분히 있을 때는 동전을 넣으면 커피가 나온다. 그런데 자판기가 제대로 작동하려면 커피가 얼마나 남았는지 항상 검사해야 한다.
#만약 커피가 떨어졌담녀 판매를 중단하고 '판매 중지' 문구를 사용자에게 보여주어야 한다. 이렇게 판매를 강제로 멈추게 하는 것이 바로 break문이다.

#다음 예는 커피 자판기 이야기를 파이썬 프로그램으로 표현해 본 것이다.
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다."% coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
print()
#money가 300으로 고정되어 있으므로 while money:에서 조건문ㅇ니 money는 0이 아니기 때문에 항상 참이다. 따라서 무한히 반복되는 무한 루프를 돌게 된다. 그리고 while문의 내용을 한 번 수행할 때마다
#coffee = coffee -1에 의해서 coffee의 개수가 1개씩 줄어든다. 만약 coffee가 0이 되면 if coffee == 0: 문장에서 coffee == 0:이 참이 되므로 if문 다음 문장 "커피가 다 떨어졌습니다. 판매를 중지합니다."가 수행되고
#break문이 호출되어 while문을 빠져나가게 된다.

#하지만 실제 자판기는 위 예처럼 작동하지 않을 것이다. 다음은 자판기의 실제 작동 과정을 비슷하게 만들어본 예이다.
coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다."% (money - 300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
print()

#While문의 맨 처음으로 돌아가기
#while문 안의 문장을 수행할 때 입력 조건을 검사해서 조건에 맞지 않으면 while문을 빠져나간다. 그런데 프로그래밍을 하다 보면 while문을 빠져나가지 않고 while문의 맨 처음(조건문)으로 다시 돌아가게 만들고 싶은 경우가 생기게 된다.
#이때 사용하는 것이 바로 continue문이다.
#1부터 10까지의 숫자 중에서 홀수만 출력하는 것을 while문을 사용해서 작성한다고 생각해보자. 어떤 방법이 좋을까?
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue #a를 2로 나누었을 때 나머지가 0이면 맨 처음으로 돌아간다.
    print(a)
print()

#위 예는 1부터 10까지의 숫자 중 홀수만 출력하는 예이다. a가 10보다 작은 동안 a는 1만큼씩 계속 증가한다. if a % 2 == 0(a를 2로 나누었을 때 나머지가 0인 경우)이 참이 되는 경우는 a가 짝수일 떄이다.
#즉 a가 짝수이면 continue 문장을 수행한다. 이 continue문은 while문의 맨 처음(조건문:a<10)으로 돌아가게 하는 명령어이다. 따라서 위 예에서 a가 짝수이면 print(a)는 수행되지 않을 것이다.

#나 혼자 코딩! 1부터 10까지의 숫자 중에서 3의 배수를 뺀 나머지 값을 출력해 보자
a = 0
while a < 10:
    a = a + 1
    if a % 3 == 0: continue
    print(a)
print()

#무한 루프
#이번에는 무한 루프(Loop)에 대해 알아보자. 무한 루프란 무한히 반복한다는 의미이다.
#우리가 사용하는 일반 프로그램 중에서 무한 로프 개념을 사용하지 않는 프로그램은 거의 없다. 그만큼 자주 사용한다는 뜻이다.

#파이썬에서 무한 루프는 while문으로 구현할 수 있다. 다음은 무한 루프의 기본 형태이다.
#while True:
#   수행할 문장1
#   수행할 문장2
#   ...
#while문의 조건문이 True이므로 항상 참이 된다. 따라서 while문 안에 있는 문장들은 무한하게 수행될 것이다.

#다음은 무한루프의 예이다.
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
print()
#위 문장은 영원히 출력된다. 하지만 이 예처럼 아무 의미 없이 무한 루프를 돌리는 경우는 거의 없을 것이다. Ctrl+C를 눌러 빠져나가자.
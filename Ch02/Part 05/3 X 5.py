#3과 5의 배수 합하기
#자, 다음 문제를 어떻게 풀면 좋을지 생각해 보자.
#10 미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
#1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

#입력받는 값은? 1부터 999까지 (1000미만의 자연수)
#출력하는 값은? 3의 배수와 5의 배수의 총합
#생각해 볼 것은? 하나. 3의 배수와 5의 배수는 어떻게 찾지?
#둘. 3의 배수와 5의 배수가 겹칠 때는 어떻게 하지?

#이 문제를 풀기 위한 중요 포인트는 두 가지이다. 한 가지는 1000 미만의 자연수를 구하는 방법이고 또 다른 한 가지는 3과 5의 배수를 구하는 것이다.
#이 두 가지만 해결되면 문제는 쉽게 해결될 것으로 보인다.

#1. 먼저 1000 미만의 자연수는 어떻게 구할 수 있을지 생각해 보자.
#여러 가지 방법이 떠오를 것이다.
#다음과 같이 변수에 초깃값 1을 준 후 루프를 돌리며 1씩 증가시켜서 999까지 진행하는 방법이 가장 일반적인 방법일 것이다.
n = 1
while n < 1000:
    print(n)
    n += 1
#또는 다음과 같이 좀 더 파이썬다운 range 함수를 사용할 수도 있다.
for n in range(1,1000):
    print(n)
#두 가지 예 모두 실행하면 1부터 999까지 출력하는 것을 호가인할 수 있다.

#2. 1000가지의 자연수를 차례로 구하는 방법을 알았으니 3과 5의 배수를 구하는 방법을 알아보자. 1000 미만의 자연수 중 3의 배수는 다음과 같이 증가할 것이다.
#3,6,9,12,15,18,...,999
#그렇다면 12부터 1000까지 수가 진행되는 동안 그 수가 3의 배수인지는 어떻게 알 수 있을까?
#1부터 1000까지의 수 중 3으로 나누었을 떄 나누어 떨어지는 경우, 즉 3으로 나누었을 때 나머지가 0인 경우가 바로 3의 배수이다. 따라서 다음과 같이 % 연산자를 사용하면 3의 배수를 쉽게 찾을 수 있다.
for n in range(1,1000):
    if n % 3 == 0:
        print(n)
#그렇다면 5의 배수는 n % 5가 0이 되는 수로 구할 수 있을 것이다.

#3. 이러한 내용을 바탕으로 만든 최종 풀이는 다음과 같다.
result = 0
for n in range(1, 1000):    #1부터 999까지 n에 대입하며 반복
    if n % 3 == 0 or n % 5 == 0:    #n을 3으로 나눈 나머지가 0이거나 n을 5로 나눈 나머지가 0이라면
        result += n
print(result)
#3과 5의 배수에 해당하는 수를 result 변수에 계속해서 더해 주었다.

#이 문제에는 한 가지 함정이 있는데 3으로도 5로도 나누어지는 15와 같은 수를 이중으로 더해서는 안 된다는 점이다. 따라서 15와 같이 3의 배수도 되고 5의 배수도 도는 값이 이중으로 더해지지 않기 위해 or 연산자를 사용하였다.
#다음 예는 15와 같은 수를 이중으로 더하여 잘못된 결과를 출력하는 잘못된 풀이이다.
#[잘못된 풀이]
result = 0
for n in range(1, 1000):
    if n % 3 == 0:
        result += n
    if n % 5 == 0:
        result += n
print(result)
#Q1 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자
def is_odd(number):
    if number / 2 == 1: #2로 나누었을 때 나머지가 1이면 홀수이다.
        return True
    else:
        return False
print(is_odd(5))
#답: number / 2 == 1 :

#Q2 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1,2)) #1.5 출력
print(avg_numbers(1,2,3,4,5)) # 3.0 출력

#Q3 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다." % total)
#이 프로그램을 수행해 보자
#첫번째 숫자를 입력하세요:3
#두번째 숫자를 입력하세요:6
#두 수의 합은 36 입니다.
#3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.

#답: int함수를 사용해 문자열이 아닌 숫자로 변형하여 오류를 수정

#Q4 다음 중 출력 결과가 다른 것 한개를 골라 보자
print("you" "need" "python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python "]))

#답: 3, 콤마를 사용하면 띄어 쓰기가 되기 때문이다.

#Q5 다음은 "test.txt"라는 파일에 "Life is too short"문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# f1 = open("test.txt",'w')
# f1.write("Life is too short")

# f2 = open("test.txt",'r')
# print(f2.close())
#이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

#답: 문제의 예와 같이 파일을 닫지 않은 상태에서 다시 열면 파일에 저장한 데이터를 읽을 수 없다. 따라서 열린 파일 객체를 close로 닫아준 후 다시 열어서 파일의 내용을 읽어야 한다.
f1 = open("test.txt",'w')
f1.write("Life is too short!")
f1.close()

f2 = open("test.txt",'r')
print(f2.read())
f2.close()

#또는 다음과 같이 close를 명시적으로 할 필요가 없는 with구문을 사용한다.
with open("test.txt",'w') as f1:
    f1.write("Life is too short!")
with open("test.txt",'r') as f2:
    print(f2.read())
    
#Q6 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
user_input = input("저장할 내용을 입력하세요")
f = open('test.txt','a')    #내용을 추가하기 위해서 'a'를 사용
f.write(user_input)
f.write("\n")               #입력된 내용을 준 단위로 구분하기 위해 줄 바꿈 문자 삽입
f.close()

#Q7 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 'java'라는 문자열을 'python'으로 바꾸어서 저장해 보자.
#Life is too short
#you need Java
f = open('test.txt','r')
body = f.read()     #test.txt 파일의 내용을 body 변수에 저장
f.close()

body = body.replace('java','python') #body 문자열에서 "java"를 "python"으로 변경

f = open('test.txt','w')        #파일을 쓰기 모드로 다시 실행
f.write(body)
f.close()

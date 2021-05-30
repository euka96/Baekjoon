# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
# 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
# 첫째 줄에 상수의 대답을 출력한다.

A, B = map(int, input().split())
a = [A % 10, A // 10 % 10, A // 100]
b = [B % 10, B // 10 % 10, B // 100]
if (a[0] * 100 + a[1] * 10 + a[2]) > (b[0] * 100 + b[1] * 10 + b[2]) : print(a[0] * 100 + a[1] * 10 + a[2])
elif (a[0] * 100 + a[1] * 10 + a[2]) < (b[0] * 100 + b[1] * 10 + b[2]) : print(b[0] * 100 + b[1] * 10 + b[2])
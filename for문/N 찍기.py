# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

N = int(input())
ntimes = range(1, N + 1)
for i in ntimes:
	print(i)
	i += 1

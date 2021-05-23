# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 A+B를 출력한다.

# EOF | End of File | 파일 입출력 시 입력이 끝날 때 까지 읽어들이는 readline)_과 같은 내장 함수 명령을 쓸 떄 사용
# try로 돌다가 오류나 예외 발생 시 except로 탈출

while True:
	try:
		A, B = map(int, input().split())
		print(A + B)
	except:
		break

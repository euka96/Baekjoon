# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

word = input()
az = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
time = 0
for i in word :
    if az[0] <= i <= az[2] :
        time += 3
    elif az[3] <= i <= az[5] :
        time += 4
    elif az[6] <= i <= az[8] :
        time += 5
    elif az[9] <= i <= az[11] :
        time += 6
    elif az[12] <= i <= az[14] :
        time += 7
    elif az[15] <= i <= az[18] :
        time += 8
    elif az[19] <= i <= az[21] :
        time += 9
    else :
        time += 10
print(time)
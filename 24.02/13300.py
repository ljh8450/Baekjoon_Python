from sys import stdin
answer = 0
n, k = map(int, stdin.readline().split())
data = [[0, 0]] * n
for i in range(n): #학생들 입력받기.
    data[i] = list(map(int, stdin.readline().split()))

data.sort(key=lambda x: (x[1], x[0])) #학년순 정렬 후, 성별 순 정렬.

th = 1#학년 확인
g = 0#성별 확인
temp = 1#k가 넘으면 초기화

for i in range(len(data)-1):
    if temp < k and g == data[i+1][0] and th == data[i+1][1]:#방에 공간 있으면 체커만 올리기
        temp += 1
    else:#방에 공간이 없으면
        if g != data[i+1][0]:#0 -> 1 성별 바꾸고 answer 늘리기
            answer += 1
            g = 1
        elif th != data[i+1][1]:#학년 높아지면 성별 자동으로 바뀜.
            answer += 1
            th += 1
            g = 0
        elif temp >= k:
            answer += 1
        temp = 1
        print('change', i)

print(answer)
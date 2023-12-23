from sys import stdin

t = int(stdin.readline())

def checker(m, n, x, y):
    bet_mn = abs(m-n)
    bet_xy = abs(x-y)
    big_num = max(m, n)
    list_bet = []
    while True:
        big_num -= bet_mn
        if bet_mn in list_bet or big_num in list_bet:
            return False
        list_bet.append(big_num)
        list_bet.append(bet_mn)
        if bet_mn == bet_xy or big_num == bet_xy:
            return True
        print(list_bet)
        big_num += bet_mn

for _ in range(t):
    a, b = 0, 0
    m, n, x, y = map(int, stdin.readline().split())
    print(checker(m, n, x, y))
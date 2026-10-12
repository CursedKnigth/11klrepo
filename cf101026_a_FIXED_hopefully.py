testcasecount = int(input())

for hopethisworks in range(testcasecount):
    moves=0
    a, b = map(int, input().split())
    if b > (a + 1):
        moves = -1
    elif a < abs(b):
        moves = abs(b) # all my bees have abs
    elif (a-b) % 2 == 0:
        moves = a
    else:
        moves = a+1
    print(moves)

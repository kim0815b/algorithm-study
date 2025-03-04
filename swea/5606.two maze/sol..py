import sys
sys.stdin = open('input.txt','r')

#################################
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # hyunmin = input()
    # jeoungwoo = input()

    hyunmin = []
    jeoungwoo = []
    for i in reversed(input().strip()):
        hyunmin.append(i)
    for i in reversed(input().strip()):
        jeoungwoo.append(i)


    print(bool(''))
    print(f'#{tc} {bfs()}')

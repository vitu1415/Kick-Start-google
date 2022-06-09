t = int(input())

for x in range(1, 1+t):
    n, b = map(int,input().split())

    ai = list(map(int,input().split()))
    ai.sort()
    
    tent = 0
    for y in ai:
        if y <= b:
            b -= y
            tent += 1
        if y > b:
            print('Case #{}: {}'.format(x, tent))
            break
        if n == tent:
            print('Case #{}: {}'.format(x, tent))
            break
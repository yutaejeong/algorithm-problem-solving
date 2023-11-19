import sys

input = sys.stdin.readline

N, K = map(int, input().split())
Stuffs = [0] + [list(map(int, input().split())) for _ in range(N)]
S = [0 for _ in range(K + 1)]
for k in range(1, K + 1):
    for j in range(1, N + 1):
        w, v = Stuffs[j]
        if k - w >= 0:
            S[k] = max(S[k], v + S[k - w])
            
print(S)

# TODO: 지금은 중복으로 들어가고 있음. 최대 하나 씩 들어갈 수 있음.
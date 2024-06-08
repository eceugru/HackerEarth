t=int(input())
for T in range(t):
    N,K=map(int,input().split())
    m=1
    for i in range(N):
        m=(m*K)%(1000000007)
        K-=1
    print(int(m))
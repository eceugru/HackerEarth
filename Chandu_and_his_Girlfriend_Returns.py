T=int(input())
z=[]
for i in range(T):
    N,M=map(int, input() .split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A)!=N:
        A = list(map(int, input().split()))
    if len(B)!=M:
        B = list(map(int, input().split()))
    Z=(A+B)
    Z.sort(reverse=True)
    for y in Z:
      print(y, end=" ")
    print()
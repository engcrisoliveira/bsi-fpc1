N = int(input())
def Recursao(N):
    if N == 0: return "b"
    elif N == 1: return "a"
    else: return Recursao(N-1) + Recursao(N-2)
print(Recursao(N))
def matrix_multiplication(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C

T = int(input())
for _ in range(T):
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    B = [list(map(int, input().split())) for _ in range(n)]

    A2 = matrix_multiplication(A, A, n)
    A3 = matrix_multiplication(A2, A, n)


    print("YES" if A3 == B else "NO")

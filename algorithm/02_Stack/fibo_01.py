def fibo(n):
    if n <= 1:
        return n
    return fibo(n-2) + fibo(n-1)

print(fibo(5))

def fibo(n):    # 5
    if len(memo) <= n:      # 메모에 5번째 없지?
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]

print(fibo(5))
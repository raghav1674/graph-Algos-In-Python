def nthFibonacii(n):

    if n == 1:
        return 0
    if n == 1 or n == 2:
        return 1
    return nthFibonacii(n-1) + nthFibonacii(n-2)


dp = {}


def memFibonacci(n):

    if n == 1 or n == 2:
        return n-1
    if n not in dp:
        dp[n] = memFibonacci(n-1) + memFibonacci(n-2)
    return dp[n]


def top_down_fib(n):
    if n == 1 or n == 2:
        return n-1
    a = 0
    b = 1
    for n in range(2, n):

        a, b = b, a+b
    return b


print(top_down_fib(8))

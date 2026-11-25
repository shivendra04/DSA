# f(n) = f(n-1) + f(n-2)

# memoization
def find_fib(n, dp):
    if n<=1:
        return n

    if dp[n] != -1:
        return dp[n]

    fib1 = find_fib(n-1, dp)
    fib2 = find_fib(n-2, dp)
    dp[n] = fib1 + fib2
    return dp[n]

def main():
    n = 6
    dp = [-1]*(n+1)
    fib = find_fib(n, dp)
    print(fib)

# main()
# tabulation

def find_fib_tab(n):
    dp = [-1]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n-1]

print(find_fib_tab(7))

# 遞迴方法
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

        
# 動態陣列方法
def fibonacci_DP(n):
    if n == 0 or n == 1:
        return n
    dp = [None for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
      dp[i] = dp[i-1] + dp[i-2]
    return dp[n]



# main
i=0
while True:
    try:
        x1 = fibonacci_DP(i)
        print("Dynamic   n = ", i)
        x2 = fibonacci_recursive(i)
        print("Recursive n = ", i)
        print("------------------")
        i+=1
    except RecursionError:
        print("崩潰時 n = ",i)
        break
        
    
    
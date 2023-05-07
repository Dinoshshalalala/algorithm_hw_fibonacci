import time
import matplotlib.pyplot as plt


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




# 建list存放執行時間
recursiveTime_list = []
DPTime_list = []

# main
def main():    
  
    for i in range(10, 110, 10):
        start1 = time.perf_counter()
        fibonacci_recursive(i)
        end1 = time.perf_counter()
        recursiveTime_list.append(end1-start1)
        print("finish recrusive n = ", i)
        print("time = ", end1-start1)
        
    print("--------------------------------------------------")
            
    for i in range(10, 110, 10):
        start2 = time.perf_counter()
        fibonacci_DP(i)
        end2 = time.perf_counter()
        DPTime_list.append(end2-start2)
        print("finish Dp n= ", i)
        print("time = ", end2-start2)

# 畫兩時間函式圖
def plot(listname,string):
    plt.cla()
       
    # 創建折線圖
    plt.plot(n_value, listname)
    
    
    # 添加標題和軸標籤
    plt.title('relationships with Time and n')
    plt.xlabel('n=')
    plt.ylabel('Time')
    
    # 顯示圖表
    #plt.show()
    plt.savefig(string + '.png')
    
    


# 建list放n=10~100
n_value = []
for i in range(10, 110, 10):
    n_value.append(i)


# exe
main()
plot(recursiveTime_list, "recursive")
plot(DPTime_list, "DP")

    
    
    

        
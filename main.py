# 作業1 等腰三角形
rows = 4 #總共要印出幾行
def tri(rows):                     # 先定義函式
    for i in range(1, rows + 1):     # for迴圈i從1到rows
        # 先印出空格
        print(" " * (rows - i), end="")# 空白部分是用rows-第i行，沒有要換行所以end=""
        # 再印出星號
        print("*" * (2 * i - 1))# 星號部分是用2 * 第i行 - 1

tri(rows)# 呼叫tri函式，並傳遞rows作為參數


# 作業2 99乘法表
def ninenine():
    i = 1  
    while i <= 9:  # 當i<=9時執行while迴圈
        j = 1  
        while j <= 9:  # 當j<=9時執行while迴圈
            result = i * j  # 計算乘法結果
         
            print(f"{i} * {j} = {result}", end="  " if result < 10 else " ")# 如果結果是一位數，後面加兩個空格，如果是兩位數，後面加一個空格
            j += 1  # j+1
        print()  
        i += 1  # i+1

# 呼叫函式來打印乘法表
ninenine()

# 作業3 輸入一個數字，會顯示0~該數字之間所有質數的數量，還有把所有質數列出來
n=int (input("input a number:"))
prime = [True]*(n+1) # 先列出0到n+1的數字
prime[0] = False # 0跟1都不是質數先刪掉
prime[1] = False

for i in range(2,n+1):
    if prime[i]==True:   # 如果i是質數，就印出來
        print(i)
        for j in range(2*i,n+1,i):  # 把i的倍數全部去除
            prime[j]=False


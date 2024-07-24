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
def multiplication_table():
    i = 1  
    while i <= 9:  # 當i<=9時執行while迴圈
        j = 1  
        while j <= 9:  # 當j<=9時執行while迴圈
            result = i * j  # 計算乘法結果
         
            print(f"{i} * {j} = {result}", end="  " if result < 10 else " ")# 如果結果是一位數，後面加兩個空格，如果是兩位數，後面加一個空格
            j += 1  # j+1
        print()  # 內層迴圈結束後換行，開始新的一行的乘法表
        i += 1  # i+1

# 呼叫函式來打印乘法表
multiplication_table()


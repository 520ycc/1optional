"""
简答题

17.了不起的分支和循环（IV）| 课后测试题及答案
0. continue 语句和 break 语句都能够跳出循环体，那么它们的区别是什么呢

1. 在不上机的情况下，你能看出下面代码会打印多少次 "FishC" 吗？
2. 你觉得 while-else 语法存在的意义是什么？
3. 你能看出下面代码存在什么问题吗？
4. 请看下面代码，当 break 语句执行之后，程序是跳转到位置 1 还是位置 2 呢？
5. 下面代码存在两个问题，细心的你发现了吗？
"""
# 1
i = 0
j = 9
while i < j:
    i += 1
    j -= 1
    print("FishC")
"""
1.
5次   09   18  27   36   45   
2.
当while不在执行后，是否输出接下来的print输出
若只有while语句时，结束便可输出print
若加上了else语句，则可以判断出是否有执行完while语句
"""
# 3
i = 0
while i < 10:
    if i % 2 == 0:
        continue
    i += 1
    print(i)
"""
3.
加了continue语句之后，又回到了最初的起点，判断while语句为True后再次执行while语句
i永远不会再变
程序便不会再往下，陷入了死循环
"""
# 4
day = 1
while day <= 7:
    while hour <= 8:
        print("今天，我一定要坚持学习8个小时！")
        hour += 1
        if hour > 1:
            break
   # 位置1
   day += 1
# 位置2
"""
4.
跳转到位置1
当break语句结束后，意味着hour已经满足if hour > 1:这行代码
返回应该回到while hour <= 8:这行直到满足hour > 8为止
"""
# 5
while True:
    command = input("请输入命令（exit/pow）：")
    if command == "pow":
        base = input("请输入底数：")
        exp = input("请输入指数：")
        pow(base, exp)
   elif command == "exit":
       continue
"""
5.
continue让这个elif陷入死循环
elif 改成else
"""
#标准答案
'''
1.continue 语句是跳出本次循环，回到循环的开头；而 break 语句则是直接跳出循环体，继续执行后面的语句。
2.上面代码会打印 5 次 "FishC"
3.while-else 可以非常容易地检测到循环的退出情况。
解析：存在即合理，任何不合理的东西都会随着版本的升级迭代而被淘汰
4.程序会进入死循环。位置1。
解析：记住，无论多少层循环嵌套，break 语句和 continue 语句都只能作用于离它最近的那一层。
5.(1)第 4 和第 5 行代码使用 input 函数获取的是一个字符串结果，如果要作为 pow() 函数的参数使用应该将它们转换成整数。
(2)第 8 行按照题意应该是“用户输入 exit 表示退出程序”，所以应该将 cotinue 修改为 break
base = int(input("请输入底数："))
exp = int(input("请输入指数："))
'''
'''
动手题
0. 将九九乘法表倒过来打印，要求代码实现效果如下图
1. 找出 10 以内的所有素数，如果不是素数，请打印出该合数对应的乘积公式，要求代码实现效果如下图
'''
#99乘法表
a = 1
while a <= 9:
    b = 1
    while b <=a:
        print(b, "*", a, "=", a * b, end="  ")
        b+=1
    print()
    a+=1
#倒过来的99乘法表
a = 1
while a <= 9:
    b = 9
    while b >= a:
        print(b, "*", a, "=", a * b, end="  ")
        b -= 1
    print()
    a += 1
# 找出 10 以内的所有素数，如果不是素数，请打印出该合数对应的乘积公式。
n = 2
while n < 10:
    x = 2
    while x < n:
        if n % x == 0:
            print(n, "=", x, "*", n // x)
            break
        x += 1
    else:
        print(n, "是一个素数")
    n += 1
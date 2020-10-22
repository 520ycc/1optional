"""
0. 以下哪个变量的命名不正确？为什么？
    (A) MM_520  (B) _MM520_  (C) 520_MM  (D) _520_MM
1. 在不上机的情况下，以下代码你能猜到屏幕会打印什么内容吗
myteacher = '小甲鱼'
yourteacher = myteacher
yourteacher = '黑夜'
print(myteacher)

myteacher = '小甲鱼'
yourteacher = myteacher
myteacher = '黑夜'
print(yourteacher)

first = 520
second = '520'
first = second
print(first)
2. 除了使用反斜杠（\）进行字符转义，还有什么方法可以打印：Let's go! 这个字符串？
3. 如果非要在原始字符串结尾输入反斜杠，可以如何灵活处理？
4. 在这一讲中，我们说变量的命名需要注意一些地方，但小甲鱼在举例的时候貌似却干了点儿“失误”的事儿，你能看得出小甲鱼例子中哪里有问题吗？
动动手：
0. 还记得我们第一讲的动动手的题目吗？这一次要求使用变量，计算一年有多少秒？
提示：可以以 DaysPerYear（每年天数），HoursPerDay（每天小时数），MinutesPerHour（每小时分钟数），SecondsPerMinute（每分钟秒数）为变量名。
1. 关于最后提到的长字符串（三重引号字符串）其实在 Python3 还可以这么写，不妨试试，然后比较下哪种更方便？
"""
'''
0.C  变量不可以数字开头
1.（1）小甲鱼
（2）myteacher
（3）second
2.print("Let's go!")
3.\\
4
0.
hour = 24
minute = 60
second = 60
year = hour*minute*second*365
print(year)
'''
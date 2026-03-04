#所谓整形，就是没有小说点的数字，可以是正数、负数、也可以是0
import sys

age = 18
temp = -15

# 当数很大时，我们可以使用下划线将数字进行分组，来让数字变得更易读
salary = 300_000
house_price = 3_200_000
graduates = 12_000_000
print(salary,house_price,graduates)

#python中整数的上限值，取决于执行代码的计算机的内存和处理能力
a = 9 ** 9999
sys.set_int_max_str_digits(0)
print(a)
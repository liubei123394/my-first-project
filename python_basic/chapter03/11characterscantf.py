name = '张三'
gender = '男'
weight = 65.2
age = 12

#写法一：直接用加号进行拼接,写起来很麻烦且代码很乱，而且只能是字符串之间拼接
info1 = '我叫' + name + ',我是' + gender + '生'

#写法二：使用占位符
info2 = '我叫%s,我是%s生,我体重是%f,年龄是%d' % (name,gender,weight,age)
print(info2)

#写法三：使用f-string
info3 = f'我叫{name},我是{gender},我体重是{weight},年龄是{age}'
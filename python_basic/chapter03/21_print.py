#使用input()获取用户的输出
name = input('请输入你的姓名:')
age = input('请输入你的年龄:')

#input()获取到的内容全都是字符串类型
#print(type(age))
#将age转为整形
age = int(age)

#打印信息
print(f'{name},你今年的年龄是{age}')
print(f'{name},你明年的年龄是{age + 1}')
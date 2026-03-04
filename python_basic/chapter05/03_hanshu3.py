#定义函数（接受位置参数）
def greet(name,gender,age,height):
    print(f'我叫{name}，姓名{gender}，年龄是{age}，身高是{height}cm')
    print(f'我的身高是{height},今年{age}岁了,我叫{name}')

#调用函数
greet('张三','男',18,183)


#错误示例
#greet('张三',18,183)
#greet('张三','男',18,183)
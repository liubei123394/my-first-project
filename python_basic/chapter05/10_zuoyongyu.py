#全局作用域与局部作用域
a = 100
b = 200


def test():
    c = '尚硅谷'
    d = '你好啊'
    global a
    a = 300
    print('函数中的打印(a)',a)
    print('函数中的打印(b)',b)
    print('函数中的打印(c)',c)
    print('函数中的打印(d)',d)
test()
print('**********')
print('全局的打印(a)',a)
print('全局的打印(b)',b)
#print(c)
#print(d)
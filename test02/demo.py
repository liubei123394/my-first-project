#使用安装在当前虚拟环境中的第三方包faker
from faker import  Faker
f = Faker('zh_CN')
print(f.name())
print(f.address())
print(f.phone_number())

#使用安装在当前虚拟环境中的第三方包jieba
import jieba
result = jieba.lcut('南京市长江大桥')
print(result)

#使用安装在当前虚拟环境中的第三方包cn2an
import cn2an
print(cn2an.cn2an('九千七百四十三'))


#使用全局的标准库
from collections import Counter
list1 = [10, 20, 30, 40, 20, 30, 20, 30, 10, 10, 10]
res = Counter(list1)
print(res)
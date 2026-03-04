#定义一个Person
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age =age
        self.gender = gender

    #speak方法、run方法，它们都属于：实例方法
    def speak(self, msg):
        print(f'我叫{self.name}, 年龄是{self.age}, 性别是{self.gender}, 我想说{msg}')


#定义一个Student类，继承自Preson类
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        super().__init__(name, age, gender)
        self.stu_id = stu_id
        self.gender = gender


    #方法重写：当子类中定义一个与父类中相同的方法，那么子类中的方法就会“覆盖”父类的方法
    #def speak(self, msg):
    #    print(f'我是学生,我的学号是{self.stu_id}, 我正在读{self.grade}, 我想说{msg}')

s1 = Student('李华', 12, '男', '2025001', '初二')
s1.speak('好好学习')
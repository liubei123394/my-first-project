from datetime import datetime

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
class Student(Person):
    #计数器
    count = 0

    def __init__(self,name,age,gender):
        super().__init__(name, age, gender)
        Student.count += 1
        self.stu_id=f'{datetime.now().year}{Student.count:03d} '
        self.scores ={}  #{'数学': 90, '语文': 80, '英语': 70}

    # 给当前学生添加成绩
    def add_score(self, subject, score):
        self.scores[subject] = score

    # 计算平均分
    def calcu_avg(self):
        if self.scores:
            return sum(self.scores.values()) / len(self.scores)
        else:
            return 0
s1 = Student('张三', 18, '男')
s1.add_score('数学',90)
s1.add_score('语文',80)
s1.add_score('英语',70)
print(s1.calcu_avg())

# class Manager:
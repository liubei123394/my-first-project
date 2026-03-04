print('欢迎来到：答题闯关挑战赛（输入q可随时推出）\n')

#题目与答案
ques1 , ans1 = 'Python中用于输出的函数是？'  , 'print'
ques2 , ans2 = 'Python中用于表示逻辑"并且"的关键字是？'  , 'and'
ques3 , ans3 = 'Python中用于编译型还是解释型？'  , '解释型'


#最多可尝试次数
max_tries = 3
#总关卡数
total_levels = 3
#是否处于可游戏状态
is_playing = True

#根据题目数量开始循环
for level in range(1,total_levels + 1):
    #打印当前是第几关
    print(f'********第{level}关********')
    #取出当前关卡所对应的题目和答案
    if level == 1:
        question , answer = ques1 , ans1
    elif level == 2:
        question , answer = ques2 , ans2
    else:
        question , answer = ques3 , ans3
    #记录当前关卡的尝试次数
    tries = 1
    #若已经尝试次数，小于等于最大尝试次数，则进入循环
    while tries <= max_tries:
        #向用户提问
        user_input = input(''+question)
        #根据用户的输入，来决定做什么
        if user_input == answer:
            print('回答正确!\n')
        elif user_input == '':
            print('你的输入为空，请重新作答!\n')
        elif user_input == 'q':
            print('你已退出游戏!\n')
            is_playing = False
            break
        else:
            #计算剩余次数
            leave = max_tries - tries
            #判断是否还有剩余次数
            if leave > 0:
                print('回答错误，你还剩xxx次机会!\n')
                tries += 1
                continue
            else:
                print(f'挑战失败，本题的正确答案是：{answer},游戏结束！')
                is_playing = False
                break
    #每次进入下一关之前，都要看一下is_playing,如果is_playing为False就要结束游戏
    if is_playing == False:
        break
#如果到了这里，is_playing的值依然为Ture，那就意味着用户已经通关了！
if is_playing:
    print('恭喜你全部通关！')
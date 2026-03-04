age = int(input('请输入你的年龄：'))
has_report = input('你是否提交了体检报告？（是/否）')
leve1 = int(input('请输入你的会员等级(1/2/3)'))

print('*******💍程序的识别结果如下💍：*******')
if 18 <= age <= 45:
    print('✔️你的年龄符合比赛要求')
    if has_report == '是':
        print('✔️你已提交体检报告！')
        print('✔️你可以参加比赛')
        if leve1 == 1:
            print(f'😀尊贵的{leve1}会员，比赛结束后，你可以领取纪念T桖👚一件!')
        elif leve1 == 2:
            print(f'😀尊贵的{leve1}会员，比赛结束后，你可以领取纪念跑鞋👟一双!')
        elif leve1 == 3:
            print(f'😀尊贵的{leve1}会员，比赛结束后，你可以领取运动耳机🎧一副!')
        else:
            print('❌你输入的会员等级不确定!')
    elif has_report == '否':
        print('❌你未提交体检报告，不能参加比赛！')
    else:
        print('❌你输入的体检报告有误！')
else:
    print('❌抱歉，参赛年龄需要在18-45之间！')
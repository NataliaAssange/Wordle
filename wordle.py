print("wordle猜单词玩法说明：\n谜底是一个5个字母的英语单词\n如果你输入的单词中，有字母与谜底对应位置的字母相同，就会变为蓝色\n如果没有猜中，就会变为黄色\n你有6次机会，加油吧！")
import csv
import random
with open('targetwordlist.csv',encoding='utf-8')as a:
    list1=list(csv.reader(a))
    tgt=random.choice(list1)
    t0=tgt[0]
with open('possiblewords.csv',encoding='utf-8')as b:
    list2=list(csv.reader(b))
    listp=list(map(lambda x: x[0],list2))
n=0
while n<6:
    w=input("请输入一个5个字母的英语单词：")
    while (w in listp):
        listt=list(t0)
        listw=list(w)
        for i in range(5):
            if listw[i]==listt[i]:
                print("\033[37;44m %s\033[0m"% listw[i],end="")
            else:
                print('\033[34;43m %s\033[0m'% listw[i],end="")
        if w==t0:
            print()
            print("恭喜你！只用了",n+1,"次就猜对了！")
            break
        else:
            print()
            print("没有猜对，再来一次吧！你还有",5-n,"次机会")
            n=n+1
            w=input("请重新输入一个5个字母的英语单词：")
    else:
        print("对不起，这不是一个5个字母的英语单词，请重新输入")
print("正确答案是",t0)

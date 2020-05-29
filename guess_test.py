#!usr/bin/env python
import random
setNum = random.randint(1,50)
print("开始猜吧！本游戏设定数为1到50之前")
guessNum = int(input("请输入你猜的数："))
if guessNum == setNum:
    print("恭喜你猜对了,数字是：" + setNum)
else:
    if guessNum > setNum:
        print("大了")
    else:
        print("小了")
    while guessNum !=  setNum:
        guessNum = int(input("猜错了，请重新输入："))
        if guessNum == setNum:
            print("你猜对了,数字是：" + str(setNum))
        else:
            if guessNum > setNum:
                print("大了")
            else:
                print("小了")
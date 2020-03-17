'''
Attribute Default Value
'''
HP = 100
MaxHP = 100
ATK = 10
DEF = 10
LUC = 10
DOL = 0
IQ = 70



from tools.ClearScreen import *

def GameOver():
    print("Game Over!!")
    import sys
    sys.exit()
    

if __name__ == '__main__':
    while True:
        print("<Q001>")
        print("是否做好一切萬全的準備，迎接這個遊戲的挑戰？")
        print("(A):是。")
        print("(B):否。")
        ANS = input("")
        if (ANS == 'A'):
            print("很好，你通過了第一關考驗。")
            break
        elif (ANS == 'B'):
            print("懦夫，你可以退出遊戲了。")
            GameOver()
            break
        else:
            print("請重新輸入。")


    print()
    while True:
        print("<Q002>")
        print("這天，你在床上醒來。")
        print("哇，你發現這是多麼一個美好的早晨啊。")
        input()
        print("要再休息一下嗎？")
        print("(A):懶得起床，再躺一下就好。")
        print("(B):奮力起床！")
        ANS = input("")
        if (ANS == 'A'):
            print("休息足夠了。體力恢復10。")
            HP = HP + 10
            break
        elif (ANS == 'B'):
            print("使勁全力起身！")
            input()
            print("但由於太累了，體力減少5。")
            print("...WTF？")
            HP = HP - 5
            MaxHP = MaxHP + 10
            break
        else:
            print("請重新輸入。")

    print()
    while True:
        print("<Q003>")
        print("起床後，你發現這裡不是你的房間，床也不是自己的床。")
        print("環顧四周，發現房間角落裡有一面全身鏡。")
        input()
        print("「有一面鏡子耶...」你自己說到。要照一下鏡子嗎？")
        print("(A):好啊。")
        print("(B):長的太醜，我死都不想照。")
        ANS = input("")
        if (ANS == 'A'):
            print("你照了一下鏡子，發現鏡子裡的人長得異常的帥氣。")
            input()
            print("帥到連自己認不得了。")
            print("不，這...這甚至不是自己的臉啊！")
            input()
            print("這..這人是誰啊！")
            break
        elif (ANS == 'B'):
            print("『對啊，我居然長這麼醜...")
            print("我爸爸媽媽居然把我生成這副德性...』")
            input()
            print("你開始回想起過去種種不愉快的經歷。")
            print("難道長得太醜是一種過錯嗎？難道長的醜就要被霸凌嗎？")
            input()
            print("各種悲嘆、哀傷的負面情緒湧入你的內心...")
            print("眼淚如泉水般湧出，你難過得快要死了。")
            print("<體力減少80。>")
            HP = HP - 80
            print("就在你快要難過死掉的瞬間...")
            input()
            print("你內心迅速崩潰。")
            input()
            print("很遺憾，你死了。")
            GameOver()
            break
        else:
            print("請重新輸入。")
    
    
    


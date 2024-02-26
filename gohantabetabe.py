import random as rdm

genre = ["和食", "洋食", "中華"]
wa = ["お寿司", "うどん", "そば"]
yo = ["パスタ", "オムライス", "ハンバーグ"]
chu = ["麻婆豆腐", "油淋鶏", "餃子"]

while True:
    dinner = rdm.choice(genre)

    decide = input("今日のご飯は"+dinner+"でどう？>>y/n")
    if decide == "y":
        print("いっぱい", dinner, "食べるぞ！")
        if dinner == "中華":
            chuchoice = rdm.choice(chu)
            final = input(chuchoice + "はどう？？>>y/n")
            if final == "y":
                print(chuchoice, "で決まり！")
                break
        if dinner == "洋食":
            yochoice = rdm.choice(yo)
            final = input(yochoice + "はどう？？>>y/n")
            if final == "y":
                print(yochoice, "で決まり！")
                break
        if dinner == "和食":
            wachoice = rdm.choice(wa)
            final = input(wachoice + "はどう？？>>y/n")
            if final == "y":
                print(wachoice, "で決まり！")
                break

#2027２度目のInputでelseだったときにFinalに戻るようにする
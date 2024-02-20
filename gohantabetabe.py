import random as rdm

genre = ["和食", "洋食", "中華"]
wa = ["お寿司", "うどん", "そば"]
yo = ["パスタ", "オムライス", "ハンバーグ"]
chu = ["麻婆豆腐", "油淋鶏", "餃子"]

while True:
    dinner = rdm.choice(genre)
    wachoice = rdm.choice(wa)
    yochoice = rdm.choice(yo)
    chuchoice = rdm.choice(chu)

    decide = input("今日のご飯は"+dinner+"でどう？>>y/n")
    if decide == "y":
        print("いっぱい", dinner, "食べるぞ！")
        if dinner == "中華":
            print(chuchoice, "にしよう！")
            break
        if dinner == "洋食":
            print(yochoice, "にしよう！")
            break
        if dinner == "和食":
            print(wachoice, "にしよう！")
            break

#0221の目標
#ループ内にループ入れる
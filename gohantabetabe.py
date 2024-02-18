import random as rdm

genre = ["和食", "洋食", "中華"]
wa = ["お寿司", "うどん", "そば"]
yo = ["パスタ", "オムライス", "ハンバーグ"]
chu = ["麻婆豆腐", "油淋鶏", "餃子"]

dinner = rdm.choice(genre)
decide = input("今日のご飯は"+dinner+"でどう？>>y/n")
if decide == "y":
    print("いっぱい", dinner, "食べるぞ！")
else:
    print("何食べようかなあ")
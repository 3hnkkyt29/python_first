#part1
users = {"user1" : "active", "user2" : "inactive", "user3" : "active"}
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
print(users)
#copy()について

#users = {"user1" : "active", "user2" : "inactive", "user3" : "active"}
#for user, status in users.items():
#    if status == "inactive":
#        del users[user]
#print(users)
#↑copy()がないとエラーになるよ

#part2
for i in range(1,10):
    for j in range(1,10):
        print(i*j, end=",")
    else:
        print("\n", str(i), "の段でした")

for i in range(2,10):
    if i % 2 ==0:
        print(i, "は偶数")
        continue
    print(i, "は奇数")

for i in range(2,10):
    if i % 2 ==0:
        print(i, "は偶数")
        break
    print(i, "は奇数")
#continueだとループの最初に戻るけどbreakだともう完全にループから抜ける
    
#part4
    pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
    pairs.sort(key=lambda pair: pair[1])
    pairs

print("a" in "abc")
print("az" in "abc")
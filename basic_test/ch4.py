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
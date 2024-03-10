#part2
t = 10, "a", [1,2]
print(t)

v = 123, 456, "hello"
a, b, c = v
print(a)
print(b)
print(c)

set1 = {1, 2, 3, "a"}
set2 = {4, 5, 6, "a"}
wa = set1 | set2
print(wa)
sa = set1 - set2
print(sa)
seki = set1 & set2
print(seki)
taisyo = set1 ^ set2
print(taisyo)

for count in range(3):
    print(count)

for i in range(4):
    if i == 2:
        continue
    print(i)

num = [1, 2, 3, 4]
num.pop(2)
print(num)

area = [x ** 2 for x in range(3)]
print(area)


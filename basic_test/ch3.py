#part1
n1 = 50 - (5*6)
print(n1)
print(type(n1)) #int

n2 = 20/5
print(n2)
print(type(n2)) #float
n3 = 20//5
print(n3)
print(type(n3)) #int

print(9**2)

n4 = (3 + 5j)*(3 - 5j)
print(n4)

n5 = 0.1
n6 = 0.2
print(n5 + n6) #10進数のあれこれでなんか上手く0.3にはならない

#part2.1
print("""
      first
      second
      third
      """)

print('"Isn\'t," they said.') #エスケープ

print('C:\some\name')
print(r'C:\some\name') #rを入れることで¥nが特殊文字として認識されなくなる

a = "python"
b = "a" + a[1:]
print(b)
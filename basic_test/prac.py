# set = {'pine', 'apple', 'apple', 'pen'}
# print(set)

# num = {'one': 1, 'two':2}
# num['three'] = 3
# print(num['three'])

# for i in range(4):
#     if i == 2:
#         continue
#     print(i)

# num = [1, 2, 3, 4]
# num.pop(2)
# print(num)

# num = [1, 2, 3]
# del num[:1]
# print(num)

# a = 'Python'
# b = 'programing'
# print(f'{a} is a {b} language')
# print('{0} is a {1} language'.format(a, b))
# print('%s is a %s language' % (a, b))

# str = 'pen'
# print(str + 'pine' 'apple')

# print("na" + "na")

# x = 10

# if x == 10:
#     print('a')
#     if x <= 10:
#         print('b')
#         if x > 10:
#             print('c')
#             if x >= 10:
#                 print('d')

# print('e')

# for i in range(3):
#     if i == 0:
#         continue
#     print(i)
#     for v in ['a', 'b', 'c']:
#         print(v)
#         break

# number = 7
# def job(arg=number):
#     print(arg)
# number = 10
# job()
# job(20)

# test = 'one',
# print(test)

# list = ['b', 'a', 'c']
# sorted(list)
# print(list)

arg = 'out'

def func1():

    def func2():
        arg = 'local'

    def func3():
        nonlocal arg
        arg = 'nonlocal'

    def func4():
        global arg
        arg = 'global'

    arg = 'in'

    func2()
    print(arg)

    func3()
    print(arg)

    func4()
    print(arg)

func1()
print(arg)
# from datetime import datetime

# date_time_str = '18/09/19 01:55:19'

# date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')

# if type(date_time_str) == str:
#     print(date_time_str)
#     print('----------------True')

# if type(date_time_obj) == datetime:
#     print('-----------------data True')


# print ("The type of the date is now",  type(date_time_obj))
# print ("The date is", date_time_obj)

# n = 1114

# str_n = str(n)
# # print(len(str_n))

# # new_n = str_n.replace('0', '5')
# # print(new_n)

# if '0' in str_n:
#     new_n = str_n.replace('0', '5')
#     print(new_n)
# else:
#     print(str_n)

# dictionary = {'key1':'1', 'key2':'2', 'key3':'3'}

# print(dictionary)

# a = dictionary.pop('key1')

# print(a)
# print(dictionary)

# a = 'true'

# if a != 'true' or a != 'false':
#     print('1')
# else:
# #     print('2')

# n = 5
# arr = [0,-1,2,-3,1]

# for num in arr:
#     r = num[0] + num
    
#     print(r)

# this is shift + O (new line above)
# this shif + o (new line below) 

# this is vim

# avoid even numbers
# give number of houses and return the sum of money


# class Solution:
#     def maximizeMoney(self, N , K):
#         # code here 
#         ans = K*(N+1)/2
        
#         if N == 1:
#             return K
        
#         print(len(str((ans))))
#         return ans

# def f():
#     s = 'my function'
#     print(s)

# def purchase(amount, item, price):
#     print()
#     print(f'{amount} {item} cost ${price:.2f}')
#     print()

# purchase(6,'apples', 10.00)

# def positional_purchase(amount=1, item='mango', price=4.12):
#     print(f'{amount} {item} cost you ${price:.2f}.')

# positional_purchase()
# print()
# positional_purchase(3,'strawberry',12.52)
# print()
# positional_purchase(item='malako')

# def f(fx):
#     print('fx=', fx, 'and id(fx)=', id(fx))
#     fx = 10
#     print('fx=', fx, 'and id(fx)=', id(fx))

# x = 5
# print('x=', x, 'and id(x)=', id(x))
# print()
# f(x)
# print()
# print('x=', x, 'and id(x)=', id(x))

def change(x):
    x[0] = 'this is function'

mylist = ['mango','durian','orange']
print('before call',mylist)
change(mylist)
print('after call', mylist)

def do_return():
    return print('this is return')

do_return()

def double_list(x):
    ans = [] 
    for i in x:
        ans.append(i * 2)
    return print(ans)

numbers = [2,3,4,5]
double_list(numbers)
print()
print()
# Variable-Length Argument Lists
def avg(a, b, c):
    return (a + b + c) / 3
print()
# Multiple Unpackings in a Python Function Call################################
def unpackcall(**kwargs):
    print(kwargs)
    for word in kwargs.keys():
        print('word -->',word)
        print(kwargs[word])

dic = {'name':'prach', 'age':'23', 'job':'programmer'}
unpackcall(**dic)
print()



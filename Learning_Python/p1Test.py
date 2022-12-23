#x = int(input())
#y = int(input())

#x = x%y
#x = x%y
#y= y%x
#print("ddd",y)
#x = input()
#y = input()

#print(x + y)

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)
print("0------------------------")



#my_list = [[0,1,2,3] for i in range(2)]
#print(my_list[2][0])

my_list = [1,2,3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)
print("1------------------------")


#my_list = [1,2,3,4]
#print(my_list[-3:-2])

my_list_1 = [1,2,3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)
print("2------------------------")


nums = [1,2,3]
vals = nums[-1:-2]
print(vals)
print("3------------------------")

for i in range(1):
    print("#")
else:
    print("#")
print("4------------------------")

vals = [0,1,2]
print(vals)
vals[0], vals[2] = vals[2], vals[0]
print(vals)
print("5------------------------")

var = 1
while var< 10:
    print('#')
    var = var << 1
print("6------------------------")

var = 0
while var< 6:
    var +=1
    if var%2 == 0:
        continue
    print('#')
print("6------------------------")

my_list = [i for i in range(-1, 2)]
print(my_list)
a = 1
b = 0
c = a&b
d= a|b
e = a^b
print(c+d+e)
print("7------------------------")

x = 1
x = x == x
print(x)
print("8------------------------")

i = 0
while i <= 5:
    i +=1
    if i%2==0:
        break
    print('*')
print("9------------------------")

z = 10
y = 0
x = y < z and z>y or y>z and z<y
print(x)
print("10------------------------")

my_list_1 = [3,1,-2]
print(my_list_1[my_list_1[-1]])
print("11------------------------")

i = 0
while i<= 3:
    i +=2
    print("*")
print("12------------------------")

#def fun(in=2, out=3):
#    return in*out
#print(fun(3))


tup = (1, ) + (1, )
print(tup)
tup = tup + tup
print(tup)
print(len(tup))
print("13------------------------")

try:
    k = "kang"#input("k: ")
    a = len(k)
    L = "ds"#input("L: ")
    b = len(L)*2
    print(len(L))
    print(a/b)
except ZeroDividionError:
    print("SEXY")
except ValueError:
    print("WV")
except:
    print("E.E.E")
print("14------------------------")

#val = input("VAL: ")
#print(10/val)

def any():
    print(var + 1, end= '')

var = 1
any()
print(var)
print("15------------------------")

def fun(x):
    x +=1
    return x

x = 2
x= fun(x+1)
print(x)
print("16------------------------")

def fun(inp=2, out=3):
    return inp*out
print(fun(out=2))
print("17------------------------")

#my_list = ['mary', 'had', 'a', 'little', 'lamb']
#def my_list(my_list):
#    del my_list[3]
#    my_list[3] = 'ram'
#
#print(my_list(my_list))

tup = (1,2,4,8)
tup = tup[-2:-1]
print(tup)
tup = tup[-1]
print(tup)
print("18------------------------")

#def f(a):
#    return d*d
#def f1(a):
#    return f(a)*f1(a)
#print(f1(2))

dic = {'one':'two', 'three':'one', 'two':'three'}
v = dic['one']

for k in range(len(dic)):
    v = dic[v]
print(v)
print("19------------------------")

def f(x):
    if x == 0:
        return 0
    return x+ f(x-1)
print(f(3))
print("20------------------------")

def fun(x, y, z):
    return x+2 *y+3 * z
print(fun(0, z=1, y=3))
print("21------------------------")

#def fun(x):
#    if x%2 == 0:
#        return 1
#    else:
#        return
#print(fun(fun(2) + 1))

m = [1,2]
#for x in m.vals():
#   print(x, end="")
for v in range(2):
    m.insert(-1, m[v])
print(m)

try:
    print(5/0)
except (TypeError, ValueError, ZeroDivisionError):
    print("a")

x = 1
y = 2

x, y, z = x, x, y

print(x, y, z)

z ,y , z = x, y, z

print(x, y, z)

lst = [ i for i in range(-1,-2)]
print(lst)

lst = [[x for x in range(3)] for y in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

a = 1
b = 0
a = a ^ b
print(a)
b = b ^ a
print(b)
a = a ^ b
print(a)
print(a, b)










    




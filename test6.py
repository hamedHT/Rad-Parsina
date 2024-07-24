#sets.
#not index and not duplicate
my_set = {"usa" , "india","iran","china"}
print(len(my_set))
my_set.add("uk")
my_set.remove("iran")
my_set.discard('usa')
my_set.pop()

print(my_set)
a = {1,2,3,4}
b = {3,4,5,6}
# c = a.union(b)
c = a | b
# d = a.intersection(b)
d = a & b
# y = a.difference(b)
y = a - b

my_set2 = set()
my_set2 = my_set.copy()

#dictionary

my_dic = {'firstname' : 'ali','lastname':'alipour','age':24}
# print(my_dic['age'])
my_dic['city'] = 'tehran'
my_dic['firstname'] = 'reza'
del my_dic['city']

Keys = my_dic.keys()
Values = my_dic.values()
print(Values)

#فعالیت منزل
# متد  زیر را در اینترنت جستجو کرده و مثال هایی برای ان بیاورید 
# isdisjoint

# در مورد متد های بیلت این در دیکشنری جستجو کنید و مثال هایی بیاورید
# built in
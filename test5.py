#methods in list

my_list = [10 ,20 ,30 , 30]
my_list.append(40)
my_list.insert(0,15)
my_list.pop(2)
my_list.reverse()
my_list.sort()
Min = min(my_list)
Max = max(my_list)
c = my_list.count(30)
copies = my_list.copy()
my_list.extend([100,200])
my_list.remove(15)
print(my_list)

my_list2 = [[1,2,3,4],[10,20,30,40]]
print(my_list2[0][2])

#tuple()

my_tuple = (1, 2 ,'a')
#my_tuple[0] = 3
print(my_tuple[:2])
print(len(my_tuple))
my_tuple2 = ('1', 11)
print(my_tuple + my_tuple2)

listt = [my_tuple,1 , 2 , 20]
print(listt)



#فعالیت منزل 
#لیست زیر را به طور نزولی مرتب کنید
#[1,5,4,77,88,63,25,48,51,30,11]
#برنامه ای بنویسید که هربار یک عضو تصادفی یا رندم از یک لیست را برگرداند
#برنامه ای بنویسید که یک لیست ایجاد کند و سپس اعداد زوج لیست اول و اعداد فرد لیست دوم را در لیست خالی اضافه کند و مرتب شده نمایش دهد
#برنامه ای بنویسید که اطلاعات شخصی یک کاربر را دریافت کند و در یک لیست وارد کند
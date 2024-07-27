test = "Rad Parsina"
result = test.capitalize()
result = test.count('a')
result = test.lower()
result = test.upper()
result = test.replace("Rad","hamed")
result = test.isdigit()
result = test.isspace()
result = test.split(' ')
result = '  '.join(test)

print(result)
####################################################

speed = int(input("please enter your speed: "))

if speed > 120:

    print('your driving is very fast')

elif speed > 100 and speed<= 120:

    print('your driving is fast')

elif speed <= 100 and speed > 60:

    print('your driving is good')

else:

    print('your driving is low')

######################################################################

nomre_kelasi = int(input("enter your nomre_kelasi: "))
nomre_emtehan = int(input("enter your nomre_emtehan: "))  

if nomre_kelasi > 10 or nomre_kelasi > 10:
    print('you are pass')
elif nomre_kelasi == 10 or nomre_emtehan == 10:
        print('you are pass!!')
else:
     print('you are fail!!')

#######################################################################
#قعالیت منزل 
#برنامه ای بنویسد که با دریافت یک عدد از کاربر زوج با فرد بودن انرا نمایش دهد
#برنامه ای بنویسید که با دریافت یک عدد از یک تا هفت روز هفته را نشان دهد
#برنامه بنویسید که با دریافت یک متن ده خطی متن را بر اساس کاراکتر نقطه قسمت بندی کند و سپس بر اساس کاراکتر اسپیس متصل کند
#برنامه بنویسید که با دریافت ماه جاری از سیستم پایتون نام ماه را نمایش دهد
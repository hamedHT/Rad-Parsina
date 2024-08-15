#حل تمرین
#سنگ-کاغذ-قیچی

import random

penalty = 0
score = 0
i = 0
game = ['k','gh','s']
while i < 10:
    bot = random.choice(game)
    man = input('enter your choose: ')
    if bot == man:
        print("!!!!!!!draw!!!!!!")
    elif man == 'k' and bot == 's':
        print('win')
        score += 1
    elif man == 'k' and bot == 'gh':
        print('loose')
        penalty += 1
    elif man == 's' and bot == 'k':
        print('loose')
        penalty += 1
    elif man == 's' and bot == 'gh':
        print('win')
        score += 1
    elif man == 'gh' and bot == 's':
        print('loose')
        penalty += 1
    elif man == 'gh' and bot == 'k':
        print('win')
        score += 1
    else:
        print('incorrect')
    i += 1

if score > penalty:
    print('**You win with score ',score)
else:
    print("!!Game Over!!")

#محاسبه فاصله ی اقلیدسی
from math import *
point1 = []
point2 = []
point1.insert(0,int(input("enter X1: ")))
point1.insert(1,int(input("enter y1: ")))
point2.insert(0,int(input("enter X2: ")))
point2.insert(1,int(input("enter y2: ")))

distance = sqrt((point2[0]-point1[0])** 2 + (point2[1]-point1[1])**2)
print(distance)

function
def polindrome():
    text = input('enter a word: ')
    if text == text[::-1]:
        print('the word is polindrome')
    else:
        print('the word is polindrome')

print(polindrome())


def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
# Driver Program 
print(Fibonacci(9))

def string_equal(str1,str2,case_sensitve = False):
    if case_sensitve == True:
        return str1 == str2
    else:
        return str1.lower() == str2.lower()
    
print(string_equal('tehran','Tehran',True))    

#تمرین در منزل
#برنامه برای محاسبه یه ماشین حساب با چهار عمل اصلی بنویسید
#برنامه بنویسید که با دریافت سه ضریب معادله درجه 2 ریشه های انرا محاسبه کند
#برنامه ای بنویسید که با دریافت سه ضلع یک مثلث قلئم الزاویه سینوس ،کسینوس و تانزانت انرا محاسبه کند
#بازی گل یا پوچ را در پایتون شبیه سازی کنید





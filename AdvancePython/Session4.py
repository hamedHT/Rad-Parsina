class Pet:
    def __init__(self, breed):
        self.breed = breed
    def about(self):
        print(f"This is {self.breed} breed")
class Insurable:
    def __init__(self, amount):
        self.amount = amount
    def about(self):
        print(f"Its insured for an amount of {self.amount}")
class Cat(Pet, Insurable):
    def __init__(self, weight, breed, amount):
            self.weight = weight
            Pet.__init__(self, breed)
            Insurable.__init__(self, amount)
    def get_weight(self):
            print(f"{self.breed} Cat weighs around {self.weight} pounds")
def main():
        cat_obj = Cat(15, "Ragdoll", "$100")
        cat_obj.about()
        cat_obj.get_weight()
if __name__ == "__main__":
        main()

#______________________________________________________________________________________________________________        

import math
class ArcLength:
    def __init__(self):
        self.radius = 0
        self.angle = 0
    def calculate_arc_length(self):
        result = 2 * math.pi * self.radius * self.angle / 360
        print(f"Length of an Arc is {result}")
al = ArcLength()
al.radius = 9
al.angle = 75
print(f"Angle is {al.angle}")
print(f"Radius is {al.radius}")
al.calculate_arc_length()

#-----------------------------------------------------------------------------------------------------------------

class Collinear:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
    def check_for_collinear(self, point_2_obj, point_3_obj):
        if (point_3_obj.y_coord - point_2_obj.y_coord)*(point_2_obj.x_coord - self.x_coord)\
            == (point_2_obj.y_coord - self.y_coord)\
            *(point_3_obj.x_coord - point_2_obj.x_coord):
            print("Points are Collinear")
        else:
            print("Points are not Collinear")
def main():
    point_1 = Collinear(1, 5)
    point_2 = Collinear(2, 5)
    point_3 = Collinear(4, 6)
    point_1.check_for_collinear(point_2, point_3)
if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------------------------------------------

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def add_time(self, duration):
        opera_hours = self.hours + duration.hours
        opera_minutes = self.minutes + duration.minutes
        opera_seconds = self.seconds + duration.seconds
        while opera_seconds >= 60:
            opera_seconds = opera_seconds - 60
            opera_minutes = opera_minutes + 1
        while opera_minutes >= 60:
            opera_minutes = opera_minutes - 60
            opera_hours = opera_hours + 1
            print(f"Opera ends at {opera_hours}:{opera_minutes}:{opera_seconds}")
def main():
    opera_start = Time(10, 30, 30)
    opera_duration = Time(2, 45, 50)
    opera_start.add_time(opera_duration)
if __name__ == "__main__":
    main()
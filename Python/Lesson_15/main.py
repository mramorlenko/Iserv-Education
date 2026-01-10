from animals import *

def info(object):
    object.printInfo()

def animalSpeak(object):
    object.speak()

cat = Cat("Рыжая", "Мурчек", 15)
dog = Dog("Ёршский-Терьер", "Гавчег", 13)

info(cat)
info(dog)

animalSpeak(cat)
animalSpeak(dog)
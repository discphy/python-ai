class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def sleep(self):
        print("Zzz")

class GuardDog(Dog):

    def __init__(self, name, breed):
        super().__init__(name, breed, 5)
        self.aggressive = True

    def rrrrr(self):
        print("stay away!")

class Puppy(Dog):

    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1)
        self.spoiled = True

    def woof_woof(self):
        print("Woof Woof!")


ruffus = Puppy(name="Ruffus", breed="Biggle")
bibi = GuardDog(name="Bibi", breed="Dalmatian")

ruffus.sleep()
bibi.sleep()
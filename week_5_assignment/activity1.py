# Assignment 1: Design Your Own Class! 

class phone:
    os = "IOS"
    name = "Iphone"
    type = "15 Pro"

    def ring(self):
        print("The Phone is Ringing...")

    def va(self):
        return "Hey Google"
    
# Create the object
phone1= phone()
print(phone.os)
print(phone.name)
print(phone.type)
phone1.ring()


class apple:

    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def va(self):
        return "Hey Siri"
  
apple1 =apple("blue", "Macbook", "2015")
apple2 = apple("Red", "Ipad", "2010")

print(apple1.color)

class Smartphone(apple):
    pass

phone2 = Smartphone("navy", "15promax", "2024")

print(phone2.model)

assist = [phone1,phone2, apple1]

for assistance in assist:
    print(assistance.va())

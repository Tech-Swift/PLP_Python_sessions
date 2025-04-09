# Assignment 1: Design Your Own Class! 

class phone:
    os = "IOS"
    name = "Iphone"
    type = "15 Pro"

    def ring(self):
        print("The Phone is Ringing...")
    
    def notification(self):
        print("A new notification is available...")

# Create the object
phone = phone()
print(phone.os)
print(phone.name)
print(phone.type)
phone.ring()


class apple:

    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
    
    def notification(self):
        return "You have a new notification"
        

    
apple1 =apple("blue", "Macbook", "2015")
apple2 = apple("Red", "Ipad", "2010")

print(apple1.color)

class phone(apple):
    pass

phone1 = phone("navy", "15promax", "2024")

print(phone1.model)

#polymorphism in action

for message in [apple1.notification(), apple2.notification(), phone1.notification()]:
    print(message)
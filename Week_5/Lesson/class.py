class Car:

    color = "red"
    model = "BMW"
    engine = "V8"

    #Method/behavior to display car details
    def drive(self):
        print("The car is driving")
    def stop(self):
            print("The car has stopped")


my_car = Car() # Create an instance of the class
my_car.drive() # Call the drive method
print(my_car.color) #Access the class attribute
print(my_car.model) #Access the model attribute


# print(my_car.color) #Access the color attribute

# self is just like a pointer which refrs to the instance of the class the method is in

# refers to the instance of the class and is used to access attributes and methods within the class.




class Person:
    # Construct a methoid to intiaze the object

    def __init__(self, name, age):
        self.name = name  #Instance variable for name
        self.age = age    #Instance variable for age

    def personDetails(self):
         print(f"Name: {self.name}, Age: {self.age}")

personDetails = Person("John", 30) # Create an instance of the Person class

personDetails.personDetails() # Call the personDetails method

 
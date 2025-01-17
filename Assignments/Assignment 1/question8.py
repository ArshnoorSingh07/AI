# A) Make a class called Restaurant. The __init__() method for Restaurant should store two 
# attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() 
# that prints these two pieces of information, and a method called open_restaurant() that prints a 
# message indicating that the restaurant is open. Make an instance called restaurant from your 
# class. Print the two attributes individually, and then call both methods. 
# B) Make a class called User. Create two attributes called first_name and last_name, and then 
# create several other attributes that are typically stored in a user profile. Make a method called 
# describe_user() that prints a summary of the user’s information. Make another method called 
# greet_user() that prints a personalized greeting to the user. Create several instances representing 
# different users, and call both method for each user.


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.name}, Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is open!")

restaurant = Restaurant("The Gourmet Spot", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()

class User:
    def __init__(self, first_name, last_name, **profile):
        self.first_name = first_name
        self.last_name = last_name
        self.profile = profile

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}, Profile: {self.profile}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

user1 = User("Alice", "Smith", age=30, location="New York")
user2 = User("Bob", "Johnson", age=25, location="Los Angeles")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

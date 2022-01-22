#A User class: This class creates a user from input. It sets a name, age, height, weight and the goal tha the user 
#wants to set in terms of dieting.

class User:

    def __init__(self):
        self.age = 0
        self.name = ""
        self.height = 0
        self.weight = 0
        self.goal = 0

    def get_name(self): 
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self,age): 
        self.age = age

    def get_height(self):
        return self.height

    def set_height(self, height): 
        self.height = height 

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight 

    def get_goal(self, goal):
        return self.goal
    
    def set_goal(self, goal):
        self.goal = goal

    def ask_name():
        name = input('What is your name?: ')
        return name 

    def ask_age():
        age = int(input('How old are you?: '))
        return age
        
    def ask_height():
        height = int(input('How tall are you in cm?: '))
        return height

    def ask_weight():
        weight = int(input('What is your weight in lbs?: '))
        return weight

    def ask_goal():
        print('These are the plans that we provide: ')
        print('1. Lose Weight')
        print('2. Gain Muscle') 
        goal = int(input('Please choose the option that better fits your goal 1 - 2: '))
        return goal
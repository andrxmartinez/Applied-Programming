import random
from user_class import User

# dieting program

print('''
oooooooooo.    o8o                .                                                                                    
`888'   `Y8b   `"'              .o8                                                                                    
 888      888 oooo   .ooooo.  .o888oo    oo.ooooo.  oooo d8b  .ooooo.   .oooooooo oooo d8b  .oooo.   ooo. .oo.  .oo.   
 888      888 `888  d88' `88b   888       888' `88b `888""8P d88' `88b 888' `88b  `888""8P `P  )88b  `888P"Y88bP"Y88b  
 888      888  888  888ooo888   888       888   888  888     888   888 888   888   888      .oP"888   888   888   888  
 888     d88'  888  888    .o   888 .     888   888  888     888   888 `88bod8P'   888     d8(  888   888   888   888  
o888bood8P'   o888o `Y8bod8P'   "888"     888bod8P' d888b    `Y8bod8P' `8oooooo.  d888b    `Y888""8o o888o o888o o888o 
                                          888                          d"     YD                                       
                                         o888o                         "Y88888P'                                       
                                                                                                                       ''')

print("------------------------------------------------------------------------------------------------------")
print("")

# this is a set of variables that will be used throughtout the program.

user = User()
#asks for user's name
name = User.ask_name()
#sets the name 
user.set_name(name)
#asks for user's age
age = User.ask_age()
#sets the user's age
user.set_age(age)
#asks the user's height
height = User.ask_height()
#sets the user's height
user.set_height(height)
#asks for the user's weight
weight = User.ask_weight()
#sets the user's weight
user.set_weight(weight)
#asks for a goal between 2 options
goal = User.ask_goal()
#sets a  goal between 2 options
user.set_goal(goal)

print("------------------------------------------------------------------------------------------------------")
print("")

#inputs the user's information into the console

print(f'HERE IS YOUR PROFILE INFORMATION: ')
print(f'name: {user.get_name()}')
print(f'age: {user.get_age()}')
print(f'height: {user.get_height()}')
print(f'weight: {user.get_weight()}')

    
if goal == 1:
        print('Looks like you are wanting to lose some weight. We have the right plan for you!')
elif goal == 2:
        print('You came to the right place! We are experts in helping people gain muscle.')
elif goal > 2:
        print ("Wrong selection. Please try again.")

print("------------------------------------------------------------------------------------------------------")

#lists containing meals for each of the two goals. 

breakfast1 = ["Oatmeal with chia Seeds", "Avocado Toast", "Peanut Butter rice cakes", "scrambled eggs", "Green Juice"]
breakfast2 = ["Protein Shake", "Boiled Eggs", "Chicken Omelette", "Banana Pancakes", "Smoked Salmon Bagel", "Greek Yogurt Pancakes"]
lunch1= ["Salmon Stuffed Avocado", "Kale Turkey Wrap", "Zucchini Noodles" "Tofu", "Curry Chicken Pita", "Avocado Egg Salad Sandwich"]
lunch2= ["Peanut Chicken Wrap", "Chicken breast salad", "Grilled Shrimp Tacos", "Cajun Chicken Alfredo", "Steak and bean burrito bowl"]
dinner1 = ["Pork Chops and Veggies", "Salmon and Asparagus", "Pesto Chicken", "Quinoa Salad", "Avocado Soup", "Quinoa Broccoli Casserole"]
dinner2 = ["Pees and Sesame Chicken", "Fetuccine Carbonara", "Steak and Baked Potatoes", "Chili",  "Veggies and Boiled eggs bowl"]

#def assign_breakfast(goal) takes a random meal from the breakfast lists and inputs it into the console.

def assign_breakfast(goal):
    if goal == 1:
        return random.choice(breakfast1)
    elif goal == 2:
        return random.choice(breakfast2)


breakfast_selection = assign_breakfast(goal)
print ("Breakfast menu:",breakfast_selection)

#def assign_lunch(goal) takes a random meal from the lunch lists and inputs it into the console.

def assign_lunch(goal):
    if goal == 1:
        return random.choice(lunch1)
    elif goal == 2:
        return random.choice(lunch2)


lunch_selection = assign_lunch(goal)
print ("Lunch menu:", lunch_selection)

#def assign_dinner(goal) takes a random meal from the dinner lists and inputs it into the console.

def assign_dinner(goal):
    if goal == 1:
        return random.choice(dinner1)
    elif goal == 2:
        return random.choice(dinner2)


dinner_selection = assign_dinner(goal)
print ("Dinner menu:",dinner_selection)





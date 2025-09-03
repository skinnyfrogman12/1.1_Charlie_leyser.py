'''
    author 
    date:25/08/2025
    varation 1 
    description fitness tracker 

'''



#--------functions---------
# To check how many pull up user has been doing 
# and tell them how strong they are.
# also add all total pull ups that user input and store in the list.
# loop the question 5 times if no error or no invalid number.


#-------libaries--------
user_name = str(input('Enter your name'))
age = int(input("Enter your age"))
pull_up = int(input("How many pull up have you done today"))

pull_up_result=[]

for i in range(5):
    result = int(input(f"Enter pull up result"))
    pull_up_result.append(result)

    print(f"Hi {user_name}")
    print(pull_up)

#-------main----------
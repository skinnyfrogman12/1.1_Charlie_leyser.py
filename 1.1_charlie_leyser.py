'''
    author 
    date:25/08/2025
    varation 1 
    description fitness tracker 

'''


#--------------main--------------
user_name = str(input('Enter your name'))
age = int(input("Enter your age")) #asks for user name and age




#--------functions---------
# To check how many pull up user has been doing 
# and tell them how strong they are.
# also add all total pull ups that user input and store in the list.
# loop the question 5 times if no error or no invalid number.

pull_up_result = [] #input will be stored in this list 

#loop the question for five times
for i in range(5):
    while True:
        pull_up = int(input("How many pull up have you done today")) #input how many pull-ups user did for today 
        pull_up_result.append(pull_up) #input variable will go into this list 

        if(pull_up >= 50):
            print("Nice!")

        else:
            print("You can do better ")

        break

    print(f'These are your pull up: {pull_up_result}') # list of all the users results    

average = sum(pull_up_result) / len(pull_up_result) #to find the average and print it 
print("average pull-ups:", round(average, 2))

best_result = max (pull_up_result) #find the max and print it 
print(f"Hi {user_name}")
print (f'Your best result is {best_result}')

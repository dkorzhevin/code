# start of program

types_of_people = 10 # assign 10 to variable
x = f"There are {types_of_people} types of people." # assign formatted string with integer variable inside to x variable

binary = "binary" # assign text to binary variable
do_not = "don't" # assign text to do_not variable
y = f"Those who know {binary} and those who {do_not}." # assign string with 2 text variable inside to variable y

print(x) # print variable x (string)
print(y) # print variable y (string)


print(f"I said: {x}") # print formatted string with x variable inside (formatted)
print(f"I also said: '{y}'")  # print formatted string with y variable inside (formatted)

hilarious = False # assign boolean False to variable hilarious
joke_evaluation = "Isn't that joke so funny?! {}" 

print(joke_evaluation.format(hilarious))

w = "This is the left side of..." # assign text string to w variable
e = "a string with a right side." # assign text string to e variable

print(w + e) # print variables w and e, + will add them togeather
def print_monthly_expense(month, hours):
    cost = hours * 0.65
    print("In " + month + " we spent: " + str(cost))

print_monthly_expense("June", 243)
print_monthly_expense("July", 325)
print_monthly_expense("August", 298)

# Old code before refactor below:

#june_hours = 243
#june_cost = june_hours * 0.65
#print("In June we spent: " + str(june_cost))

#july_hours = 325
#july_cost = july_hours * 0.65
#print("In July we spent: " + str(july_cost))

#august_hours = 298
#august_cost = august_hours * 0.65
#print("In August we spent: " + str(august_cost))
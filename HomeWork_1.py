# This is the first home work

# Separating a new task
print('***** Variables with Float *****')

# Create variables john_salary and marta_salary of some type (floating point). Assign the created variables the values you want.
# Print the values of both variables to the console using the print method.
john_salary = 100.55
marta_salary = 153.45

print(john_salary)
print(marta_salary)

print('John salary =', john_salary)
print('Marta salary =', marta_salary)
print('John salary =', john_salary, 'and', 'Marta salary =', marta_salary)

# Separating a new task
print('***** Variables with Int *****')

# Create variables john_age and marta_age of integer type. Assign the created variables the values you want.
# Print the values of both variables to the console using the print method.
john_age = 25
marta_age = 22

print('John age is', john_age)
print('Marta age is', marta_age)
print('John is', john_age, 'and', 'Marta is', marta_age)

# Separating a new task
print('***** Variables witn String *****')

# Create string type variables john_name and marta_name. Assign the created variables the values you want.
# Print the values of both variables to the console using the print method.
john_name = 'John Deer'
marta_name = 'Marta Sanchez'

print(john_name)
print(marta_name)

print('Guy name is' , john_name, 'and', 'his girlfriend is', marta_name)

# Separating a new task
print('***** Variables with Boolean *****')

# Create boolean variables john_gender and marta_gender. Let john be false and Marta be true.
# Print the values of both variables to the console using the print method.
john_gender = False
marta_gender = True

print(john_gender)
print(marta_gender)

if john_gender:
    print('John is a woman')
else:
    print('John is a man!')
    if marta_gender:
        print('Marta is a woman!')
    else:
        print('Marta is a man')

# Separating a new task
print('***** List type variables  *****')

# Create variables john_friends and marta_friends. Assign lists to variables. Each list must contain the names of friends.
# John has his list of friends and Martha has hers. Friends (friend's name) can be the usual strings "James", "Peter", etc.

john_friends = ["Peter Pen", "Vasyl", "Micki", "Vinni Pukh", "Micki", "Vasyl", "Serg"]
marta_friends = ["Victoria", "Lucy", "Kate", "Mary", "Linda", "Sarah", "Lucy", "Mary"]

print("John's friends", john_friends)
print("Marta's friends", marta_friends)

# Separating a new task
print('***** List type to Set type variables  *****')

# Create a list with people's names, some names should be repeated in it. Turn a list of duplicate names into a list of unique names using sets.

people_names = ["Peter", "Olga", "Mykola", "Vasyl", "Ivan", "Serhiy", "Ilona", "Roman", "Max", "Nastia", "Ivan", "Peter", "Vasyl"]

print("People's names are", people_names)
print("People's names are", set(people_names))

uniq_names = set(people_names)
print("List of unique names", uniq_names)

# define the lists
names = {
    "Tinus" : " ", 
    "Barrie" : " ", 
    "Hans" : " "
}

# length of the names
for name, snack in names.items():
    print(name)
    len_name = (len(name))
    print(f'The length of the name of {name} is {len_name} characters.')

    # ask each person personally what their favorite snack is
    names[name] = input(f'What is your favourite snack {name}? ')

    print(names)

for name, snack in names.items():
    print(f'{name} your favourite snack is {snack}')


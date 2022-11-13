#Display a menu of options
def print_menu():
    print('~ What would you like to do? ~')
    print(' 1. Add an item')
    print(' 2. Search')
    print('')
    print(' 3. EXIT (YES/NO)')
    print('[==================]')

#Allow users to select item in the menu (check if valid)
print_menu()
first_list = []
last_list = []
Age_list = []
address_list = []
number = []
entry_list = []
count = 0    

while count <= 100:
    menu_choice = int(input(' Choose Your Option:   '))

#Add an item
    if menu_choice == 1:
        print(' Add a Contact ')

#Users Input of Personal Information
        count = count + 1
        entry_list.append(count)
        print(' The Entry Number', count)

        first_list.append(input(' Enter your First Name: '))
        last_list.append(input(' Enter your Last Name: '))
        address_list.append(input(' Enter your Address: '))
        number.append(input(' Enter your Phone Number: '))
        Age_list.append(input('Enter your Age: '))
        print_menu()
#Search for a contact
    elif menu_choice == 2:

#Prompt the user to search
        print('~ Search ~')
        print('(1) Search by First Name?')
        choice = input (' Enter your choice ')
#Search the First Name
        if choice == '1':
            search_first = input('~ Search using the Full Name ~')     
            rep = []
            print('== RESULTS ==')
            for i in range (len(first_list)):
                if search_first in first_list[i]:
                    index = int(first_list.index(search_first))
                    rep.append(index)
                    print('Entry number', entry_list[i])
                    print('First Name', first_list[i])
                    print('Last Name', last_list[i])
                    print('Phone Number', number[i])
                    print('Address', address_list[i])
                    print('Age', Age_list[i])


                    if search_first not in first_list:
                        print(' It Does Not Exist ')

#Exit the Program
    elif menu_choice == 3:
        cont = input('EXIT (YES/NO)')
        if cont == 'YES':
            print('== Thank You for using Contact Tracing ==')
    else:
        cont == 'NO'
        print_menu()












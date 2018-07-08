list_names = []

def menu_list():
    print('1 - Add a new name to list')
    print('2 - Print list info')
    print('3 - Empty list of names')
    print('Q - Quit program')

def get_list_option():
    return input('Enter list option: ')

def get_name():
    return input('Enter the name: ')

def add_name_to_list(new_name):
    if len(new_name) == 0:
        return None
    else:
        list_names.append(new_name)
    return new_name


def empty_name_list():
    while len(list_names) > 0:
        list_names.pop()
    
    if len(list_names) == 0:
        print('name list is empty now!')

def list_name_list_info():
    
    print('*'*40)
    print("names in list")
    for name in list_names:
        print('name: ' + name + ' length: ' + str(len(name)))
    
    print()
    print('Names longer than 5 characteres')
    for name in list_names:
        if len(name) > 5:
            print('name: ' + name)

    print()
    print("Names with 'n' or 'N'")
    for name in list_names:
        for char in name:
            if char == 'n' or char == 'N':
                print("name " + name + " as a 'n' or 'N'")
                break
    print('*'*40)


continue_loop = True

while continue_loop:
    menu_list()
    list_option = str(get_list_option())

    if  list_option == '1':
        name_added = add_name_to_list(get_name())
        if name_added != None:
            print('name ' + name_added + ' added!')
        else:
            print('name is empty!')
    elif list_option == '2':
        list_name_list_info()
    elif list_option == '3':
        empty_name_list()
    elif list_option == 'q' or list_option == 'Q':
        continue_loop = False
    else:
        print('Option not valid!')
        continue
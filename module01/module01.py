name = ""
age = -1

def get_user_data():
    global name
    global age
    name = input("Insert your name: ")
    age = int(input("Insert your age: "))


def print_user_info():
    print("Name: " + name + " Age: " + str(age))


def print_info(user_name,user_age):
    print("Name: " + user_name + " Age: " + str(user_age))


def calc_num_decades(age):
    return age//10

get_user_data()
print_user_info()
print_info(name, age)

print(name + " already lived " + str(calc_num_decades(age)) + " decades")
# Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
def sum_function(a, b):
    return str(a + b)

def exec_function(fction, a, b):
    print('function result: ' + fction(a,b))

exec_function(sum_function,2,5)

# Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
def exec_function(fction, a, b):
    print('function with lambda result: ' + fction(a,b))

exec_function(lambda a,b: str(a+b),5,5)

# Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.
# Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.
def exec_function(fction, *args):
    sum = 0
    if len(args) > 0:
        for arg in args:
            sum = fction(sum,arg)

    print('function result with args: {value:^20.02f}'.format(value=sum))
ß
exec_function(lambda sum,value: sum+value,1,2,3,4,5)


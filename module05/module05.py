# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
from random import random, randint
from datetime import datetime, date

# random number between 0 and 1
print('random between [0 , 1[ ' + str(random()))
# random number between 1 and 10
print('random between [1 , 10[ ' + str(random()*9 + 1))

# 2) Use the datetime library together with the random number to generate a random, unique value.
unique_value = str(randint(0,date.toordinal(date.today()))) + '-' + datetime.now().isoformat()
print('unique_value: ' + unique_value)
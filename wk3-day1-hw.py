
### Exercise #1 <br>
# <p > Filter out all of the empty strings from the list below < /p >

# places = [' ', 'Argentina', '  ', 'San Diego',
#           '', '   ', '', 'Boston', 'New York']
# = [Argentina, San Diego, Boston, New York]

# HINT: LOOK FOR A STRING METHOD THAT REMOVES WHITESPACE

# def remove_whitespace(str):
#     x = str.strip()
#     return x

# result = filter(remove_whitespace, places)

# for each in result:
#     print(each)


# result = list(filter(lambda str: str.strip(), places))
# print(result)


### Exercise #2 <br>
# <p >Write an anonymous function that sorts this list by the last name...<br><b>Hint: Use the ".sort()" method and access the key"</b></p>

# .sort(key=)

authors = ["Connor Milliken", "Victor aNisimov",
           "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

# HINT: YOU'LL NEED TO CONVERT EACH PERSON'S NAME (A STRING) INTO A LIST IN ORDER TO GRAB THE LAST NAME BY
# THE INDEX
def takeLast(elem):
    return elem[-1].lower()


def func():
    new_list = [each.split(' ') for each in authors]
    print(new_list)
    new_list.sort(key=takeLast)
    print(new_list)

func()





### Exercise #3 <br>
# <p >Convert the list below from Celsius to Farhenheit, using the map function with a lambda...</p>

places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]

# HINT: KEEP IN MIND PEMDAS. USE THE CELCIUS - FAHRENHEIT CONVERSION
# F = C * 9/5 + 32


# fahr = [each[1] for each in places]

# def celcius(n):
#     return n * 9/5 + 32

# cel = list(map(celcius, fahr))
# print(list(cel))
# updated_places = []
# for num in range(len(places)):
#     updated_places.append((places[num][0], cel[num]))
# print(updated_places)



### Exercise #4 <br>
# <p >Write a recursive function to perform the fibonacci sequence up to the number passed in.</p>

# def fib(n):
#     series = [0, 1]
#     if n == 0:
#         return 0
#     elif n == 1: 
#         return 1
#     else:
#         for num in range(2, n+1):
#             series.append(series[num-2]+series[num-1])
#     print(sum(series))
#     return sum(series)

# fib(6)
# Write a Python function that takes a name as an argument
# and prints that name

def name(name):
    return name
segun = name("segun")
print(segun)

'''Write a Python function that takes a string as an argument
and prints whether it is upper- or lowercase.'''

def string(check):
    if check.isupper() == True:
        print("this is uppercase")
    elif check.islower() == True:
        print(" This is a lowercase")
    return

upper = string("segun")

'''Write a list comprehension that results in a list of every letter
in the word smogtether capitalized.'''

list = ['watermelon is good', 'mango is not so good', 'apple is the best', 'pineapple, i like it average']
word = 'smogtether'

compre = [x for x in word.upper()]

print(compre)


'''Write a generator that alternates between returning Even and
Odd.'''

def alternating_numbers():
    even = True
    num = 0
    while True:
        if even:
            yield num
            even = False
        else:
            yield num + 1
            even = True
            num += 1



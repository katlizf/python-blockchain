#Create two variables - one with your name and one with your age. Can also practice asking the user for their name and age.
name = 'Katie '
age = 24

user_name = input('Enter your name: ')
user_age = input('Enter your age: ')

#Create a function which prints your data as one string.
def print_info():
    """Prints the user name (uses global variables)."""
    print(user_name + ' ' + user_age)


print_info()


#Create a function which prints ANY data (two arguments) as one string.
def concatenate_info(a, b):
    """Print two concatonated strings.
    
    Arguments:
        :param a: The first string to be concatonated.
        :param b: The second string to be concatonated.
    """
    print(a + b)


concatenate_info(user_name, user_age)


#Create a function which calculates and returns the number of decades your are old.
def calculate_age(age):
    """Calculates the integer part of the age received.
    
    Arguments:
        :param age: The age for which the decades should be calculated.
    Returns: the decades lived.
    """
    decades = age//10
    return decades


decades_lived = calculate_age(int(user_age))
print(decades_lived)


#Create a list of names and use a loop to output the length of each name (leng()).
names = ['Katie', 'John', 'Alexandra', 'Bob', 'Catherine']

for name in names:
    print(len(name))


#Add an if check inside the loop to only output naames longer than 5 characters. Add a check to see whether a name includes a "n" or "N" character. Use a while loop to empty the list of names (via pop()).
for name in names:
    if len(name) > 5 and ("n" in name or "N" in name):
        print (name)
while len(names) >= 1:
    names.pop()

print(names)


#Create a list of "person" dictionaries with a name, age and list of hobbies for each person.
persons = [{'name': 'Katie', 'age': 34, 'hobbies': ['walking', 'cooking']}, {'name': 'John', 'age': 28, 'hobbies': ['reading', 'gaming']}, {'name': 'Sarah', 'age': 22, 'hobbies': ['painting', 'dancing']}]


#Use a list comprehension to convert this list of persons into a list of names.
person_names = [person['name'] for person in persons]


#Use a list comprehension to check whether all persons are older than 20.
all([person['age'] > 20 for person in persons])


#Copy a person list such that you can safely edit the name of the first person (without changing the original list).
copied_person_list = [person.copy() for person in persons]

# Unpack the persons of the original list into different variables and output these variables.
person1, person2, person3 = persons
print(person1)
print(person2)
print(person3)
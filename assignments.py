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
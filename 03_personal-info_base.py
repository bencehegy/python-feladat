"""
Write code to get output below:

What is your first name? First
What is your last name? Last
What is your location? Texas
What is your age? 54
Hi First Last! Your location is Texas and you are 54 years old.
>>>
"""

first = input('Mi a vezetékneved? ')
last = input('Mi a keresztneved? ')
location = input('Hol van a lakhelyed? ')
age = int(input('Mennyi idős vagy? '))
print("Üdvözlöm", first, last, "!" "A lakhelyed", location, "és",age, "éves vagy.")
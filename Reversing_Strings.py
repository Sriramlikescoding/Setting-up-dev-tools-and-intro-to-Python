string = input("Enter a string to be reversed: ")

string2 = ''

for i in string:
    string2 = i + string2

print("\n Your Original String", string)
print("\n Your String Reversed", string2)
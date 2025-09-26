# TAKE AN INPUT FROM USER AS A STIRNG THEN REVERSE IT

a = input("ENTER THE STRING  : ")
print(a[::-1])

# WAP TO CHECK IF A STRING CONTAINS ONLY DIGITS

b = input("enter the string : ")
print(b.isdigit())

if b == True:
    print("it contins only digits ")
else:
    print("it contains letters not only digits ")

# WAP TO CHECK THE STRING IS PALINDROME OR NOT

user = input("enter the string to check palindrome : ")
rev = user[::-1]

if rev == user:
    print("the string is palindrome ")
else:
    print("the string is not palindrome")

# WAP TO FIND NUMBER OF VOWELS IN A STRING

c = input("enter the string : ").lower()
vowels = 0

for i in c:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowels += 1
print("the number of vowels in the string are : " , vowels)

# WAP TO CHECK IF EVERY FIRST LETTER OF THE WORD IN A STRING IS CAPITALIZED OR NOT

d = input("ENTER THE TITLE HERE : ")
cap = d.istitle()

if cap:
    print("THE TITLE IS PERFECT ")
else:
    print("It should be a proper title , the first letter of every wword should be on capital ")




#A python program that checks whether a number is even or old

num =int(input("Enter a number :"))

if num % 2 ==0:
    print(num, "is even number")

else:
    print(num, "is odd number")



#A python program that checks whether a letter is a vowel or consonant

letter = input("Enter a letter :").lower()
if letter.isalpha() and len(letter)==1:
    if letter in  "aeiou":
        print("vowel")
    else:
      print("consonant")
else:
    print("invalid input")







#A python program that returns the perimeter of a rectangle

length = float(input("Enter the length of a rectangle :"))
width = float(input("Enter the with of a rectangle :"))

perimeter = 2* (length + width)
print("The perimeter of the triangle is", perimeter)
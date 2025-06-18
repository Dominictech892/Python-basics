#program

age = int(input("How old are you?"))

if age > 18:
    print("You are a voter")
else:
    print("You are not a voter")

#program2
temperature = float(input("Enter current temperature;"))

if temperature >25.0:
    print("It is too hot")
elif temperature < 25.0:
    print("It is too cold")
else:
    print("normal temperature")

print()


#program3
first = int(input("Enter first number"))
second = int(input("Enter secnd nunmber"))
third = int(input("Enter third nunmber"))


if first>second and first>third:
    print(first, "Is the largrst number")

elif second>first and second>third:
    print(second, "Is the largest number")

else:
    print(third, "Is the largest number")



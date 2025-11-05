# -------- Assignment 1, 2, 3, 4, 5 --------
# print this --> "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt

name = "Nada"
age = 23
country = "Egypt"
print(
    f"\"Hello '{name}', How You Doing \\ "
    + '"""'
    + f' Your Age Is "{age}"" + And Your Country Is: {country}'
)

print(
    f"\"Hello '{name}', How You Doing \\\n"
    + '"""'
    + f' Your Age Is "{age}"" +\nAnd Your Country Is: {country}'
)

name = "Elzero"
# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"

print(
    "Second Letter Is {}\nThird Letter Is {}\nLast Letter Is {}".format(
        name[1], name[2], name[-1]
    )
)

# Needed Output
# "lze"
# "Ezr"
# "rzE"
print(
    "Second Letter Is {}\nThird Letter Is {}\nLast Letter Is {}".format(
        name[1:4], name[0:5:2], name[len(name) - 2 :: -2]
    )
)

name = "#@#@Elzero#@#@"
print(name.strip("#@"))

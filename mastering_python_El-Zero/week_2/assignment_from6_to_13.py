# --------------------- Assignment 6 ---------------------
num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))

# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500

# --------------------- Assignment 7 ---------------------
name_one = "Osama"
name_two = "Osama_Elzero"

# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero

print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

# --------------------- Assignment 8 ---------------------
name_one = "OSamA"
name_two = "osaMA"

# Needed Output
# osAMa
# OSAma

print(name_one.swapcase())
print(name_two.swapcase())

# --------------------- Assignment 9 ---------------------
msg = "I Love Python And Although Love Elzero Web School"

# Needed Output
# 2
print(msg.count("Love"))

# --------------------- Assignment 10 ---------------------

name = "Elzero"
# Needed Output
# 2
print(name.find("z"))

# --------------------- Assignment 11,12 ---------------------
msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although <3 Elzero Web School

print(msg.replace("<3", "Love", 1))
print(msg.replace("<3", "Love"))

# --------------------- Assignment 13 ---------------------
name = "Osama"
age = 38
country = "Egypt"

# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")

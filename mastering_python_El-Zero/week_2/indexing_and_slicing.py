# -----------  indexing (access single item) ----------#
mystring = "I Love Python"

print("------------------Indexing------------------")
print(mystring[0])  # first char.
length = len(mystring)
# print(type(length))
print(mystring[-length])
print(mystring[-1])  # first char. from end

# -----------  slicing (access multiple item) ----------#
print("------------------Slicing------------------")
print(mystring[8:11])  # yth -- end is not included
print(mystring[:10])  # when start is not included, it will start from 0
print(mystring[5:])  # will print from start till end
print(mystring[:])  # full string
print("------------------trying using steps--------------------")
print(mystring[0:length:1])  # full string
print(mystring[0:length:2])  # ILv yhn
print(mystring[::3])  # Io tn

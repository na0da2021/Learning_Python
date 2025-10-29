# index(substr, start, end) --> not accessing it is searching

a = "I Love Python"
print(a.index("P"))
print(a.index("P", 0, 8))
# print(a.index("P", 0, 5))  # Throgh Error و هيوقف اللاينز اللي بعده مش هيكمل

# find(substr, start, end
b = "I Love Python"
print(b.find("P"))
print(b.find("P", 0, 8))

print(b.find("P", 0, 5))  # -1
# print("code is still running")

# rjust() and ljust()
name = "Nada"
print(name.rjust(10, "%"))
print(name.ljust(10, "%"))


# splitlines()
n = """1st line
2nd line
3rd line"""
print(n)
print(n.splitlines())

c = "1st line \n2nd line \n3rd line"
print(c)
print(c.splitlines())

# expandtabs
st = "my\tname\tis\tNada\tand\ti\tam\t23\tyears\told"
print(st)
print(st.expandtabs(1))
print(st.expandtabs(10))

one = "nada"
two = "nada_100"
three = "nada--100"

print(one.isidentifier())
print(two.isidentifier())
print(three.isidentifier())  # false --> can not be a variable name

x = "AaaaBbbbb"
y = "AaaaBbbbb1234"

print("\n" + str(x.isalpha()))
print(y.isalpha())

print(x.isalnum())
print(y.isalnum())

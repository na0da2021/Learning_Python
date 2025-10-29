# strip()  # remove spaces from right and left
# rstrip() # remove spaces from right
# lstrip() # remove spaces from left

a = "            I love python            "
print(a)
print(a.strip())
print(a.rstrip())
print(a.lstrip())

b = "#### I love # python ####"
print("new b :" + b.strip("#"))

# title() and capitalize()
c = "I love Python and 2d graphics and 3g Technology"
print(c.title())
print(c.capitalize())  # لاحظ الفرق في الحروف اللي بعد الأرقام

# zfill(full size of returnd numeric strings)

a = "5"
b = "66"
c = "1000"

print(a + " --> " + a.zfill(4))
print(b + " --> " + b.zfill(4))
print(c + " --> " + c.zfill(4))

# upper()
name = "nada"
print(name.upper())

# lower()
name = "NADA"
print(name.lower())

# swapcase() # upper to lower and lower to upper
n = "nada"
e = "RITAJ"
f = "AHMed"

print(n.swapcase())
print(e.swapcase())
print(f.swapcase())

# split
q = "i love python, css and php"
print(q.split())  # spliter is white space by default
print("length:" + str(len(q.split())))

r = "i-love-python,-css-and-php"
print(r.split("-"))  # splitter here is "-"
print("length:" + str(len(r.split("-"))))

s = "i-love-python,-css-and-php"
print(s.split("-", 2))  # splitter here is "-", maxsplit = 2
print("length:" + str(len(s.split("-", 2))))

s = "i-love-python,-css-and-php"
print(s.rsplit("-", 2))  # splitter here is "-", maxsplit = 2
print("length:" + str(len(s.rsplit("-", 2))))

# center
name = "Nada"
print(name.center(len(name) + 10, "#"))

# count  #--------case sensetive--------
stringg = (
    "I love python and PHP because python and PHP are super easy and very interesting"
)
print(stringg.count("PHP", 0, len(stringg)))
print(stringg.count("php"))  # case sensetive


# startswith()
i = "I love python"
print(i.startswith("i"))
print(i.startswith("I"))  # case sensetive
print(i.startswith("p", 7, 13))

# endswith()
i = "I love python"
print(i.endswith("n"))
print(i.endswith("e", 2, 6))

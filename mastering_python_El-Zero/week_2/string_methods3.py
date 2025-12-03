# replace(old value, new value, count)

a = "Hello one two three one one on on"

print(a.replace("one", "1", 3))

# join(Iterable{tuple or list})
mylist = ["Nada", "Mohamed", "Ahmed", "Mohamed", "Omar"]
print("-".join(mylist))
print("".join(mylist))
print(", ".join(mylist))
print(type(", ".join(mylist)))

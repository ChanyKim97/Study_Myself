my_dictionary = {
    5: 25,
    3: 9,
    2: 4
}

print(type(my_dictionary))

print(my_dictionary[3])

my_dictionary[9] = 81

print(my_dictionary)

my_family = {
    "mom": "Yoon"
}

print(my_family["mom"])

print(my_dictionary.values())
print(my_dictionary.keys())

for key, value in my_dictionary.items():
    print(key, value)

name = "Hine"

list = list(name)
name2 = str(list)
print(name2)
print(len(name))
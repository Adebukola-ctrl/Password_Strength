## Types of differnrt Values

print(type(167))
print(type("Adebukola"))
print(type(100.44))
print(type(False))
print(type(2+3j))

## Basic arithmatic Operators
print(10+21)
print(29.5+3.6)
print(55-41)
print(77/11)
print(4**4)
print(15//4)
print(23%5)

## Conversion between Int and Float

a = 4
print(float(a))
b = 23.005
print(int(b))

## Texts Manipulation

Text = "I want to be a Data Scientist"
print(Text.upper())
print(Text.capitalize())
print(Text.lower())
print(Text.replace(" ", "."))

## Strings Formatting

Name = "Folashade"
Age = 23
Relationship = "Sister"
print("Her name is {}, she is {} years old and she is my {}.". format(Name, Age, Relationship))
print(f"Her name is {Name}, she is {Age} years old and she is my {Relationship}.")

## List (indexing, slicing and list operstions)
My_list = ["Books", "Pens", "Pencils", "Erasers", "Calculator"]
print(My_list[0])
print(My_list[2:4])
print(My_list[-4])
print(My_list[0:5:2])
print(My_list.append("Crayons"))
print(My_list)
others = ["Ruler", "Marker"]
print(My_list.append(others))
print(My_list)
print(My_list.remove(others))
print(My_list)
print(My_list.pop(3))
print(My_list)
print(My_list.sort())
print(My_list)
print(My_list.sort(reverse=True))
print(My_list)
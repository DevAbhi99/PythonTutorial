#Functions for strings in python are:- 

s="hi man"

#1)len :- Find length of a string 

print(len(s))

#2)endswith("substring") :- To check if a given string ends with a substring

print(s.endswith("man"))

#3) find("substring") :- To find a substring

print(s.find("man"))


#4) replace("old",new) :- replace old substring with a new string

s.replace("hi","hey")

print(s)

#5) capitalize() :- capitalizes a string

print(s.capitalize())


#6) slicing() :- the concept of slicing in python strings is similar to that of arrays

#I want to fetch ma from "hi man"

print(s[3:5])

#7) concat() :- the concept of adding multiple strings is known as concatenation

print("hi"+" bro"+" hey")
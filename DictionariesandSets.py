karan={
"age":21,
"skills":["Python","Javascript","C"],
"role":{
    "software":["React.js","Express.js","Node.js","MySql","ML"],
    "hardware":["IOT","Arduino","Wireless Network"]
}

}


print(karan)

print(karan["age"])

print(karan["role"]["software"])


#Updating data in a dictionary

karan.update({"degree":["Computer Science Engineer","Electronics Engineer"]})

print(karan)


#Sets: Sets is a collection that stores unique values 


sets={1,2,2,3,4}

print(sets)

#add :- add specified element

sets.add(5)

print(sets)


#remove :- remove specified element

sets.remove(1)

print(sets)

#pop :- removes random element

sets.pop()

print(sets)

#clear :- clears the entire set

sets.clear()

print(sets)

#Create a new empty set


nsets=set()

print(nsets)

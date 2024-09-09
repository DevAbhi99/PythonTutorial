arr=[1,2,3,4,5]

print(arr)

#Functions of arrays

#1) Append() :- Add elements 

arr.append(6)

print(arr)


#2) changing value in arrays

arr[1]="hi"

print(arr)

#3) pop(index) :- removes element on the basis of index provided

arr.pop(0)

print(arr)



arr1=[5,4,3,2,1]

#4) sort():- sort an array in ascending order


print(arr1.sort())


#5) sort(reverse=true) :- sort in the array in descending order

print(arr1.sort(reverse=True))


#6) reverse() :- reverse the array


#print(arr1.reverse())


#7) slicing() using positive indices :-


print(arr1[1:3])


#8) insert(index, element) :- insert an element at any index

arr1.insert(2,"man")

print(arr1)



#Tuples :- These are data structures just like arrays but unlike arrays tuples are immutable  which cannot be changed

tuples=(1,2,2,3,4,5,6)

print(tuples)

#Tuple functions

#1) index(element) :- to find the index of an element

print(tuples.index(2))


#2) count(element) :- to find the index of an element

print(tuples.count(2))








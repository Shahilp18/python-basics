word = "python"

print(len(word)) #? Length

print(word[2:4]) #? indexing

a = 5
b = 10
sum = a + b

#? NORMAL FORMATTING
print("Sum is {}".format(sum))
print("Sum of {} and {} is {}".format(a, b, sum));

#? INDEX BASED FORMATTING
print("Sum of {1} and {0} is {2}".format(a, b, sum));

#? VALUE BASED FORMATTING
print("values of vars {a} and {b}".format(a=5, b=10));

#! F-strings
name = "Rahul"
age = 33
print(f"Cricker is {name} and age is {age}")

#! Lists
marks = [10,20,30,40,50]

marks[1] = 200
print(marks)

#? Methods of LISTS
val = [1,2,3]
val.append(4) 
print(val)

val.insert(0, 3000)
print(val)

val.sort()
print(val)

val.reverse()
print(val)

#? Loops in Lists

nums = [1,2,3,4,5]
x = 4
idx = 0
for val in nums:
    if(val == x):
        print(f"Val found at idx {idx}")
        break;
    idx+=1
    
#! TUPLES
tup = (1,2,3,4,5)
print(tup)

#? Methods in Tuples
t = [1,2,3,4,5]
print(t.count(1))

#! Dictionary
info =  {
    "name": "Shahil Patel",
    "age":  20 ,
}
print(info)

#? Methods in Dictionary
print(info.keys())
print(info.values())
print(info.items())
print(info.get("name"))
print(info.update({
    "city": "HMT"
}))

#! Sets
#? Methods of Sets

set = {1,2,3,4,5}

set.add(22)
print(set)

set.remove(22)
print(set)

set.clear()
print(set)

# set.pop()
# print(set)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))

print(s1.intersection(s2))



 
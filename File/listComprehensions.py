
#! List Comprehensions
#* [output for item in iterable if condition]

sq = [i*i for i in range(6)]
print(sq)

#* conditional
sq2 = [i*i for i in range(6) if i%2 !=0]
print(sq2)
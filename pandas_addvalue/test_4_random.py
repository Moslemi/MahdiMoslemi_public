import random

#if DeltaH max >1
A = [1,2,3,4,5,6,7,8]
#length = len(A)

A.remove(max(A))
A.remove(min(A))

random.shuffle(A)
print (A[:6])

# for checking convergence when we find the Delta h Max if DeltaH max is more than 2 less than 5 f.write("2")
## then shuffle the list A
### then select "2" of the list A
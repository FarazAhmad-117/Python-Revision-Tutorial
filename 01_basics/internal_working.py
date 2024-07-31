
a = "Ali"
b = a
a *= 3

# print(b)
# import sys
# print(sys.getrefcount(2114602))
# print(sys.getrefcount('h'))

# Exception


# a = [1,2,3,4]
# b = a[:] # Way to copy
# b[3] = 55
# print(a)
# print(b)


# l1 = [1,2,3,[1,2,3,4]]
# l2 = l1[:]

# l1[3][0] = 44
# l1[0] = 55
# print(l1) # [55, 2, 3, [44, 2, 3, 4]]
# print(l2) # [1, 2, 3, [44, 2, 3, 4]]


# import copy as c

# l1 = [1,2,3,[1,2,3,[1,2,3]]]
# l2 = c.deepcopy(l1)

# l1[3][3][0] = 55
# l1[3][0] = 44

# print(l1)
# print(l2)


# m = [1,2,3]
# n = [1,2,3]

# print(m == n)
# print(m is n) # Memory Referance











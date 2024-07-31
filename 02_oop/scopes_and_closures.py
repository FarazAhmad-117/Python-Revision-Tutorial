# Scopes and Closures -- > 

# print("Finally Learning Scopes and Closures!")

# username = "Faraz Ahmad"

# print(username)


# ali = username

# username = "ahmad"

# print(ali)


# username = "Faraz Ahmad"


# def test():
#     username = "Ali Ahmad"
#     print(username)


# test()
# print(username)


################################################################################


# username = "Faraz Ahmad"

# def test(prop):
#     prop['username'] = "Ali Ahmad"

# data = {'username':username}

# print(data['username'])
# test(data)
# print(username)
# print(data['username'])



###################################################################################



# username = "Faraz Ahmad"


# def test():
#     print(username)


# test()

# username = "Ali Ahmad"



# x=99

# def fun():
#     global x
#     x = 12
    
# print(x)
# fun()
# print(x)



# x = 99

# def fun():
#     x = 13    # How can I change it??
#     def fun2():
#         global x
#         x = 12
#     fun2()


# print(x)
# fun()
# print(x)





# x = 99

# def fun():
#     x = 13    # How can I change it??
#     def fun2():
#         nonlocal x   # This will change nearest scoped variable
#         x = 12
#     fun2()
    
#     print(x)


# print(x)
# fun()
# print(x)


######################################################

# CLOSURE -> NOT ONLY GOES DEFINATION BUT ALSO ALL VARIABLES

# x =99

# def fun():
#     x = 88
#     def f2():
#         print(x)
#     return f2

# res = fun()

# print(x)
# res()


# def f1(num):
#     def f2(x):
#         print(x ** num)
#     return f2

# pow2 = f1(2)  # Making a function that gives power of 2
# pow3 = f1(3)

# pow2(3)
# pow3(3)

# ALSO KNOWN AS FACTORY FUNCTIONS  -->> MOSTLY USED in DJango

######################################################################3
















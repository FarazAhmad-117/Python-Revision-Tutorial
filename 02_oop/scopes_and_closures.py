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


















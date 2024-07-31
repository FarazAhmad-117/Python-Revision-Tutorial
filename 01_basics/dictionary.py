#  A Breif intro on Dictionary

# Used mod=st of the times
# e.g. NoSQL Databases in MongoDB

friends = {
    "first":"Faraz Ahmad",
    "second":"Hashir Azeez",
    "third":"Rehan Rasheed"
}

friends["forth"] = "Rana Mubashir"
friends["fifth"] = "Zubair Khan"


# print(friends["sixth"]) # Produce Error
# print(friends.get("sixth")) # Replied None

# for f in friends:
#     print(f,'\t',friends[f])

print('Hello G!')


# for (k,v) in friends.items():
#     print(k,'\t',v)


# for k,v in friends.items():
#     print(k,'\t',v)


# if "Faraz Ahmad" in friends:
#     print("Yes Faraz is a friend")
# else:
#     print("No he is not a friend")


# if "first" in friends:
#     print(f"Yes {friends["first"]} is a friend")
# else:
#     print("No he is not a friend")


# print(len(friends))  # 5

# friends.pop("forth") # Actuall removed
# print(friends)


# print(friends.popitem()) # Zubair Khan
# print(type(friends.popitem())) # class tuple


# del friends["second"]
# print(friends)


# a = friends
# a["first"] = "Whi Bhai Ab usse baat na kri Demotivated feel kr rha ha na"
# print(friends)


# a = friends.copy()  #Shalow copy
# a['first'] = "Ab wapis track pe ana pre ga"
# print(friends) 


person = {
    "name":{
        "first":"Hafiz",
        "last":"Ahmad"
        },
    "age":20,
    "friends":friends
}

# person2 = person.copy()
# person["age"] = 45 # Not reflected
# person["friends"]["first"] = "Ahmad Ameen" # reflected

# import copy as c

# person2 = c.deepcopy(person)
# person["age"] = 45 # Not reflected
# person["friends"]["first"] = "Ahmad Ameen" # Not reflected

# print(person2)


# squared_dict = {x:x**2 for x in range(1,11)}
# print(squared_dict)

# keys = ["first","second","thrid","nothing"]
# default_val = "Somthing Useful"

# new_dict = dict.fromkeys(keys,default_val)
# print(new_dict)


# keys = ["first","second","thrid","nothing"]
# default_val = "Somthing Useful"
# new_dict = dict.fromkeys(keys,keys)
# print(new_dict)

















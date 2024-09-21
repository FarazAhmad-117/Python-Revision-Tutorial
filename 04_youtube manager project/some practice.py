# lst = ("Apple", "Mango", "Banana")
# y = enumerate(lst)
# print(y)

# print(list(y))


# file = open("./youtube.txt", "w")

# try:
#     file.write("chai aur code")

# except FileExistsError:
#     print("File already exists")

# finally:
#     file.close()


with open("youtube.txt", "w") as file:
    file.write("chai aur python")

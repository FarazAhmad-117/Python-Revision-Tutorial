import requests as req


url_header = "https://api.freeapi.app/api/v1"


users = req.get(f"{url_header}/public/randomusers")


if users.status_code == 200:
    data = users.json()
    data = data.get("data")  # Extracting the data object out of it
    if data == None:
        print("Data not found")
        exit()
    else:
        userList = data.get("data")
        if userList is not None:
            for idx, user in enumerate(userList, start=1):
                userName = f"{user['name']['first']} {user['name']['last']}"
                age = user["dob"]["age"]
                print(f"{idx}. {userName} is {age} years of his age")

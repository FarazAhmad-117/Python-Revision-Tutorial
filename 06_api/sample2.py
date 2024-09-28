import requests as req


url_header = "https://api.freeapi.app/api/v1"


def get_random_data():
    url = f"{url_header}/public/randomusers/user/random"

    resp = req.get(url)

    data = resp.json()

    # if resp.get("data") == None:
    #     print("Unable to fetch data from API.")
    #     return
    # else:
    #     user_data = resp["data"]
    #     print(f"Name: {user_data['name']['first']} {user_data['name']['last']}")
    #     print(f"Email: {user_data['email']}")
    #     print(f"Phone: {user_data['phone']}")
    #     print(
    #         f"Address: {user_data['location']['street']}, {user_data['location']['city']}, {user_data['location']['state']}, {user_data['location']['country']}"
    #     )
    #     print(f"Birthday: {user_data['dob']['date'].split('T')[0]}")

    if data["success"] and "data" in data:
        # Now it confirmed that the reponse has came:
        user_data = data["data"]
        print(f"Name: {user_data['name']['first']} {user_data['name']['last']}")
        print(f"Email: {user_data['email']}")
        print(f"Phone: {user_data['phone']}")
        print(
            f"Address: {user_data['location']['street']}, {user_data['location']['city']}, {user_data['location']['state']}, {user_data['location']['country']}"
        )
        print(f"Birthday: {user_data['dob']['date'].split('T')[0]}")
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        get_random_data()
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        exit()


if __name__ == "__main__":
    main()

import requests as req


url = "https://api.chucknorris.io/jokes/random"


def get_new_jokes():
    resp = req.get(url)
    if resp.status_code == 200:
        resp = resp.json()
        joke = resp.get("value")
        joke = str(joke).replace("Chuck Norris", "Rana")
        print(f"Joke: =====>>>>>   {joke}")
    else:
        raise Exception("Failed to fetch Error")


def main():
    try:
        while True:
            get_new_jokes()
            any_more = input("Press n/N to exit")
            if any_more.lower() == "n":
                exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()


if __name__ == "__main__":
    main()

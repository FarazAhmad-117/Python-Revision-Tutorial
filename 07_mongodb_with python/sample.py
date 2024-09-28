from pymongo import MongoClient
from os import system
from bson.objectid import ObjectId

db_url = "mongodb://localhost:27017/youtube"


client = MongoClient("localhost", 27017)

db = client["youtube"]

video_collection = db["videos"]

print(video_collection)


def list_videos():
    for video in video_collection.find():
        print(video)


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def update_video(id, name, time):
    video_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": {"name": name, "time": time}}
    )


def delete_video(id):
    video_collection.delete_one({"_id": ObjectId(id)})


def main():
    while True:
        system("cls")
        print("Welcome to Youtube Manager!")
        print("1- List all videos")
        print("2- Add a video")
        print("3- Update a video details")
        print("4- Delete a video")
        print("5- Exit the app")
        opt = input("Choose your option: ")

        match opt:
            case "1":
                list_videos()
            case "2":
                name = input("Enter name of video: ")
                time = input("Enter time of video: ")
                add_video(name, time)
            case "3":
                id = input("Enter id of video: ")
                name = input("Enter name of video: ")
                time = input("Enter time of video: ")
                update_video(id, name, time)
            case "4":
                id = input("Enter id of video: ")
                delete_video(id)
            case "5":
                print("Exiting the app...")
                exit()
            case _:
                print("Invalid option. Please try again.")
                continue

        input("Press enter to continue....")


if __name__ == "__main__":
    main()


# TODO : Just make a complete DJANGO  APP

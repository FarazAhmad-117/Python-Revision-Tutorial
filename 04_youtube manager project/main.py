# Just a raw program
import json
import os


def clear_console():
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For Linux and macOS
        os.system("clear")


FILE_NAME = "youtube.txt"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open(FILE_NAME, "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    for idx, a in enumerate(videos, start=1):
        print(f"{idx}. Video Name: {a['name']}, Time: {a['time']}")


def add_video(videos):
    # Adding video
    name = input("Enter video name:")
    time = input("Enter video time:")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    idx = input("Enter the number of video you want to edit: ")
    if 0 < int(idx) <= len(videos):
        name = input("Enter updated video name:")
        time = input("Enter updated video time:")
        videos[int(idx) - 1] = {"name": name, "time": time}
        save_data_helper(videos)
        print("Video updated successfully!")
        return
    print("Video not found!")


def delete_video(videos):
    idx = input("Enter the number of video you want to delete: ")
    if 0 < int(idx) <= len(videos):
        videos.pop(int(idx) - 1)
        save_data_helper(videos)
        print("Video deleted successfully!")
        return
    print("Video not found!")


def main():
    videos = load_data()
    while True:
        clear_console()
        print("Welcome to YouTube Manager!")
        print("Choose an option:")
        print("1- List all youtube videos")
        print("2- Add a youtube video")
        print("3- Update a youtube video details")
        print("4- Delete a youtube video")
        print("5- Exit the app")
        choice = input("Enter you choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting the app...")
                exit()
            case _:
                print("Invalid choice. Please try again.")
                continue

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()

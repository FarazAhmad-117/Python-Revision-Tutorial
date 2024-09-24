import sqlite3
import os


def clear_console():
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For Linux and macOS
        os.system("clear")


con = sqlite3.connect("./youtube.db")
cur = con.cursor()

cur.execute(
    """
        CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            v_name TEXT NOT NULL,
            v_time TEXT NOT NULL
        )
"""
)


def list_all_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        # print(row)
        print(f"{row[0]}. Video Name: {row[1]}, Time: {row[2]} hours")


def add_video(name, time):
    cur.execute("INSERT INTO videos(v_name, v_time) VALUES(?,?)", (name, time))
    con.commit()
    print("Video Added Successfully")


def update_video(id, name, time):
    cur.execute(
        """
                UPDATE videos
                SET v_name=?,
                v_time=?
                WHERE id=?
""",
        (name, time, id),
    )
    con.commit()
    print("Video updated successfully")


def delete_video(id):
    cur.execute("DELETE FROM videos WHERE id=?", (id,))
    con.commit()


def main():
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

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter name of video: ")
            time = input("Enter time of video: ")
            add_video(name, time)
        elif choice == "3":
            id = input("Enter video ID to update: ")
            name = input("Enter name of video: ")
            time = input("Enter time of video: ")
            update_video(id, name, time)
        elif choice == "4":
            id = input("Enter video ID to delete: ")
            delete_video(id)
        elif choice == "5":
            print("Exiting the app...")
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

    con.close()


if __name__ == "__main__":
    main()

Project Title: Spotify Mini Music Streaming System
Course: SEN
Student Name: OLOGUNDE OLAMIDE JOSIAH
Matric Number: 24/13913




# List of available songs in the system
songs = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "album": "After Hours"},
    {"title": "Shape of You", "artist": "Ed Sheeran", "album": "Divide"},
    {"title": "Essence", "artist": "Wizkid", "album": "Made in Lagos"},
    {"title": "Ojuelegba", "artist": "Wizkid", "album": "Ayo"},
    {"title": "Calm Down", "artist": "Rema", "album": "Rave & Roses"},
]

# Dictionary to store registered users
# Format: {username: password}
users = {}

# Dictionary to store user playlists
# Format: {username: [list_of_songs]}
playlists = {}


def register():
    """
    Handles new user registration.
    Prompts user for username and password.
    Stores credentials in the users dictionary.
    """
    print("\n--- USER REGISTRATION ---")

    username = input("Enter a username: ").strip()

    # Check if username already exists
    if username in users:
        print("ERROR: Username already exists. Please login instead.")
        return

    password = input("Enter a password: ").strip()

    # Save user details
    users[username] = password
    playlists[username] = []

    print("SUCCESS: Registration completed.")


def login():
    """
    Handles user login.
    Verifies username and password.
    Returns username if login is successful.
    """
    print("\n--- USER LOGIN ---")

    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username in users and users[username] == password:
        print("SUCCESS: Login successful.")
        return username
    else:
        print("ERROR: Invalid username or password.")
        return None


def view_songs():
    """
    Displays all available songs in the system.
    """
    print("\n--- SPOTIFY SONG LIBRARY ---")

    for index, song in enumerate(songs, start=1):
        print(f"{index}. {song['title']} - {song['artist']} ({song['album']})")


def search_songs():
    """
    Allows users to search songs by title or artist.
    """
    print("\n--- SEARCH SONGS ---")

    keyword = input("Enter song title or artist: ").strip().lower()

    results = []
    for song in songs:
        if keyword in song["title"].lower() or keyword in song["artist"].lower():
            results.append(song)

    if results:
        print("\nSearch Results:")
        for index, song in enumerate(results, start=1):
            print(f"{index}. {song['title']} - {song['artist']} ({song['album']})")
    else:
        print("No matching songs found.")


def add_to_playlist(username):
    """
    Adds a selected song to the logged-in user's playlist.
    """
    view_songs()

    try:
        choice = int(input("\nEnter the song number to add to playlist: "))

        if 1 <= choice <= len(songs):
            playlists[username].append(songs[choice - 1])
            print("SUCCESS: Song added to your playlist.")
        else:
            print("ERROR: Invalid song number.")

    except ValueError:
        print("ERROR: Please enter a valid number.")


def view_playlist(username):
    """
    Displays all songs in the user's playlist.
    """
    print("\n--- YOUR PLAYLIST ---")

    user_playlist = playlists.get(username, [])

    if not user_playlist:
        print("Your playlist is empty.")
        return

    for index, song in enumerate(user_playlist, start=1):
        print(f"{index}. {song['title']} - {song['artist']} ({song['album']})")


def spotify_menu(username):
    """
    Displays the main Spotify menu after login.
    """
    while True:
        print("\n========== SPOTIFY MAIN MENU ==========")
        print("1. View Songs")
        print("2. Search Songs")
        print("3. Add Song to Playlist")
        print("4. View Playlist")
        print("5. Logout")

        choice = input("Select an option: ").strip()

        if choice == "1":
            view_songs()
        elif choice == "2":
            search_songs()
        elif choice == "3":
            add_to_playlist(username)
        elif choice == "4":
            view_playlist(username)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("ERROR: Invalid menu option.")


# ======================================================
# PHASE 4: MAIN APPLICATION CONTROLLER
# ======================================================

def main():
    """
    Main entry point of the Spotify Mini Project.
    Controls system flow and user interaction.
    """
    while True:
        print("\n========== WELCOME TO SPOTIFY ==========")
        print("Student Name: OLOGUNDE OLAMIDE JOSIAH")
        print("Matric Number: 24/13913")
        print("---------------------------------------")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            logged_in_user = login()
            if logged_in_user:
                spotify_menu(logged_in_user)
        elif choice == "3":
            print("Thank you for using Spotify Mini App. Goodbye!")
            break
        else:
            print("ERROR: Invalid selection.")


# ======================================================
# PROGRAM EXECUTION
# ======================================================

if __name__ == "__main__":
    main()

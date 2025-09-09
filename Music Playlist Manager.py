"""
Music Playlist Manager
Covers: input, variables, lists, dicts, functions, loops,
if-else, nesting, docstrings, file handling
"""

import random

# ---- Global Constant ----
PLAYLIST_FILE = "playlist.txt"

# ---- Playlist Storage ----
playlist = []  # each song is stored as a dict


# ---- Functions ----

def add_song():
    """Add a new song to the playlist"""
    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    duration = input("Enter song duration (e.g., 3:45): ")

    song = {"title": title, "artist": artist, "duration": duration}
    playlist.append(song)

    print(f"✅ Added: {title} by {artist}")


def view_playlist():
    """Show all songs in the playlist"""
    if not playlist:
        print("⚠️ Playlist is empty.")
        return

    print("\n🎶 Current Playlist:")
    for idx, song in enumerate(playlist, start=1):
        print(f"{idx}. {song['title']} - {song['artist']} ({song['duration']})")


def remove_song():
    """Remove a song by number"""
    view_playlist()
    if not playlist:
        return

    try:
        choice = int(input("Enter song number to remove: "))
        if 1 <= choice <= len(playlist):
            removed = playlist.pop(choice - 1)
            print(f"🗑️ Removed: {removed['title']} by {removed['artist']}")
        else:
            print("❌ Invalid song number.")
    except ValueError:
        print("⚠️ Invalid input. Enter a number.")


def play_random_song():
    """Play a random song from the playlist"""
    if not playlist:
        print("⚠️ Playlist is empty.")
        return
    song = random.choice(playlist)
    print(f"🎵 Now playing: {song['title']} - {song['artist']} ({song['duration']})")


def save_playlist():
    """Save playlist to file"""
    with open(PLAYLIST_FILE, "w") as f:
        for song in playlist:
            f.write(f"{song['title']},{song['artist']},{song['duration']}\n")
    print(f"💾 Playlist saved to {PLAYLIST_FILE}")


def load_playlist():
    """Load playlist from file"""
    try:
        with open(PLAYLIST_FILE, "r") as f:
            for line in f:
                title, artist, duration = line.strip().split(",")
                playlist.append({"title": title, "artist": artist, "duration": duration})
        print("📂 Playlist loaded successfully.")
    except FileNotFoundError:
        print("⚠️ No saved playlist found.")


def playlist_menu():
    """Main menu for playlist manager"""
    load_playlist()

    while True:
        print("\n--- Music Playlist Manager ---")
        print("1. Add Song")
        print("2. View Playlist")
        print("3. Remove Song")
        print("4. Play Random Song")
        print("5. Save & Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_song()
        elif choice == "2":
            view_playlist()
        elif choice == "3":
            remove_song()
        elif choice == "4":
            play_random_song()
        elif choice == "5":
            save_playlist()
            print("👋 Exiting Music Playlist Manager. Bye!")
            break
        else:
            print("❌ Invalid choice, try again.")


# ---- Run Program ----
playlist_menu()

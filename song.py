class Song:

    def __init__(self, song_id, title, artist, duration):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return (f"Song ID: {self.song_id}\n"
                f"Song Title: {self.title}\n"
                f"Artist: {self.artist}\n"
                f"Duration: {self.duration}")

class Node:

    def __init__(self, song):
        self.song = song
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    def insert_first(self, song):
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_last(self, song):
        new_node = Node(song)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.count += 1

    def insert_at(self, position, song):

        if position < 1 or position > self.count + 1:
            return False

        if position == 1:
            self.insert_first(song)
            return True

        new_node = Node(song)
        current = self.head

        for _ in range(position - 2):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.count += 1
        return True

    def search(self, song_id):
        current = self.head
        while current is not None:
            if current.song.song_id == song_id:
                return current.song
            current = current.next
        return None

    def delete(self, song_id):
        current = self.head
        previous = None

        while current is not None:
            if current.song.song_id == song_id:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.count -= 1
                return True
            previous = current
            current = current.next
        return False

    def display(self):
        if self.is_empty():
            print("The playlist is empty.")
            return

        print("-" * 60)
        current = self.head
        index = 1
        chain = []
        while current is not None:
            song = current.song
            print(f"[{index}] {song.song_id} | {song.title} | "
                  f"{song.artist} | {song.duration}")
            chain.append(f"[{song.title}]")
            current = current.next
            index += 1
        print("-" * 60)
        print(" -> ".join(chain) + " -> NULL")
        print(f"Total number of songs: {self.count}")

class MusicPlaylistManager:

    def __init__(self):
        self.playlist = SinglyLinkedList()

    def run(self):
        while True:
            self._print_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_song_beginning()
            elif choice == "2":
                self.add_song_end()
            elif choice == "3":
                self.insert_song_at_position()
            elif choice == "4":
                self.playlist.display()
            elif choice == "5":
                self.search_song()
            elif choice == "6":
                self.remove_song()
            elif choice == "7":
                print(f"Total number of songs: {self.playlist.size()}")
            elif choice == "8":
                print("Exiting Music Playlist Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 8.")

    def _print_menu(self):
        print("\n================================")
        print("     MUSIC PLAYLIST MANAGER")
        print("================================")
        print("1. Add Song at Beginning")
        print("2. Add Song at End")
        print("3. Insert Song at Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit")

    def _get_non_empty_input(self, prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty. Please try again.")

    def _get_new_song_details(self):
        song_id = self._get_non_empty_input("Song ID: ")
        if self.playlist.search(song_id) is not None:
            print(f"A song with ID '{song_id}' already exists.")
            return None
        title = self._get_non_empty_input("Song Title: ")
        artist = self._get_non_empty_input("Artist: ")
        duration = self._get_non_empty_input("Duration (e.g. 4:23): ")
        return Song(song_id, title, artist, duration)

    def add_song_beginning(self):
        print("\n-- Add Song at Beginning --")
        song = self._get_new_song_details()
        if song is not None:
            self.playlist.insert_first(song)
            print(f"'{song.title}' added at the beginning of the playlist.")

    def add_song_end(self):
        print("\n-- Add Song at End --")
        song = self._get_new_song_details()
        if song is not None:
            self.playlist.insert_last(song)
            print(f"'{song.title}' added at the end of the playlist.")

    def insert_song_at_position(self):
        print("\n-- Insert Song at Position --")
        max_position = self.playlist.size() + 1
        while True:
            pos_input = input(f"Enter position (1 to {max_position}): ").strip()
            if pos_input.isdigit() and 1 <= int(pos_input) <= max_position:
                position = int(pos_input)
                break
            print(f"Invalid position. Please enter a number between 1 and {max_position}.")

        song = self._get_new_song_details()
        if song is not None:
            self.playlist.insert_at(position, song)
            print(f"'{song.title}' inserted at position {position}.")

    def search_song(self):
        print("\n-- Search Song --")
        song_id = self._get_non_empty_input("Enter Song ID to search: ")
        song = self.playlist.search(song_id)
        if song:
            print("\nSong Found:")
            print(song)
        else:
            print(f"No song found with ID '{song_id}'.")

    def remove_song(self):
        print("\n-- Remove Song --")
        song_id = self._get_non_empty_input("Enter Song ID to remove: ")
        if self.playlist.delete(song_id):
            print(f"Song with ID '{song_id}' removed successfully.")
        else:
            print(f"No song found with ID '{song_id}'.")

def main():
    manager = MusicPlaylistManager()
    manager.run()

if __name__ == "__main__":
    main()
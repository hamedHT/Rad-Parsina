class Mobile:
    def __init__(self):
         print("This message is from Constructor Method")
    def receive_message(self):
         print("Receive message using Mobile")
    def send_message(self):
         print("Send message using Mobile")
def main():
    nokia = Mobile()
    nokia.receive_message()
    nokia.send_message()
if __name__ == "__main__":
    main()

#_________________________________________________________________________________________________    

class Mobile:
    def __init__(self, name):
        self.mobile_name = name
    def receive_message(self):
        print(f"Receive message using {self.mobile_name} Mobile")
    def send_message(self):
        print(f"Send message using {self.mobile_name} Mobile")
def main():
    nokia = Mobile("Nokia")
    nokia.receive_message()
    nokia.send_message()
if __name__ == "__main__":
    main()

#_________________________________________________________________________________________________

class Dog:
    def __init__(self, breed="German Shepherd", color="Tan Black"):
        self.breed = breed
        self.color = color
    def dog_breed(self):
        print(f"Dog Breed is {self.breed}")
    def dog_color(self):
        print(f"Dog Color is {self.color}")
def main():
    babloo = Dog()
    babloo.dog_breed()
    babloo.dog_color()
if __name__ == "__main__":
    main()
#_________________________________________________________________________________________________

class Track:
    def __init__(self, song, artist):
        self.song = song
        self.artist = artist
def print_track_info(vocalist):
    print(f"Song is '{vocalist.song}'")
    print(f"Artist is '{vocalist.artist}'")
singer = Track("The First Time Ever I Saw Your Face", "Roberta Flack")
print_track_info(singer)

#_________________________________________________________________________________________________

class Dog:
    kind = 'canine'
    def __init__(self, name):
        self.dog_name = name
d = Dog('Fido')
e = Dog('Buddy')
print(f"Value for Shared Variable or Class Variable 'kind' is '{d.kind}'")
print(f"Value for Shared Variable or Class Variable 'kind' is '{e.kind}'")
print(f"Value for Unique Variable or Instance Variable 'dog_name' is '{d.dog_name}'")
print(f"Value for Unique Variable or Instance Variable 'dog_name' is '{e.dog_name}'")

class Playlist:
    def __init__(self,name,songs:list=[]):
        self.name=name
        self.songs=songs

    def add(self,song):
        self.songs.append(song)

    def remove(self,song):
        if song in self.songs:
            self.pop(song)
        else:
            print(f"{song} is not in the Playlist")

    def show(self):
        return_output=f"{self.name}\n"
        for i,song in enumerate(self.songs):
            return_output=return_output +str(i+1)+". " +song + "\n"
        print(return_output)

happy = Playlist("Happy")
happy.add("Marvin Gaye")
happy.add("24K Magic")
happy.remove("Marvin Gay")
happy.show()
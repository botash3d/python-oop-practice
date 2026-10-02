class Book:
    def __init__(self,title:str,author:str):
        self.title=title
        self.author=author

    def __str__(self):
        return f"{self.title} by {self.author}"

book1=Book("Pride and Prejudice" , "Jane Austen")
book2=Book("1984", "George Orwell")
print(book1)
print(book2)
import datetime
import os
# os.getcwd()

class LMS:
    """  This class is used to keep record of books library.
     It has total four module: "Display Books", "Issue books", "Return books","Add books" """
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books 
        self.library_name = library_name 
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            print(line)

print(LMS("List_of_books.txt", "Python's Library"))                

        
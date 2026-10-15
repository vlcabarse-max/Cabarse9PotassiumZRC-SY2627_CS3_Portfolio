class Publication:
    def __init__(self, title, author):
       
        self.set_title(title)
        self.set_author(author)

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def display_info(self):
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self._number_of_pages

    def set_number_of_pages(self, number_of_pages):
        # Data validation requirement
        if number_of_pages > 0:
            self._number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")
            self._number_of_pages = None

    def display_info(self):
        super().display_info()
        if self._number_of_pages is not None:
            print(f"Number of Pages: {self.get_number_of_pages()}")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self._issue_number

    def set_issue_number(self, issue_number):
        
        if issue_number > 0:
            self._issue_number = issue_number
        else:
            print("The issue number must be positive.")
            self._issue_number = None

    def display_info(self):
        super().display_info()
        if self._issue_number is not None:
            print(f"Issue Number: {self.get_issue_number()}")



print("=== Publications ===")
pub1 = Publication("General Knowledge", "John Smith")
pub1.display_info()
print("-" * 20)

pub2 = Publication("Library Guide", "Jane Doe")
pub2.display_info()

print("\n=== Books ===")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book1.display_info()
print("-" * 20)

book2 = Book("Python Basics", "Alan Turing", -50) 
book2.display_info()

print("\n=== Magazines ===")
mag1 = Magazine("National Geographic", "Various", 202)
mag1.display_info()
print("-" * 20)

mag2 = Magazine("Tech Monthly", "Editorial Board", 0)  
mag2.display_info()
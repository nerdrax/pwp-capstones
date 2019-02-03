
# User
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "This user's email has been updated to: {email}".format(email=address)

    def __repr__(self):
        return "User {name}, email: {email}, books read: {books}".format(name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        return sum([rating for rating in self.books.values() if rating is not None]) / len(self.books)


# Book
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, number):
        self.isbn = number
        return "This book's ISBN has been updated to: {isbn}".format(isbn=number)

    def add_rating(self, rating):
        if not rating or rating < 0 or rating > 4:
            return "Invalid Rating"
        else:
            self.ratings.append(rating)

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        return sum([rating for rating in self.ratings]) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

# Fiction Subclass of Book
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

# Non Fiction Subclass of Book
class Non_Fiction(Book):
    def  __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


# TomeRater
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        isbns = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbns:
            print("The ISBN already Exists")
        else:
            return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        isbns = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbns:
            print("The ISBN already Exists")
        else:
            return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        isbns = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbns:
            print("The ISBN already Exists")
        else:
            return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, "No user with email: {email}!".format(email=email))
        if user:
            user.read_book(book, rating)
            book.add_rating(rating)
            self.books[book] = self.books.get(book, 0) + 1

    def add_user(self, name, email, user_books=None):
        if email.find("@") == -1 or (email.find(".com") == -1 and email.find(".edu") == -1 and email.find(".org") == -1):
            print("Email is Invalid")
        else:
            if email not in self.users:
                self.users[email] = User(name, email)
                if user_books is not None:
                    for book in user_books:
                        self.add_book_to_user(book, email)
            else:
                print("User already Exists")

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self,users.values():
            print(user)

    def most_read_book(self):
        return max(self.books, key=self.books.get)

    def highest_rated_book(self):
        highest_rated = max(rating.get_average_rating() for rating in self.book.keys())
        return str([book for book in self.books.keys() if book.get_average_rating() == highest_rated]).strip("[]")

    def most_positive_user(self):
        most_positive = max(rating.get_average_rating() for rating in self.users.values())
        return str([user for user in self.users.values() if user.get_average_rating() == most_positive]).strip("[]")

    #Get Creative Part
    def get_n_most_read_books(self, n):
        books_sorted = [k for k in sorted(self.books, key=self.books.get, reverse=True)]
        return books_sorted[:n]

    def get_n_most_prolific_readers(self, n):
        readers = [(reader, reader.get_books_read()) for reader in self.users.values()]
        readers_sorted = [k[0] for k in sorted(readers, key=lambda reader: reader[1], reverse=True)]
        return readers_sorted[:n]

    def get_n_most_expensive_books(self, n):
        books = {book: book.get_price() for book in self.books.keys()}
        books_sorted = [k for k in sorted(books, key=books.get, reverse=True)]
        return books_sorted[:n]

    def get_worth_of_user(self, user_email):
        if user_email.find("@") == -1 or (user_email.find(".com") == -1 and user_email.find(".edu") == -1 and user_email.find(".org") == -1):
            print("Email is Invalid")
        else:
            user = self.users.get(user_email)
            if not user:
                print("User Does Not Exist")
            else:
                price = 0
                for book in user.books.keys():
                    price += book.get_price()
                return price

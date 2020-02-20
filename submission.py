import sys
import os

score = 0
book_score_table = {}
library_list = [] # list of libraries to be set up
books = 0
days = 0
libraries = 0
scan_list = []

class Book():
    score = 0

class Library:
    num_books = 0
    setup_time = 0
    daily_ship = 0
    books = []
    signed_up = False
    setup_time_left = setup_time
    books_shipped = []

    def __init__(self, ID, num_books, setup_time, daily_ship, books):
        self.id = ID
        self.num_books = num_books
        self.setup_time = setup_time
        self.daily_ship = daily_ship
        print(books)
        self.books = sorted(books, key=lambda x: book_score_table[x], reverse=True)
        print(self.books)
        self.setup_time_left = setup_time
        

# signups can only happen one at a time
# need to schedule what the optimal ordering of signups are
# order low to high?

def signup_library(need_to_signup):
    if len(need_to_signup) > 0:
        need_to_signup[0].setup_time_left -= 1
        if need_to_signup[0].setup_time_left <= 0:
            need_to_signup[0].setup_time_left = 0
            need_to_signup[0].signed_up = True
            lib = need_to_signup.pop(0)
            scan_list.append(lib)


def parse_input():
    global library_list, book_score_table, books, days, libraries
    books_libraries_days = list(map(int, input().split(" ")))
    
    books = books_libraries_days[0]
    libraries = books_libraries_days[1]
    days = books_libraries_days[2]
    book_scores = list(map(int, input().split(" ")))
    
    # process book scores
    for i in range(len(book_scores)):
        book_score_table[i] = book_scores[i]
    
    # process library information
    for i in range(libraries):
        library_information = list(map(int, input().split(" ")))
        book_indices = list(map(int, input().split(" ")))
        library_list.append(Library(i, library_information[0], library_information[1], library_information[2], book_indices))
    
    # print(library_list)
    print(book_score_table)


def scan(lib):
    global score, book_score_table
    for i in range(lib.daily_ship):
        print("i", i)
        if len(lib.books) == 0:
            return

        book_to_ship = lib.books.pop(0)
        score += book_score_table[book_to_ship]
        book_score_table[book_to_ship] = 0
        
        lib.books_shipped.append(book_to_ship)
        lib.books.sort(key=lambda x: book_score_table[x], reverse=True)
        print("lib books", lib.books)
        print("lib.books_shipped", lib.books_shipped)

def run():
    global library_list, book_score_table, books, days, libraries, scan_list
    
    need_to_signup = sorted(library_list, key=lambda x: x.setup_time, reverse=False)
    library_list.sort(key=lambda x: x.setup_time, reverse=False)

    for d in range(days):
        if need_to_signup:
            signup_library(need_to_signup)  
        
        for sl in scan_list:
            if len(sl.books) > 0:
                scan(sl)

    print(len(scan_list))
    for i in scan_list:
        print(i.id, len(i.books_shipped))
        print(*(i.books_shipped))
    
if __name__ == "__main__":
    parse_input()
    run()

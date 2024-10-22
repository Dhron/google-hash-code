import sys
import os

score = 0
book_score_table = {}
library_list = [] # list of libraries to be set up
books = 0
days = 0
libraries = 0
scan_list = []

class Library:
    def __init__(self, ID, num_books, setup_time, daily_ship, books):
        self.id = ID
        self.num_books = num_books
        self.setup_time = setup_time
        self.daily_ship = daily_ship
        self.books = sorted(books, key=lambda x: book_score_table[x], reverse=True)
        self.setup_time_left = setup_time
        self.signed_up = False
        self.setup_time_left = setup_time
        self.books_shipped = []
        self.max_score = 0
        self.rate = 0
        self.update_rate()

    def update_rate(self):
        for b in self.books:
            self.max_score += book_score_table[b]
        self.rate = float(self.max_score) / float(self.setup_time)
        # self.books.sort(key=lambda x: book_score_table[x], reverse=True)


def signup_library(need_to_signup):
    added = False
    if len(need_to_signup) > 0:
        need_to_signup[0].setup_time_left -= 1
        if need_to_signup[0].setup_time_left <= 0:
            need_to_signup[0].setup_time_left = 0
            need_to_signup[0].signed_up = True
            lib = need_to_signup.pop(0)
            scan_list.append(lib)
            added = True
    if added:
        for n in need_to_signup:
            n.update_rate()
        need_to_signup = sorted(library_list, key=lambda x: (-x.rate, x.daily_ship), reverse=False)

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


def scan(lib):
    global score, book_score_table
    for i in range(lib.daily_ship):
        # print("i", i)
        if len(lib.books) == 0:
            return

        book_to_ship = lib.books.pop(0)
        score += book_score_table[book_to_ship]
        book_score_table[book_to_ship] = 0
        
        lib.books_shipped.append(book_to_ship)
        lib.books.sort(key=lambda x: book_score_table[x], reverse=True)
        # print("lib books", lib.books)
        # print("lib.books_shipped", lib.books_shipped)
        # print("Score: ", score)

def run():
    global library_list, book_score_table, books, days, libraries, scan_list
    need_to_signup = sorted(library_list, key=lambda x: ((-x.rate, x.daily_ship)), reverse=False)

    for d in range(days):       
        
        # library_list.sort(key=lambda x: (x.rate, x.setup_time), reverse=False)

        if need_to_signup:
            signup_library(need_to_signup)  
        
        for sl in scan_list:
            if len(sl.books) > 0:
                scan(sl)

    # print("\n")
    # for l in library_list:
    #     print(l.__dict__)
    # print("\n")

    # print("Output")
    print(len(scan_list))
    for i in scan_list:
        print(i.id, len(i.books_shipped))
        print(*(i.books_shipped))
    
if __name__ == "__main__":
    parse_input()
    run()

import sys
import os

book_score_table = {}
class Book():
    score = 0

class Library:
    num_books = 0
    setup_time = 0
    daily_ship = 0
    books = []
    
    def __init__(self, num_books, setup_time, daily_ship, books):
        self.num_books = books
        self.setup_time = setup_time
        self.daily_ship = daily_ship
        self.books = books
        
    
# signups can only happen one at a time
# need to schedule what the optimal ordering of signups are
# order low to high?

def signup_library():
    pass

def parse_input():
    books_libraries_days = list(map(int, input().split(" ")))
    
    books = books_libraries_days[0]
    libraries = books_libraries_days[1]
    days = books_libraries_days[2]
    book_scores = list(map(int, input().split(" ")))
    
    # process book scores
    for i in range(len(book_scores)):
        book_score_table[i] = book_scores[i]
    
    library_list = [] # list of libraries to be set up
    
    # process library information
    for i in range(libraries):
        library_information = list(map(int, input().split(" ")))
        book_indices = list(map(int, input().split(" ")))
        library_list.append(Library(library_information[0], library_information[1], library_information[2], book_indices))
    
    print(library_list)
    
if __name__ == "__main__":
    parse_input()
    pass
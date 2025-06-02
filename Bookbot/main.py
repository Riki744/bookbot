# Author: Riki 
# The entry point to our program
from stats import *
import sys


# file path to book argument
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at", book[-22:]) 
    print("----------- Word Count ----------")    
    get_num_words(book)
    print("--------- Character Count -------") 
    chars = get_characters(get_book(book)) 
    final = sorted_chars(chars) 

    for char in final:
        if char['char'].isalpha():
            test = f"{char['char']}: {char['num']}"
            print(test)        
    print("============= END ===============")


if __name__ == "__main__":
    main()

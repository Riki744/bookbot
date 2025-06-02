# stats.py A file that contains functions for analyzing the text

# file path to book
book = "/home/riki/bootdev/bootdev/Bookbot/books/frankenstein.txt"

# read file
def get_book(book):
    with open(book) as f:
        book_contents = f.read()
    return book_contents
        

# count words
def get_num_words(book_text):
    with open(book) as f:
        book_contents = f.read()
        word_count = len(book_contents.split())
        print(f"Found {word_count} total words")


# get character and their counts
def get_characters(text):
    # creating key-value pairs
    chars = {} 
    for char in text:
        char = char.lower()
        # Check if we've seen this character before
        if char in chars:
            # If yes, increment its count
            chars[char] += 1
        else:
            # If no, add it to the dictionary with count 1
            chars[char] = 1
    return chars

# returns sorted list of characters and thier counts
def sorted_chars(dict):
    sorted = []
    for char, num in dict.items():
        sorted.append({"char": char, "num": num})
        sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(dict):
    return dict["num"]



   
def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
    word_count = count_words(book_text)
    print(f"{word_count} characters in the book")

def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    split_text = text.split()
    character_count = len(split_text)
    return character_count

main()
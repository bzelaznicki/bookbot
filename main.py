def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    print(f"{word_count} words in the book")
    print(f"{character_count}")

def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    split_text = text.split()
    word_count = len(split_text)
    return word_count

def count_characters(text):
    lowered_text = text.lower()
    characters = list(lowered_text)
    character_counts = {}
    for character in characters:
        if character in character_counts:    
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

main()
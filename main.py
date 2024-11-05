import sys

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        book_text = read_book(book_path)
        if book_text != None:
            word_count = count_words(book_text)
            character_count = count_characters(book_text)
            converted_character_count = convert_character_count(character_count)
            generate_book_report(book_path, word_count, converted_character_count)
    else:
        print("No file specified!")
        return None

def read_book(book_path):
    try:
        with open(book_path) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print(f"Error: file at {book_path} was not found")
        return None
    except IOError:
        print(f"An error has occured when reading {book_path}")
        return None
def count_words(text):
    split_text = text.split()
    word_count = len(split_text)
    return word_count

def count_characters(text):
    lowered_text = text.lower()
    characters = list(lowered_text)
    character_counts = {}
    for character in characters:
        if character.isalpha():
            if character in character_counts:    
                character_counts[character] += 1
            else:
                character_counts[character] = 1
    return character_counts

def convert_character_count(words_dict):
    def sort_on(dict):
        return dict["count"]
    characters_list = []
    for character in words_dict:
        characters_list.append({"character": character, "count": words_dict[character]})
    characters_list.sort(reverse=True, key=sort_on)
    return characters_list
    
def prettified_converted_characters(conv_characters):
    for character in conv_characters:
        print(f"The '{character['character']}' was found {character['count']} times")

def generate_book_report(book_path, word_count, converted_character_count):  
        print(f"--- Begin report of {book_path} ---")
        print("")
        print(f"{word_count} words found in the book")
        prettified_converted_characters(converted_character_count)
        print("")
        print(f"--- End report ---")
main()
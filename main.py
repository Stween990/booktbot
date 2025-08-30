from stats import get_num_words, times_character, sort_on
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(sys.argv[1]))} total words")
    print("----------- Character Count ----------")
    x = sort_on(times_character(get_book_text(sys.argv[1])))
    for i in x:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
main()
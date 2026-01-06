import sys
from stats import get_num_words, get_chars_dict, sorted_list

def main():
    # Check if the user provided exactly one argument (the file path)
    # sys.argv[0] is the script name, sys.argv[1] should be the path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    # The rest of your logic remains the same, but uses book_path
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted = sorted_list(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in chars_sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
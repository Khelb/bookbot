from stats import character_counter, count_words


def get_book_text(file):
    with open(file) as f:
        file_data = f.read()
    return file_data


def main():
    opened_file = get_book_text("books/frankenstein.txt")
    split_string = count_words(opened_file)
    print("Found", split_string, "total words")
    counted_characters = character_counter(opened_file)
    print(counted_characters)


main()

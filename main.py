from stats import character_counter, count_words, sorted_char_counter


def get_book_text(file):
    with open(file) as f:
        file_data = f.read()
    return file_data


def main():
    opened_file = get_book_text("books/frankenstein.txt")
    split_string = count_words(opened_file)
    counted_characters = character_counter(opened_file)
    # print(counted_characters)
    sorted_list = sorted_char_counter(counted_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {split_string} total words")
    print("--------- Character Count -------")

    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")


main()

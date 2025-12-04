def get_book_text(file):
    with open(file) as f:
        file_data = f.read()
    return file_data


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(file_contents)

def count_words():


main()

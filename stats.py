def count_words(text):
    word_count = text.split()
    return len(word_count)


def character_counter(text):
    char_dict = {}

    for char in text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1

    return char_dict

def count_words(text):
    word_count = text.split()
    return len(word_count)


def character_counter(text):
    char_dict = {}
    lower_case_string = text.lower()
    sep_chars = list(lower_case_string)
    for char in sep_chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

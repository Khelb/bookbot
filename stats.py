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


def sort_on(items):
    return items["num"]


def sorted_char_counter(dic):
    sorted_list = []

    for key, value in dic.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        sorted_list.append(new_dict)

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

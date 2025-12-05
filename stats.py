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
    dict_list = []
    dict_char = {}
    dict_count = {}
    dict_comb = {}

    for key, value in dic.items():
        dict_char["char"] = key
        dict_count["num"] = value
        dict_comb = dict_char | dict_count
        dict_list.append(dict_comb)

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list

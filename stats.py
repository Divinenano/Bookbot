def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = str.split(file_contents)
        word_count = len(words)
    return word_count

def total_counter(filepath):
    dictionary = {}
    with open(filepath) as f:
        file_contents = f.read()
        for char in file_contents:
            lowcase_char = str.lower(char)
            if lowcase_char in dictionary:
                dictionary[lowcase_char] += 1
            else:
                dictionary[lowcase_char] = 1
    return dictionary

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        if not ch.isalpha():
            continue
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

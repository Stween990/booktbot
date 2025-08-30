from operator import itemgetter

def get_num_words(text):
    return f"{len(text.split())}"


def times_character(book):
    characters = {}
    for i in book.lower():
        if i not in characters:
            characters[i] = 1
        else:
            characters[i] +=1 
    return characters


def sort_key(key):
    return key["num"]


def sort_on(characters_dictionary):
    dict_list = []
    for i in characters_dictionary:
        dict_list.append({"char": i, "num": characters_dictionary[i]})
    dict_list.sort(reverse=True, key=sort_key) 
    return dict_list
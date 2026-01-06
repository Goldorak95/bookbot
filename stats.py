def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# This helper function tells .sort() which value to look at
def sort_on(d):
    return d["num"]

def sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        # Create a new dictionary for each character
        new_dict = {"char": char, "num": chars_dict[char]}
        sorted_list.append(new_dict)
    
    # Sort the list in place, descending (reverse=True)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
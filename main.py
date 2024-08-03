def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    number_of_word = count_words(text)
    char_frequency = count_frequency_each_letter(text)

    sort_char(char_frequency)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"There are {number_of_word} number of word in text")
    print(char_frequency)

    for key in char_frequency:
        if key.isalpha() == True:
            print(f"The {key} character was found {char_frequency[key]} times")
  
    print("--- End report ---")

def sort_char(char_frequency):
    sorted_list = []
    for key, value in char_frequency.items():
        sorted_list.append({"key": key, "value": value})

    sorted_list.sort(reverse=True, key=sort_on)

def sort_on(dict):
    return dict["value"]

def get_book_text(path):
    with open(path, 'r') as f:
        file_contents = f.read()
        return file_contents
 
def count_words(contents):
    words = contents.split()
    number_of_word = len(words)
    return number_of_word

def count_frequency_each_letter(contents):
    char_frequency = {}

    lowered_string_contents = contents.lower()

    for char in lowered_string_contents:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 0

    return char_frequency

main()
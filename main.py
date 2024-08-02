def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    number_of_word = count_words(text)
    print(f"There are {number_of_word} number of word in text")

    char_frequency = count_frequency_each_letter(text)
    print(char_frequency)
  
def get_book_text(path):
    with open(path, 'r') as f:
        file_contents = f.read()
        return file_contents
 
def get_num_words(words):
    return len(words)

def count_words(contents):
    words = contents.split()
    number_of_word = get_num_words(words)
    return number_of_word

def count_frequency_each_letter(contents):
    char_frequency = {}

    for number in range(0, 26):
        letter = chr(number + ord('a'))
        char_frequency[letter] = 0

    lowered_string_contents = contents.lower()
    words = lowered_string_contents.split()

    for word in words:
        for letter in word:
            if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
                char_frequency[letter] += 1

    return char_frequency
main()
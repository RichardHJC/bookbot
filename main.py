def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    number_of_word = count_words(text)
    print(f"There are {number_of_word} number of word in text")
  
def get_book_text(path):
    with open(path, 'r') as f:
        file_contents = f.read()
        return file_contents
 

def get_num_words(words):
    return len(words)

def count_words(contents):
    words = contents.split()
    print(words)
    number_of_word = get_num_words(words)
    return number_of_word

main()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    numbers_dict, letters_dict = sort_on(char_count)  # Corrected the output
    print(f"{num_words} words found in the document")
    
    sorted_letters = sorted(letters_dict.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    char_count = {}    
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(char_count):
    letters_dict = {}
    numbers_dict = {}
    
    for key, value in char_count.items():
        if key.isdigit():
            numbers_dict[key] = value
        elif key.isalpha():
            letters_dict[key] = value

    return numbers_dict, letters_dict


main()
    
    
    



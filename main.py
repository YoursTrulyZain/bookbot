def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = countWords(file_contents)
        character_dict = countCharacters(file_contents)
        alpha_character_list = dict_to_list(character_dict)
        alpha_character_list.sort(reverse=True, key=sort_on)
        print_report(word_count, alpha_character_list)

def countWords(file_contents):
    count = len(file_contents.split())
    return count

def countCharacters(file_contents):
    character_count = {}
    for c in file_contents.lower():
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count
    

def dict_to_list(dict):
    temp_list = []
    for c in dict:
        if c.isalpha():
            temp_list.append({"character": c, "count": dict[c]})
    return temp_list

def sort_on(dict):
    return dict["count"]

def print_report(word_count, character_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print("{} words found in the document".format(word_count))
    print()
    for dict in character_list:
        print("The {} character was found {} times".format(dict["character"], dict["count"]))



main()
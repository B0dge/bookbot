def main():
	book_path = "books/frank.txt"
	text = get_file(book_path)
	num_words = word_count(text)
	print(f"There are {num_words} words in document")

	lower_text = to_lower(text)

	result = char_count(lower_text)

	print(result)

	list_of_dicts(result)

def sort_on(dict):
    return dict["num"]

def word_count(file):
	words = file.split()
	return(len(words))

def get_file(path):
	with open(path) as f:
		return f.read()

def to_lower(text):
    return text.lower()

def char_count(low_text):
    character_count = {}

    for i in low_text:
        if i not in character_count:
            character_count[i] = 1
        else:
            character_count[i] += 1

    return character_count


def list_of_dicts(dict):
    dict_list = []
    for i in dict:
        if i.isalpha():
            dict_list.append({"name": i, "num": dict[i]})

    dict_list.sort(reverse=True, key=sort_on)
    print(dict_list)
    for i in dict_list:
        print (f"The '{i['name']}' character was found {i['num']} times")	

main()

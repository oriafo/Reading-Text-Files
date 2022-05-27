# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
filename = "story.txt"
dictionary = dict()

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as readFile:
        file = readFile.read()
    return file


def count_words():
    text = read_file_content(filename)
    # [assignment] Add your code here
    words = text.split()

    for split in words:   
        if split in dictionary:
            dictionary[split] = dictionary[split] + 1
        else:
            dictionary[split] = 1
    print(dictionary)
    return {"as": 10, "would": 20}

count_words()
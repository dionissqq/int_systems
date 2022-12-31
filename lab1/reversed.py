import string

def reversed_index(filenames):
    indexes = {}
    for filename in filenames:
        f = open(filename)
        for line in f:
            for word in line.split():
                word = word.translate(str.maketrans('','', string.punctuation))
                if not word in indexes:
                    indexes[word] = [filename]
                else:
                    if not filename in indexes[word]:
                        indexes[word].append(filename)
    return indexes
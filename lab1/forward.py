import string

def forward_index(filenames):
    indexes = {}
    for filename in filenames:
        f = open(filename)
        for line in f:
            for word in line.split():
                word = word.translate(str.maketrans('','', string.punctuation))
                if not filename in indexes:
                    indexes[filename] = [word]
                else:
                    if not word in indexes[filename]:
                        indexes[filename].append(word)
    return indexes
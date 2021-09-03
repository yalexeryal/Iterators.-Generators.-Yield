def hash_generator(filename):
    file = open(str(filename))
    for line in file.readline():
        yield hash(line)
    file.close()



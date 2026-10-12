testcasecount = int(input())

for hopethisworks in range(testcasecount):
    word = input()
    characters = []
    for character in word:
        characters.append(character)
    if len(characters) > 10:
        abbrev = str(len(characters)-2)
        ddd = len(characters)
        lennn = ddd-1
        newword = [characters[0], abbrev, characters[lennn]]
        word = "".join(newword)
        print(word)

    else: print(word)
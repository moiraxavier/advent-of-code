def contains_2_3(ID):
    letter_count = {}
    for letter in ID:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    two_letters = 2 in letter_count.values()
    three_letters = 3 in letter_count.values()

    return (two_letters, three_letters)

def checksum(data_input):
    cont = [0, 0]
    for ID in data_input:
        for i in range(2):
            if contains_2_3(ID)[i]:
                cont[i] += 1
    return cont[0] * cont[1]

def areClose(ID1, ID2):
    diff = 0
    for i in range(len(ID1)):
        if ID1[i] != ID2[i]:
            diff += 1
    if diff == 1:
        return True
    else:
        return False

def commonLetters(ID1, ID2):
    letters = []
    for i in range(len(ID1)):
        if ID1[i] == ID2[i]:
            letters.append(ID1[i])
    for l in letters:
        print(l, end ="")
    print()


def closeIDs(data_input):
    for i in range(len(data_input)):
        for j in range(i, length):
            if areClose(data_input[i], data_input[j]):
                commonLetters(data_input[i], data_input[j])
            

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        data_input = [i for i in f.read().splitlines()]

    print(checksum(data_input))
    closeIDs(data_input)


    
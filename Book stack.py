from string import ascii_lowercase

SYMBOLTABLE = list(ascii_lowercase)

def move2front_decode(sequence, symboltable):
    chars, pad = [], symboltable[:]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad
    return ''.join(chars)

if __name__ == '__main__':
    print(move2front_decode([1,17,15,0,0,5], SYMBOLTABLE))

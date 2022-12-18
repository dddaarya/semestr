# BWT coder
# Sample input:
# абракадабра
# Sample output:
# рдакраааабб 2
def bwt_coder(message):
    bwt_matrix = []
    for i in range(len(message)):
        bwt_matrix.append(message[i:] + message[:i])

    bwt_matrix.sort()
    last_column = ''.join([word[-1] for word in bwt_matrix])

    # print(*bwt_matrix, sep='\n')
    # print('________________________________')
    return last_column, bwt_matrix.index(message)


def bwt_decoder(encoded_word, position):
    decode_matrix = list(sorted(encoded_word))
    for _ in range(len(encoded_word) - 1):
        for i in range(len(encoded_word)):
            decode_matrix[i] = encoded_word[i] + decode_matrix[i]
        decode_matrix.sort()
    # print(*decode_matrix, sep='\n')
    # print('________________________________')
    return decode_matrix[position]


# Move to front coder
def mtf_coder(strng, symboltable):
    sequence, pad = [], symboltable[::]
    for char in strng:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad
    return sequence


def mtf_decoder(sequence, symboltable):
    chars, pad = [], symboltable[::]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad
    return ''.join(chars)


word = input('слово: ')
alphabet = sorted(list(set(word)))
print('алфавит', alphabet, end="\n\n")
bwt_encoded, position = bwt_coder(word)
print('bwt encode ', bwt_encoded, position)
mtf_encoded = mtf_coder(bwt_encoded, alphabet)
print('mtf encode ', mtf_encoded, position)
# расшифровка
mtf_decoded = mtf_decoder(mtf_encoded, alphabet)
print('mtf decode ', mtf_decoded, position)
print('bwt decode ', bwt_decoder(mtf_decoded, position)

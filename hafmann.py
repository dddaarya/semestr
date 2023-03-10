def findTheCharFrequency(text):
    result = dict()
    with open(text,'r') as f:
        lines = f.readlines()
        ver = [float(i) for i in list(lines[1].split())]
        result = (dict(zip(lines[0], ver)))
        global final_result_code
        final_result_code = {}
    return result



class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None


class HuffmanTree(object):
    def __init__(self, char_Weights):
        self.Leaf = [Node(k,v) for k, v in char_Weights.items()]
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node:node.value, reverse=True)
            n = Node(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.lchild = self.Leaf.pop(-1)
            n.rchild = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))

    def Hu_generate(self, tree, length):
        node = tree
        k = []
        if (not node):
            return
        elif node.name:
            for i in range(length):
                k.append(self.Buffer[i])
            final_result_code.update({node.name: ''.join(map(str, k))}) 
            return
        self.Buffer[length] = 0
        self.Hu_generate(node.lchild, length + 1)
        self.Buffer[length] = 1
        self.Hu_generate(node.rchild, length + 1)

    def get_code(self):
        self.Hu_generate(self.root, 0)

if __name__=='__main__':
    text = 'huffman.txt'
    result = findTheCharFrequency(text)
    tree = HuffmanTree(result)
    tree.get_code()
    code_message = ""
    word = input("Введите слово\n")
    for i in word:
        code_message += final_result_code[i]

    print(final_result_code)
    print(code_message)

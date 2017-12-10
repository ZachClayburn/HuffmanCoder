import HuffmanTree as Tree


class HuffmanCoder:
    def __init__(self):
        self.tree = None

    def build_tree(self, file_name):
        try:
            file = open(file_name, 'r')
            text = file.read()
        except FileNotFoundError:
            print('File Not Found\n No tree created.')
            return False
        file.close()

        char_count = dict()
        for char in text:
            if char in char_count.keys():
                char_count[char] += 1
            else:
                char_count[char] = 1

        self.tree = Tree.HuffmanTree(char_count)



if __name__ == "__main__":
    coder = HuffmanCoder()
    coder.build_tree('TestFiles/test1.txt')



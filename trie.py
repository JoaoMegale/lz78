class Node:
    def __init__(self, character, index):
        self.character = character
        self.index = index
        self.parent_index = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node("", 0)
        self.node_count = 1

    # insere um texto na trie e retorna o novo nó criado
    def insert(self, text):
        # inicia pela raiz
        node = self.root
        parent_index = 0
        for i in range (len(text)):
            # se o caractere está presente entre os nós do filho atual, segue percorrendo e atualiza o index do pai
            if text[i] in node.children:
                node = node.children[text[i]]
                parent_index = node.index
            # se o caractere nao foi encontrado, cria um novo nó para ele e retorna esse nó
            else:
                new_node = Node(text[i], self.node_count)
                node.children[text[i]] = new_node
                new_node.parent_index = parent_index
                self.node_count += 1
                return new_node
    
    # funcao booleana que retorna se um texto está contido ou nao na Trie
    def find(self, text):
        node = self.root
        # vai procurando cada caractere até que o texto todo seja lido
        for i in range (len(text)):
            # se em algum momento encontrar um caractere que nao esta na trie, retorna false
            if text[i] in node.children:
                node = node.children[text[i]]
            else:
                return False
        # se percorreu o texto todo e encontrou todos os caracteres, retorna true
        return True
                


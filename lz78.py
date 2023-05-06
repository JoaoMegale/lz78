from trie import Trie

def compression(file, out):
    tree = Trie()
    with open(file, "r", encoding="utf-8") as file_in:
        with open(out, "wb") as file_out:
            text = ""
            for char in file_in.read():
                # fim do arquvio
                if char == "":
                    break
                # se o texto for encontrado na trie, continua a concatenar os proximos caracteres
                text += char
                text_found = tree.find(text)
                # se o texto nao for encontrado, cria um novo nó para o caractere e o texto a ser encontrado volta a ser vazio
                if text_found == False:
                    new_node = tree.insert(text)
                    parent_index = new_node.parent_index
                    # escreve o indice do pai e o caractere adicionado no arquivo de saida em bytes
                    file_out.write(int(parent_index).to_bytes(3, byteorder='big'))
                    file_out.write(ord(char).to_bytes(2, byteorder='big'))
                    # texto a ser encontrado reinicia
                    text = ""


def decompression(file, out):
    with open(file, "rb") as file_in:
        with open(out, "w", encoding="utf-8") as file_out:
            text_storage = [''] # variavel para auxiliar a obter a ordem dos caracteres
            decoded_text = '' # variavel que armazena o texto final decodificado
            while True:
                # lê o arquivo binario e checa fim do arquivo
                coded_index = file_in.read(3)
                if coded_index == b'':
                    break
                coded_text = file_in.read(2)
                if coded_text == b'':
                    break
                # descodifica o que estava em bytes
                index = int.from_bytes(coded_index, 'big')
                text = int.from_bytes(coded_text, 'big')
                text = chr(text)
                # armazena o texto decodificado de acordo com o index
                text_storage.append((text_storage[index] + text))
                # o texto original vai sendo concatenado de acordo com a variavel de armazenamento
                decoded_text += text_storage[index] + text
            # escreve o texto decodificado completo no arquivo de saida
            file_out.write(decoded_text)


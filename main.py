from lz78 import compression, decompression
import sys

def main():
    if sys.argv[1] == '-c':
        arq_in = sys.argv[2]
        if len(sys.argv) <= 3:
            arq_out = sys.argv[2].replace('.txt', '.z78')
        else:
            arq_out = sys.argv[4]
        compression(arq_in, arq_out)
    if sys.argv[1] == '-x':
        arq_in = sys.argv[2]
        if len(sys.argv) <= 3:
            arq_out = sys.argv[2].replace('.z78', '.txt')
        else:
            arq_out = sys.argv[4]
        decompression(arq_in, arq_out)

if __name__ == "__main__":
    main()
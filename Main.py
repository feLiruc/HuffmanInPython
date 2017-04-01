import sys
from Encode import EncodeHuffman
from Decode import DecodeHuffman

def error():
    print("")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(">>      É necessario executar o script com 2 paramentros. Ex:         <<")
    print(">>                                                                    <<")
    print(">>                 python3 Main.py encode texto.txt                   <<")
    print(">>                                 ou                                 <<")
    print(">>                 python3 Main.py decode texto.txt                   <<")
    print(">>                                                                    <<")
    print(">>                           Tente novamente.                         <<")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("")


if __name__ == '__main__':
    if(len(sys.argv)==3):
        if sys.argv[1] == "encode":
            string = ''
            try:
                f = open(sys.argv[2], 'r')
                for line in f:
                    string += line+'\n'
                f.close()
                EncodeHuffman(string, sys.argv[2])
            except:
                print("Arquivo não encontrado, tente novamente")
        elif sys.argv[1] == "decode":
            print("decode")
            print("Tentando decodificar o arquivo: "+sys.argv[2])
            f = open(sys.argv[2],'r')
            argumentos = {}
            count = 0
            for line in f:
                argumentos[count] = line
                count +=1
            DecodeHuffman(argumentos[0],argumentos[1],sys.argv[2])
        else:
            error()

            
    else:
        error()

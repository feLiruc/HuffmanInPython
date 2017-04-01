import json
import heapq

def DecodeHuffman(tree, input, nomeArquivo):
    d = {}
    d = json.loads(tree.replace("'",'"'))
    j = [(v,k) for k,v in d.items()]
    count = 0
    test = ''
    finalString = ''
    while count != len(input):
        test += input[count]
        count += 1
        if([x for x in j if test in x]):
            finalString += (str([x[1] for x in j if test in x]))
            test = ''
    print(finalString)

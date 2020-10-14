from decrypt import vigenere_second
from decrypt import constants

import csv
import sys
sys.dont_write_bytecode = True

if __name__ == "__main__":
    with open("input/cryptogram.txt", mode="r") as f:
        message = f.read()

    differenceDict = {}
    with open("input/explore_vigenere_input.csv", mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            differenceDict[int(row[0])-1] = int(row[1])

    with open('output/vigenere_result.txt', mode='w') as f:
        for offset in range(26):
            offsetDict = {}
            for key in differenceDict:
                offsetDict[key] = (differenceDict[key] + offset) % 26
            encryptionKey = []
            for key in offsetDict:
                encryptionKey.append(constants.alphabet[offsetDict[key]])
            f.write(str(encryptionKey) + ' : ' + vigenere_second.VigenereProcessor(message, offsetDict).run() + '\n\n')

from decrypt import vigenere_second

import csv
import sys
sys.dont_write_bytecode = True

if __name__ == "__main__":
    with open("input/cryptogram.txt", mode="r") as f:
        message = f.read()

    differenceDict = {}
    with open("input/explorer_vigenere_input.csv", mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            differenceDict[int(row[0])-1] = int(row[1])

    with open('output/vigenere_result.txt', mode='w') as f:
        for offset in range(26):
            offsetDict = {}
            for key in differenceDict:
                offsetDict[key] = (differenceDict[key] + offset) % 26
            f.write(str(offset) + ' : ' + vigenere_second.VigenereProcessor(message, offsetDict).run() + '\n\n')

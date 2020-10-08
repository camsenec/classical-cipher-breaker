import os
import sys
import csv
import re

class SubstituteSolver(object):
    def __init__(self, message, datadir='data/'):
        self.ciphertxt = message
        self.datadir = datadir
        self.__load_data()


    def __load_data(self):
        f = open(os.path.join(self.datadir, 'letterfreq.csv'))
        dr = csv.reader(f)
        letterfreqs = {}
        for entry in dr:
            letterfreqs[entry[0]] = float(entry[1])
        f.close()
        self.letterfreqs = sorted(letterfreqs.items(), key=lambda x:x[1],reverse=True)
        f.close()

    def __getFrequencyOfText(self, inputText):
        text = ''.join(inputText.lower().split())
        frequency = {}
        for letter in text:
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
        return frequency


    def __sanity(self):
        if len(self.letterfreqs) != 26 or len(self.cipherfreqs) != 26:
            print('Number of letters != 26.  Exiting.')
            sys.exit(-1)

    def __keygen(self):
        self.__sanity()
        key = {}
        for x in range(0,26):
            #Confirm that both cipher freqs and letter freqs are sorted
            k = self.cipherfreqs[x][0]
            v = self.letterfreqs[x][0]
            key[k] = v

        return key

    def __decrypt(self, key):
        new_message = ''
        for letter in self.ciphertxt:
            if re.match('[A-z]', letter):
                new_message += key[letter.lower()]
            else:
                new_message += letter
        return new_message.upper()

    def run(self):
        self.cipherfreqs = sorted(self.__getFrequencyOfText(self.ciphertxt).items(), key=lambda x:x[1],reverse=True)
        self.key = self.__keygen()
        print(self.cipherfreqs)
        print(self.letterfreqs)
        return self.key, self.__decrypt(self.key)

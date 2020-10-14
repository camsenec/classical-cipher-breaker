from string import ascii_lowercase
from decrypt import shift
from decrypt import constants


class VigenereSolver(object):
    def __init__(self, message):
        self.ciphertxt = message

    def __getFrequencyOfText(self, inputText):
        text = ''.join(inputText.lower().split())
        frequency = {}
        for letter in text:
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
        return frequency

    def __calculateIC(self, partialText):
        partialText = ''.join(partialText.lower().split())
        # maps characters to their frequencies
        frequency = self.__getFrequencyOfText(partialText)
        ic = 0.0
        for letter in ascii_lowercase:
            if letter in frequency:
                ic += frequency[letter] * (frequency[letter] - 1)

        ic /= len(partialText) * (len(partialText) - 1)
        return ic

    def __calculateMuturalIC(self, partialTextX, partialTextY):
        textX = ''.join(partialTextX.lower().split())
        textY = ''.join(partialTextY.lower().split())
        # maps characters to their frequencies
        frequencyX = self.__getFrequencyOfText(textX)
        frequencyY = self.__getFrequencyOfText(textY)
        ic = 0.0
        for letter in ascii_lowercase:
            if letter in frequencyX and letter in frequencyY:
                ic += frequencyX[letter] * frequencyY[letter]

        ic /= len(textX) * len(textY)
        return ic

    def __extractPartialTexts(self):
        icList = []
        for m in range(1, len(self.ciphertxt)):
            lengthOfKey = m
            # create dictionary of each sequence generated by a key of this length
            averageIC = 0.0
            sequenceDictionary = {}
            for index in range(len(self.ciphertxt)):
                sequenceNumber = index % lengthOfKey
                if sequenceNumber in sequenceDictionary:
                    sequenceDictionary[sequenceNumber] += self.ciphertxt[index]
                else:
                    sequenceDictionary[sequenceNumber] = self.ciphertxt[index]

            hadZeroError = False
            for stringSequence in sequenceDictionary.values():
                try:
                    averageIC += self.__calculateIC(stringSequence)
                except ZeroDivisionError:
                    hadZeroError = True
                    break
            if hadZeroError == True:
                averageIC = 0
            else:
                averageIC /= len(sequenceDictionary.keys())
            icList.append(averageIC)

        candidateMList = []
        for i in range(len(icList)):
            if icList[i] <= 0.07 and icList[i] >= 0.06:
                candidateMList.append(i+1)

        estimatedM = min(candidateMList)
        return estimatedM


    def __findDifferenceOfKeys(self, lengthOfKey):
        pairOfShiftKeys = []
        candidatePairList = []
        sequenceDictionary = {}
        for index in range(len(self.ciphertxt)):
            sequenceNumber = index % lengthOfKey
            if sequenceNumber in sequenceDictionary:
                sequenceDictionary[sequenceNumber] += self.ciphertxt[index]
            else:
                sequenceDictionary[sequenceNumber] = self.ciphertxt[index]

        #log
        print("\n\n[Vigenere Cipher] Partial Texts")
        for key in sequenceDictionary.keys():
            print("Y", key+1, ":", sequenceDictionary[key], '\nI.C.:', round(self.__calculateIC(sequenceDictionary[key]),3), '\n')

        #iterate through both sequence
        for indexI in sequenceDictionary.keys():
            for indexJ in sequenceDictionary.keys():
                for g in range(len(constants.alphabet)):
                    mutualIC = self.__calculateMuturalIC(sequenceDictionary[indexI], shift.ShiftSolver(sequenceDictionary[indexJ], g).run())
                    if(indexI < indexJ):
                        candidatePairList.append([indexI+1, indexJ+1, g, mutualIC])

        #log
        print("\n\n[Vigenere Cipher] Mutual IC")
        for pair in candidatePairList:
            print("Y" + str(pair[0]) + ", Y" + str(pair[1]) + ", g =", str(pair[2]) + ", Mutual I.C. =", pair[3])

        epsilon = 0.0005
        pairOfShiftKeys = []
        while True:
            pairOfShiftKeys.clear()
            for candidatePair in candidatePairList:
                if candidatePair[3] <= 0.065+epsilon and candidatePair[3] >= 0.065-epsilon:
                    pairOfShiftKeys.append(candidatePair)

            if len(pairOfShiftKeys) >= lengthOfKey*2:
                break

            epsilon += 0.0005

        return pairOfShiftKeys

    def __decrypt(self):
        m = self.__extractPartialTexts()
        pairOfShiftKeys = self.__findDifferenceOfKeys(m)
        return m, pairOfShiftKeys

    def run(self):
        return self.__decrypt()

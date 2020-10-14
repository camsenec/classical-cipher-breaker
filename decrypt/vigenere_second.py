from decrypt import constants

class VigenereProcessor(object):
    def __init__(self, message, offsetDict):
        self.ciphertxt = message
        self.offsetDict = offsetDict

    def __decrypt(self):
        newMessage = ''
        keyLength = len(self.offsetDict)
        index = 0

        for letter in self.ciphertxt:

            letter = letter.lower()

            if letter.isalpha():
                shiftPos = constants.alphabet.index(letter) - self.offsetDict[index % keyLength]
                new_pos = constants.alphabet[shiftPos % 26]
                newMessage += new_pos

            elif letter in ' \t\n':
                newMessage += letter

            elif letter.isnumeric():
                newMessage += letter

            else:
                print('An error took place in recording the message. Check input.\n')

            index = index + 1

        return newMessage.upper()

    def run(self):
        return self.__decrypt()

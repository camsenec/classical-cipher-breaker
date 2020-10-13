from decrypt import constants

class ShiftSolver(object):
    def __init__(self, message, offset):
        self.ciphertxt = message
        self.offset = offset

    def __decrypt(self):
        newMessage = ''

        for letter in self.ciphertxt:

            letter = letter.lower()

            if letter.isalpha():
                shiftPos = constants.alphabet.index(letter) - self.offset
                new_pos = constants.alphabet[shiftPos % 26]
                newMessage += new_pos

            elif letter in ' \t\n':
                newMessage += letter

            elif letter.isnumeric():
                newMessage += letter

            else:
                print('An error took place in recording the message. Check input.\n')

        return newMessage.upper()


    def run(self):
        return self.__decrypt()

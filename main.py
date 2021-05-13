from decrypt import constants, shift, substitute, vigenere

import sys
sys.dont_write_bytecode = True

if __name__=='__main__':

    with open("input/cryptogram.txt", mode="r") as f:
        message = f.read()

    with open('output/result.txt', mode='w') as f:
        #Shift
        print("Shift Cipher Decryption")
        f.write('Shift\n')
        f.write('-----------------------------------------------------------\n')
        for offset in range(len(constants.alphabet)):
            f.write(str(offset) + ' : ' + shift.ShiftSolver(message, offset).run() + '\n\n')
        print("Shift Cipher Decryption Completed")
        print("Check output/results.txt\n")

        #Substitute
        print("Substitute Cipher Decryption")
        f.write('\nSubstitute\n')
        f.write('-----------------------------------------------------------\n')
        substitute_key, shifted_by_substitute = substitute.SubstituteSolver(message).run()
        f.write('Keys : ' + str(substitute_key) + '\n')
        f.write(str(shifted_by_substitute) + '\n')
        print("Substitute Cipher Decryption Completed")
        print("Check output/results.txt")


        #Vigenere
        print("Vigenere Cipher Decryption")
        f.write('\nVigenere\n')
        f.write('-----------------------------------------------------------\n')
        m, pairOfShiftKeys = vigenere.VigenereSolver(message).run()
        f.write("the number of keys m is " + str(m) + '\n')
        f.write(str(pairOfShiftKeys) + '\n')
        f.write('============> Calculate Manually!!')
        print("\nThe result is saved to 'output/result.txt'")
        print("After calculation and input to 'explore_vigenere_input.csv', excecute 'python explore_vigenere.py'")
        print("[Details] https://github.com/thanatoth/classical-cipher-breaker/blob/master/README.md#classical-cipher-breaker")

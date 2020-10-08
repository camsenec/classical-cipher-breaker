import constants
import shift
import substitute
import vigenere

import sys
sys.dont_write_bytecode = True

#0. File Open
try:
    with open('output/result.txt', mode='x') as f:
        f.write('')
except FileExistsError:
    with open('output/result.txt', mode='w') as f:
        f.write('')

if __name__=='__main__':

    message = 'XHWLISAMYALBSNKTWRWVELDXHBQIPALHENVTWVAOMDDRECLXHUHHRBQVSRLXDHSOIAUHQMGGENVBRTWKISLBRGMGHEJECIFZPOYBGNGMMCWMLALMLEKHPDAXVSSKINGMQOLBZALXHTGKITJXETBNWTGKIVWGQAAGPYTRXHWBVRSMMOFTPAKLISKFINLHJTZXHAFZIRKHJBSMXLWTRDTRXHWBVSWEJIFMIRWLXRSMLEJMLEQWMSUHZEJTWOMGHRWTWOFMSRMGEWSRFYJXELASMNYMLALPLALBXMSDISKXRSWYSRLAIMLHHOVXTEFWWOFPLALBXWAEPMSDISWGWEXHVOLAIRKMSDGTRDLAETSEPOXMLEGMLEJLGAFGSTAVITZBWTGHIVWGEQMBXETKEVWLSLVBIRETCPJXJEJMSRMGVALAIRLAENZXVOAVELDRFULISIFMPEKLPYVBITJRMNYMSSLXQTZXSNUHQIFZXIVXELDUCHAFWEDYXHMLAEUHYLVBQAYBREOBXHGNXCGGXRSWMCLBSNSVMRUNQSLTRCWBRWZBGHSGERERELDHJWZHWEEXQBWKWAJXFRSOIFDXISSMXOHLTEWWFEXHVELAIEFXQYETOEKTQONXMFLAISGEHIWKWRWTPLQTVETKEVWMLEFMLIKLYRWECIKGXTZXSULVSMWTRYGYXHWFAAFMIDWTGHOHYLVAEVWIVEXXVRWWXHSMELDLXAFWENVYMGZMAHSMAEZTZEZXVELAINALECSLIIFPLIUAXHWBRTWKECLBSNGYQAFRMNVBZIVNELDRVALBSNSEHEUBWIGGQACBRGHKSCWLWEKHREHKSCWLWPWKWODWMEJIVOVNGEKTROMMGOEXMNLXRDWWFYFHSNWFSSLTVMAXWTJRXOSOSIVMLIKIVOTEIMBNWTSLGOJMIZVBHSAGGELAIYUTRTMLYADECMSDIRWMVESMTHQLMCSEPYAFTOKLMBDXXHWRQACXMTWVSNGFMCSEPYAFTOKLMBDXXHWRWHGHXDWLIRLXVSLAINKMENVBRGSGHFAZLTAGKIKXECZLSLVBIRKBRDAOMDMTPLQKETAHRADVSUJLIOXTGTAHRAXMIRSEPBWVEUKXXHWVSSLHJRMGRIFZMSKNVELHFESMPESLXAKAMGZTWTZXGOKMSFKMEYAGK'

    with open('output/result.txt', mode='a') as f:
        #Shift
        f.write('Shift\n')
        f.write('-----------------------------------------------------------\n')
        for offset in range(len(constants.alphabet)):
            f.write(str(offset) + ' : ' + shift.ShiftSolver(message, offset).run() + '\n\n')

        #Substitute
        f.write('\nSubstitute\n')
        f.write('-----------------------------------------------------------\n')
        substitute_key, shifted_by_substitute = substitute.SubstituteSolver(message).run()
        f.write('Keys : ' + str(substitute_key) + '\n')
        f.write(str(shifted_by_substitute) + '\n')

        #Vigenere
        f.write('\nVigenere\n')
        f.write('-----------------------------------------------------------\n')
        pairOfShiftKeys = vigenere.VigenereSolver(message).run()
        f.write(str(pairOfShiftKeys) + '\n')
        f.write('============> Calculate Manually!!')

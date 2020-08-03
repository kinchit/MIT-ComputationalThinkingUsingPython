import string

def build_shift_dict(shift):
    letter_dict = {}
    lowerLetters = string.ascii_lowercase
    upperLetters = string.ascii_uppercase
    lowCh = 97
    upCh = 65
    if (shift >= 0 and shift < 26):
        for i in range (97,123):
            letter_dict[chr(i)] = chr((ord(chr(i))+shift))
            if letter_dict[chr(i)] not in lowerLetters:
                letter_dict[chr(i)] = chr(lowCh)
                lowCh += 1
        for i in range (65,91):
            letter_dict[chr(i)] = chr((ord(chr(i))+shift))
            if letter_dict[chr(i)] not in upperLetters:
                letter_dict[chr(i)] = chr(upCh)
                upCh += 1
        print(letter_dict)
        return letter_dict

def apply_shift(shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        referDict = build_shift_dict(shift)
        message_text = "Hello, My Name is Kinchit"
        new_text = ''
        length = len(message_text)
        for i in range(0,length):
            if message_text[i] in referDict:
                new_text += referDict[message_text[i]]
            if message_text[i] == ' ':
                new_text += ' '
            if message_text[i] in string.punctuation:
                new_text += message_text[i]
            if message_text[i] in string.digits:
                new_text += message_text[i]   
        print(new_text)

message_text = "Hello, My Name is Kinchit"
build_shift_dict(5)
apply_shift(5)





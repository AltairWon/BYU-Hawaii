def encrypt(plaintext, numeric):
    #put the cipher in blank for clearing previous encrypt
    cipher = ''
    for char in plaintext: 
        # if the character of text is blank
        if char == ' ':
            #set cipher as blank
            cipher += char
        #if the character of text is uppercase
        elif  char.isupper():
            #put ASCII code uppsercase
            #ord is convert character to ASCII number
            #mod 26 and add 65 for uppercase 'A'
            cipher = cipher + chr((ord(char) + numeric - 65) % 26 + 65)
        else:
            #put ASCII code lowercase
            #mod 26 and add 97 for lowercase 'a'
            cipher = cipher + chr((ord(char) + numeric - 97) % 26 + 97)
  
    return cipher
#input the plain text and numeric key
text = input()
k = int(input())
print("ciphertext: ", encrypt(text, k))

#set the alphabets for decoding of encrypt
ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(ALPHABETS)):
    translated = ''
    for symbol in encrypt(text, k):
        if symbol in ALPHABETS:
            #find the numbers of symbol of alphabets
            num = ALPHABETS.find(symbol)
            #set number negative the length of alphabets
            num = num - key
            #if the number is lower than 0
            if num < 0:
                #set number to add the length of alphabets
                num = num + len(ALPHABETS)
            #add the num of symbol of the translated
            translated = translated + ALPHABETS[num]

        else:
            #add the symbol 
            translated = translated + symbol
    #print the key number and translated decode
    print('Key: %s  decodes to: %s' % (key, translated))



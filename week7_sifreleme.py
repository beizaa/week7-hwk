#Şifreleme Uygulaması
#Kullaniciya iki secenek sunarak orjinal metni sifreli metne ve
#sifreli metni orjinal
#metne donusturebilen bir program yazmanizi istiyoruz. 
#Sozlukler yardimi ile bir sifreleme algoritmasi olusturun ve
#kullanicidan alacaginiz inputu bu algoritma yoluyla sifreleyin 
#ve ekrana yazdirin. Kullanici daha sonra bu sifreli metni
#input olarak yazdiginda orjinal metne ulasabilsin.



#SYNTAX ERROR, INVALID CHARACTER IN IDENTIFIER VERIYOR.
#CALISMIYOR



CODE_DICT = { 'A':'Q', 'B':'W',
                    'C':'E', 'D':'R', 'E':'T',
                    'F':'Y', 'G':'U', 'H':'I',
                    'I':'O', 'J':'P', 'K':'A',
                    'L':'S', 'M':'D', 'N':'F ',
                    'O':'G', 'P':'H', 'Q':'J',
                    'R':'K', 'S':'L ', 'T':'Z',
                    'U':'X', 'V':'C', 'W':'V',
                    'X':'B', 'Y':'N', 'Z':'M'
              }


print("\n Welcome to the encrypting program!!!\n")
while True:
    choice = input(" Please press 1 to encrypt, press 2 to decipher.")
​
    if choice == "1":
        text = input("Please enter the plain text you would like to encrypt:\n").upper() 
        password = ""
        for letter in text:
            if letter != " ":
                password += CODE_DICT[letter] + " "       
            else:
                password += " "
        print(password)
​
    if choice == "2":
        text = input("Please enter the text you would like to decipher:\n")
        text += " "
        decipher = ""
        code_let = ""
​
        for letter in text:
            if letter != " ":
                i = 0
                code_let += letter
            else:
                i += 1 
                if i == 2:
                    decipher += " "            
                else:
                    decipher += list(CODE_DICT.keys())[list(CODE_DICT.values()).index(code_let)] #CODE_DICT.keys() = bize anahtarlari verir
                    code_let = ""                                                                                #Buradda basina da list koyunca liste oldu
​                                                                                                                #CODE_DICT.values() = bize anahtarlari verir
        print(decipher)

        #sozlukte anahtardan degere ulasabiliyrum ama degerden anahtara ulasamiyorum. Bunun icin
        #anahtar ve degerler icin iki liste olusturdum, ve burada da listeler olustu.
        # 2 liste yapabiliriz, ayri ama ya da boyle yapabiliriz.
        #bunlarin liste halleinde indexleri ayni oldugundan bu sekidle karsilikli kullanilir.
​


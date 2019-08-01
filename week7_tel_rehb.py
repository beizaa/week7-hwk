#telefon rehberi uygulamasi
#Bu odevde bir telefon rehberi simulasyonu yapmanizi istiyoruz.
#Program acildiginda kullaniciya, rehbere kisi ekleme, kisi silme,
#kisi isim ya da tel bilgisi guncelleme, 
#rehberi listeleme seceneklerini sunun.
#Kullanicinin secimine gore gerekli inputlarla programinizi sekillendirin.
#Olusturulan rehberi bir dosyaya kaydedin.
#Rehberi olustururken sozlukleri kullanin.

#with open("dosya.txt","r+") as f:
#    veri=f.readlines()

#DOSYAYA YAZDIRAMADIM.CUNKU VAKIT BULAMADIM BELKII YAPABILIRDIM.

phone_book = { 'beyza' : '061234567',
               'kubra' : '062345678',
               'gamze' : '063456789'
               }

counter = 1

while counter <=100:
    
    option = input(""" Welcome to the telephone book! Dear user, you
    may here add people to or delete them from your directory. You can
    also update their names or numbers and display all the numbers you have
    as a list:
            Press    1    to add people,
            press    2    to delete a person from your book,
            press    3    to update a number,
            press    4    to update a name,
            press    5    to list the whole directory. """)


    
    if option == "1":    
        print("""Adding a person. Please fill in the name
        and the number of the person you want to add, below.""")
        add_name   = input("Name: ")
        add_number = input("Number: ")
        new_person  = {add_name: add_number}
        #phone_book[ add_name ] = add_number    #to add a new item to the dict
    
        phone_book.update(new_person)           #to add the new item and then update the list
        print( add_name, "is succesfully added to your phone book.")
        print( phone_book )
        counter += counter + 1
        
    
    elif option == "2":   
        print("""Deleting a person. Please fill in the name
        or the number of the person you want to delete, below.""")
        del_name   = input("Name: ")
        
        phone_book.pop(del_name)   #to delete the indicated key-value couple
        print( del_name, "is succesfully deleted from your phone book.")
        print( phone_book )
        counter += counter + 1
        

    elif option == "3":                       
        print("""Updating a number. Please fill in below the person's name,
        and new number whom you want to update its number respectively.""")   #to update the value of a key
        
        whose_number = input("Name: ")
        updated_number = input("Number: ")
        #to change a value (key stays the same)
        phone_book[ whose_number ] = updated_number
        
        #
        #phone_book[ upd_name ] = upd_number
        print(  whose_number, "'s phone number has succesfully updated to",updated_number, " in your phone book.")
        print( phone_book )
        counter += counter + 1



    elif option == "4":
        print(""" Updating a name. Please fill in the name
        and the number of the person you want to update its name below.""")   #to update a key 

        oldnametochange   = input("Name of the person you want to change: ")
        
        phone_book[ oldnametochange ]

        phone_book.get(oldnametochange)    

        whose_number = phone_book.get(oldnametochange)
        
        print(phone_book.get(oldnametochange, 'no key'))
        
        new_name = input("New name: ")
        #how to change the key (value stays the same)
        
        
        #format methoduyla
        phone_book[ new_name ] = whose_number
        phone_book.pop(oldnametochange) #sonrasinda eski ikiliyi silmesi ;azim listeden
        
        print( oldnametochange, " 's name succesfully updated to ", new_name, "in your phone book.")
        print( phone_book )
        counter += counter + 1

        
    elif option == "5":  
        print("Listing the directory.")      
        for key, value in phone_book.items():
            print("{} = {}".format(key, value))       
       
       
        counter += counter + 1
    else:
        print("Wrong entrance, please try again. ")



#veri=f.readlines()
#f.seek(5)
#f.write("Sehri Gokcan\t 0987 342 43 21\n"+veri)
#veri.insert(2,"Sedat Koz\t 09876 656 65 76")
#f.seek(0)
#f.writelines(veri)
#print(veri)

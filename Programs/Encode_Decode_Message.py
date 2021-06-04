import base64

file_name = input("Enter you File Name ( without extensions ): ")

while True:
    
    en_or_de = input("Encode or Decode ( E or D or quit ): ")

    if en_or_de == "E" or en_or_de == "e":

        with open(f"{file_name}.txt", 'w') as f:
            Enmessage = input("Message: ")
            encode_message = base64.b64encode(Enmessage.encode('ascii'))
            f.write(encode_message.decode('ascii'))
            print(f"\nSuccessfully your Message is Encoded and Saved in {file_name}.txt\n")
        
    
    elif en_or_de == "D" or en_or_de == "d":
        with open(f"{file_name}.txt", 'r+') as f:
            Demessage = f.readline()
            Decoded_Message = base64.b64decode(Demessage.encode('ascii'))
            print(f"\nYour Decoded Message: {Decoded_Message.decode('ascii')}\n")
        
    elif en_or_de == "quit" or en_or_de == "Quit" or en_or_de == "q" or en_or_de == "Q":
        break

    else:
        print("\nEnter Correct Value\n")
        continue
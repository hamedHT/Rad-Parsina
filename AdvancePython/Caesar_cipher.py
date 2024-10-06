class Caesar:
    def __init__(self,plain_text,cipher_text,key):
        self.plain = plain_text
        self.cipher = cipher_text
        self.key = key

    def encoder(self):
        cipher = ""
        for i in self.plain:
            i = chr(ord(i) + self.key)
            cipher = cipher + i
        print(cipher)

    def decoder(self):
        plain = ""
        for i in self.cipher:
            i = chr(ord(i) - self.key)
            plain = plain + i
        print(plain)

def main():
    plain_input = input("enter your plain text: ")
    cipher_input = input("enter your cipher text: ")
    key = int(input("enter key of the text: "))
    test = Caesar(plain_input,cipher_input,key)
    test.encoder()
    test.decoder()

if __name__ == "__main__":
    main()
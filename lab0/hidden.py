class hidden:
# hidden message 1: taked baby meet at bar night or day sometime

    message = ['-'] * 50

    def test0(self, guess, answer):
        if guess == answer:
            print("correct!")
            self.message[3:6] = list('ed ')
        else:
            print("sorry! try again")
        

    def get_phrase(self):
        print("").join("{}".format(i for i in self.message))
    
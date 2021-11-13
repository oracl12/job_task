class Vocabulary:
    def __init__(self):
        self.vocabulary = list()

    def add_words(self, words):
        for i in words.split(" "):
            if i not in self.vocabulary:
                self.vocabulary.append(i)
        print("Word was added successfully")

    def __add__(self, other):#to add objs
        for i in other.vocabulary:
            if i not in self.vocabulary:
                self.vocabulary.append(i)

    def replace_word(self, to_replace, new):
        try:
            self.vocabulary.remove(to_replace)
            self.vocabulary.append(new)
        except:
            print("Vocabulary doesn't have such word to replace")

    def find_all(self, letters):
        count = 0
        for word in self.vocabulary:
            if letters in word:
                count += 1
        print(count,end=" ")

    def print_voc(self):
        if len(self.vocabulary) < 1:
            print("Vocabulary is empty")
        elif len(self.vocabulary) > 6:
            for i in self.vocabulary[:6]:
                print(i, end=", ")
            print("...")
        else:
            for i in self.vocabulary:
                print(i)

    def print_all(self):
        for i in self.vocabulary:
            print(i)

def help_main():
    print("Press 'q' to exit")
    print("Press 'n' to create new vocabulary")
    print("Press 'u' to add vocabularies")
    print("Press 's' to select voc(first created voc will be with index 1,second with index 2...)")
def help_select():
    print("Press 'a' to add word to selected voc")
    print("Press 'b' to replace word in selected voc")
    print("Press 'p' to print current voc")
    print("Press 'pp' to print all in current voc")
    print("Press 'f' to findall special symbols in selected voc")

if __name__ == '__main__':
    voc = list()
    help_main()
    help_select()
    print("Print help to get all commands")
    count = 0
    while True:
        try:
            string = str(input("Choose action: "))
            if string == "q":
                print("Exit... ")
                break
            if string=="help":
                help_main()
            elif string == "n":
                voc.append(Vocabulary())
                print(f"You successfully create voc with index: {count + 1}")
            elif string=="u":
                vo1 = int(input("First: "))
                vo2 = int(input("Second: "))
                print(f"You choosed {vo1} and {vo2} vocs")
                voc[vo1-1]+voc[vo2-1]
            elif string == "s":
                print("---------------------------------------")
                print("Write index of voc you wont to select: ")
                selected = int(input())
                print(f"You select voc with index:{selected}")
                while True:
                    print("-------------------------------------")
                    select = str(input())
                    if select == "q":
                        break
                    if select == "help":
                        help_select()
                    if select == "p":
                        voc[selected-1].print_voc()
                    if select == "pp":
                        voc[selected - 1].print_all()
                    if select == "a":
                        print("Example: word1 word2 word3 word5")
                        words=str(input("Words to add: "))
                        voc[selected-1].add_words(words)
                    if select == "b":
                        word1=str(input("Word to replace: "))
                        new=str(input("New word: "))
                        voc[selected-1].replace_word(word1,new)
                    if select == "f":
                        spec = str(input("Special symbol: "))
                        voc[selected - 1].find_all(spec)
                        print("words")

            count += 1
        except:
            print("Something goes wrong, check all pls")

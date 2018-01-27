"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']


def parse_names():
    names_txt = open("p022_names.txt","r")
    names_strings = names_txt.read().split(",")
    names_strings.sort()
    names = []
    for i in range(0,len(names_strings)):
        new = name(names_strings[i][1:-1],i+1)
        names.append(new)
    return names

def calculate_total_score(names):
    total = 0
    for name in names:
        total += name.score
    return total


class name():
    def __init__(self,name, list_position):
        self.name= name
        self.alphabetic_value = self.get_alphabetic_value()
        self.alphabetical_position = list_position
        self.score = list_position * self.alphabetic_value

    def get_alphabetic_value(self):
        sum = 0
        for char in self.name.lower():
            new= ord(char)
            if 65 <= new <= 90:
                # Upper case letter
                sum+= new - 64
            elif 97 <= new <= 122:
                # Lower case letter
                sum+= new - 96
            # Unrecognized character
        return sum


def main():
    names = parse_names()
    print("Total score:%d"%calculate_total_score(names))

if __name__ == '__main__':
    main()

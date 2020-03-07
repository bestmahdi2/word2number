class mains:
    def __init__(self, text):
        # text = input("enter your number in letters : ")
        self.text = text.lower().replace("-", " ").replace(" and ", " ").replace("  "," ").replace(" hundred", "_hundred").split(" ")
        self.text.append("zero")
        self.num = 0
        self.Million = []
        self.B_Thousand = []
        self.A_Thousand = []
        # print(self.text)

    def Million_seprator(self, text):
        x = 0
        Num_M = 0
        # print(text)
        for i in text:
            if i == "million":
                Num_M = text.index(i)
        new_text = []
        while x < Num_M:
            new_text.append(text[x])
            x += 1
        self.Million = new_text
    def B_Thousand_seprator(self, text):
        x = 1
        Num_M = 0
        Num_T = 0
        for i in text:
            if i == "thousand":
                Num_T = text.index(i)
            if i == "million":
                Num_M = text.index(i)
                x += Num_M
        if "million" not in text:
            Num_M = -1
            x = 0
        new_text = []
        while x < Num_T and x > Num_M:
            new_text.append(text[x])
            x += 1
        self.B_Thousand = new_text
    def A_Thousand_seprator(self, text):
        x = 1
        Num_T = 0
        if "thousand" in text:
            for i in text:
                if i == "thousand":
                    Num_T = text.index(i)
                    x += Num_T
        if "thousand" not in text and "million" in text:
            for i in text:
                if i == "million":
                    Num_T = text.index(i)
                    x += Num_T
        if "thousand" not in text and "million" not in text:
            x= 0
            Num_T = -1

        new_text = []
        while x > Num_T and x < len(text):
            new_text.append(text[x])
            x += 1
            self.A_Thousand = new_text
    def counter(self, text , sep):
        all_dic = {"a_hundred": 100,"one_hundred": 100, "two_hundred": 200, "three_hundred": 300, "four_hundred": 400,
                   "five_hundred": 500, "six_hundred": 600, "seven_hundred": 700, "eight_hundred": 800,
                   "nine_hundred": 900,
                   "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
                   "ninety": 90,
                   "ten": 10,"zero" : 0 ,"a" : 1,"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
                   "nine": 9,
                   "eleven": 11, "twelve": 12, "thirteen": 13, "forteen": 14, "fifteen": 15, "sixteen": 16,
                   "seventeen": 17, "eighteen": 18, "nineteen": 19}
        textlist = []
        textlist = text.split(" ")
        for i in textlist:
            self.num += all_dic[i] * sep

    def duplicate_error(self , text):
        Rhundred = 0
        Rtens = 0
        Rteens = 0
        Rones = 0

        hundred = ["one_hundred","two_hundred","three_hundred","four_hundred","six_hundred","seven_hundred",
                   "eight_hundred","nine_hundred"]
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "ten", ]
        ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

        for i in text:
            if i in hundred:
                Rhundred +=1
            if i in tens:
                Rtens += 1
            if i in teens :
                Rteens += 1
            if i in ones:
                Rones += 1
        if Rhundred > 1 or Rones > 1 or Rteens> 1 or Rtens> 1 :
            self.dup = "yes"
        else:
            self.dup = "no"

    def results(self):
        s = " "
        if "million" in self.text :
            self.Million_seprator(self.text)
            million_str = s.join(self.Million)
            self.counter(million_str, 1000000)
            self.duplicate_error(self.Million)

        if "thousand" in self.text :
            self.B_Thousand_seprator(self.text)
            b_thousand_str = s.join(self.B_Thousand)
            self.counter(b_thousand_str, 1000)
            self.duplicate_error(self.B_Thousand)

        self.A_Thousand_seprator(self.text)
        a_thousand_str = s.join(self.A_Thousand)
        self.counter(a_thousand_str , 1)
        self.duplicate_error(self.A_Thousand)
if __name__ == "__main__":
        pass
        # s = Ui()
        # try:
        #     m = mains("two million")
        #     m.results()
        #     print(m.num)
        # except :
        #     print("wrong entrance")


from collections import OrderedDict

max_weight = 0  #used to calculate maximum number of words in pages and queries for weight
global_word_list = {} #for storing words and the page names they have occured in dictionary
global_pages_list = {} # for storing pages per thier page names in dictionary
global_queries_list = [] #used to store queries in list
class Company:
    def __init__(self):
        self.name = ""
        self.word_list = {}
        self.count = 0
        self.listOfWords =[]
        self.sum = 0

    def getName(self):
        return self.name

    def getWordList(self):
        return self.word_list

    def setName(self, name):
        self.name = name

    def setCount(self,count):
        self.count = count

    def setList(self,words):
        self.listOfWords = words

    def addToList(self):
        for word in self.listOfWords:
            if word not in self.word_list:
                self.word_list[word] = self.count
                self.count -= 1

def add_to_global(words, pageName):
    for word in words:
        if word in global_word_list:
            global_word_list[word].append(pageName)
        else:
            global_word_list[word] = [pageName]

def create(value,i,type):
    page = Company()
    words = value.split()
    findMaximum(len(words))
    page.setList(words)
    if type == 'p':
        page.setName("P" + str(i + 1))
        add_to_global(words, page.getName())
        global_pages_list[page.getName()] = page
    else:
        page.setName("Q" + str(i + 1))
        global_queries_list.append(page)

def findMaximum(number):
    global max_weight
    if max_weight < number:
        max_weight = number
def searchMain():
    for query in global_queries_list:
        visited =[]
        d ={}
        for word in query.getWordList():
            if word in global_word_list:
                for page in global_word_list[word]:
                    if page not in visited:
                        visited.append(page)
                        sop = sumOfProducts(query,global_pages_list[page])
                        d[page] = sop
        d = OrderedDict(sorted(d.items(), key=lambda x: (-x[1], (x[0][0], int(x[0][1:])))))
        forPrint(query.getName(),d)
def sumOfProducts(query,page):
    sop = 0
    for qword in query.getWordList():
        if qword in page.getWordList():
            sop = sop + query.getWordList()[qword] * page.getWordList()[qword]
    return sop

def forPrint(name,Dict):
    print(name,':',end=" ")
    if Dict == {}:
        print("NO MATCHES FOUND")
    else:
        i = 0
        for key in Dict.keys():
            if i < 5:
                print(key, end=" ")
                i += 1
            if i >= 5:
                break
        print("")

def weightAssignment():
    for key,page in global_pages_list.items():
        page.setCount(max_weight)
        page.addToList()
    for query in global_queries_list:
        query.setCount(max_weight)
        query.addToList()

def readInput():
        print("Reading input from input.txt file : ")
        f = open('input.txt','r')
        page_index =0
        query_index = 0
        for line in f:
            print(line,end="")
            if line[0] == 'P':
                create(line[1:],page_index,'p')
                page_index += 1

            if line[0] == 'Q':
                create(line[1:],query_index,'q')
                query_index += 1
        print("\n")

if __name__ == '__main__':
    readInput()
    weightAssignment()
    searchMain()

# P Dell Laptop Review
# P Review Laptop
# P Review Dell
# P Laptop
# P HP Laptop
# Q Dell Review
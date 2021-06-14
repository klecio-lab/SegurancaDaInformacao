import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter


def start(url):

    wordlist = []
    #aqui ele pega o html e transforma em string
    source_code = requests.get(url).text

    #baixa o site html
    soup = BeautifulSoup(source_code, 'html.parser')

    # text in given web-page is stored under
    # the <div> tags with class <entry-content>
    #aqui ele pega uma parte especifica do codigo html baixado
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

    '''aqui ele pega todas as plavras que estavam no 'content' e deixa
    minusculas e depois tranforma a string em uma lista'''
    words = content.lower().split()

    for each_word in words:
        wordlist.append(each_word)
    clean_wordlist(wordlist)

def clean_wordlist(worlist):
    #limpa a lista
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\;:<>?/., '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            clean_list.append(word)
        create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

        for key, value in sorted(word_count.items(),
                                 key = operator.intemgetter(1)):
            print("% s : % s " % (key, value))

        c = Counter(word_count)

        top = c.most_common(10)
        print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref+lefbar")






    

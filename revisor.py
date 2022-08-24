import PyPDF2
import re
# coding=utf8
# _*_ coding: utf-8 _*_

pdf_name = input("Insira exatamente o nome do pdf! ")

# pdf_object = open(fr'C:\Users\João Pereira\PycharmProjects\pythonProject1\{pdf_name}.pdf', 'rb')
pdf_object = open(f'{pdf_name}.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_object)
notas_dic = open('BR words-utf8.txt', 'rb')

# separação de nome proprio
# [A-Z]+[a-z]*[-]{1}\n[a-z]*
# espaço apos virgula
# [ ]*[,]
# espaço entre palavras indevido
# [ ]{2,}
# encontrar viuvas
# [\n]\w*$ , atual -> [\n]{1}[a-z]*[.]{1,3}

print(f"Total de páginas: {pdf_reader.numPages}")

choices_dic = {'1': '[A-ZÁ-ÚÂ-ÛÃ-Õ]{1}[a-zá-úã-õâ-ô]*\n{0,2}[ ]*[-]?\n{1,4}[a-zá-úã-õâ-ô]+',
               '2': '[ ]{1}[,]',
               '3': '[A-ZÁ-ÚÂ-ÛÃ-Õ]{0,10}[a-zá-úã-õâ-ô]{0,10}[ ]{2,}',
               '4': '([\n]{1,3}[A-ZÁ-ÚÂ-ÛÃ-Õ]?[a-zá-úã-õâ-ô]*[\W]{0,1}[ ]{0,5}([\w][\s][\d])*)',
               '5': '((http|https)://)([\w-]+\.)+[\w-]+(/[\w ./?%&=])?',
               '6': '(\w)*[-]{1}\n(\w)*', '7': ''}

# [A-ZÁ-ÚÂ-ÛÃ-Õ]{1}[a-zá-úã-õâ-ô]*\n{0,2}[-]?\n{1,4}[a-zá-úã-õâ-ô]+ oficial do 1

def Find(string):
        regex = fr"({choices_dic.get(check_ask)})"
        search1 = re.findall(regex, string, re.MULTILINE)
        # print(regex)
        return [x for x in enumerate(search1, start=1)]


# re.DOTALL|re.MULTILINE
# FIBONACCI_EM_FGB_SERIE1_C1_RED_CE_CAP1_P1

searching = True

while searching == True:
    check_ask = input("\nO que voce gostaria de pesquisar ? \n 1) Separação de nome proprio. \n 2) Espaço antes de virgula. \n"
             " 3) Espaço indevido entre palavras. \n 4) Encontrar viuvas. (versão beta) \n 5) Links \n 6) Corretor ortografico."
                          " (versão beta) \n 7) Palavra estrangeira hifenizada. (em breve) \n 8) Paralelismo. (em breve)"
                          " \n\n Escolha 1,2,3,4,5,6,7 ou 8 !\n")


    for page_number in range(pdf_reader.numPages):
        pageObject = pdf_reader.getPage(page_number)
        pdf_text = pageObject.extractText()
        print(f"Pg:{page_number + 1} {Find(pdf_text)}")
        # print(pdf_text)



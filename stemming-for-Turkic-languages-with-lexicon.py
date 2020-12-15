import re
import os
import xlrd, xlwt

def splitting_by_words(text):
    result = re.findall(r'\w+', text)
    return result

def sorting_affixes(file_name):
    affixes_wb = xlrd.open_workbook(affixes_file_name)
    affixes_sh = affixes_wb.sheet_by_index(0)
    affixes = []
    for rownum in range(affixes_sh.nrows-1):
        affix = affixes_sh.cell(rownum+1,0).value
        if '\ufeff' in affix:
            affix = affix.replace('\ufeff', '')
        affixes.append(affix)

    sorted_affixes = sorted(affixes, key=len, reverse=True)

    return sorted_affixes

def stem(word, affixes, sfile_name):
    stop_stem_file = open(sfile_name, 'r', encoding="utf-8")
    stop_stem_file = stop_stem_file.read()
    stop_stems = splitting_by_words(stop_stem_file)
    
    word_len = len(word)
    min_len_of_word = 2
    stems = []

    if word_len > min_len_of_word:
            n = word_len - min_len_of_word
            for i in range(n+1, 0, -1):
                word_affix = word[word_len - (i-1):]
                stem = word[:word_len-len(word_affix)]
                for affix in affixes:
                    if affix == word_affix:
                        if stem in stop_stems:
                            stems.append(stem)
                        else:
                            break
                    elif affix == '' or word_affix == '':
                            stems.append(word)
    else:
        stems.append(word)
                        
    return stems[0]
    

def stemming(tfile_name, affixes, sfile_name):
    text_file = open(tfile_name, 'r', encoding="utf-8")
    text_file = text_file.read()

    text = splitting_by_words(text_file)
    res_text = []
    for word in text:
        if word not in res_text:
            res_text.append(word)

    stem_text = {}
    for word in res_text:
        stemm = stem(word, affixes, sfile_name)
        stem_text.update({word: stemm})

    for i in stem_text.keys():
        word = str(i)
        stemm = str(stem_text[i])

        if word in text_file:
            text_file = re.sub((rf"\b{word}\b"), stemm, text_file)
       
    return text_file
    

affixes_file_name = input("Name of the affix file: ") #"affixes.xls"
affixes = sorting_affixes(affixes_file_name)
print(affixes)

text_file_name = input("Name of the text file: ") #"text.txt"
stems_file_name = input("Name of the vocabulary of correct stems: ") #"truestems.txt"
text = stemming(text_file_name, affixes, stems_file_name)
print("\n")
print(text)

output_file_name = input("Name of the output file (result): ") #"results.txt"
output_file = open(output_file_name, 'w', encoding="utf-8")
output_file.write(text)
output_file.close()

print("The results of the stemming process are written to a file " + output_file_name + " and saved in the folder where this python file is located")



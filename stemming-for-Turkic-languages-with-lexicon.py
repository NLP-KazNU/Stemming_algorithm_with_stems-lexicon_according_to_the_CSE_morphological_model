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
    

def stemming(tfile_name, affixes, stopwords_file_name, sfile_name):
    text_file = open(tfile_name, 'r', encoding="utf-8")
    text_file = text_file.read()

    with open(stopwords_file_name, "r", encoding="utf-8") as f:
        stopwords_file = f.readlines()
    stop_words = []
    for stop_word in stopwords_file:
        if "\n" in stop_word:
            stop_word = stop_word.replace("\n", "")
        stop_words.append(stop_word)
    #print(stop_words)
        
    text = splitting_by_words(text_file)
    res_text = []
    for word in text:
        if word not in res_text:
            res_text.append(word)

    result_words  = [word for word in res_text if word.lower() not in stop_words]
    #result = ' '.join(result_words)
    
    stem_text = {}
    for word in res_text:
        stemm = stem(word, affixes, sfile_name)
        stem_text.update({word: stemm})
       
    return stem_text
    

stopwords_file_name = input("Name of the stop-words file: ") #"stop_words.txt"

affixes_file_name = input("Name of the affix file: ") #"affixes.xls"
affixes = sorting_affixes(affixes_file_name)
#print(affixes)

text_file_name = input("Name of the text file: ") #"text.txt"
stems_file_name = input("Name of the vocabulary of correct stems: ") #"truestems.txt"
stem_text = stemming(text_file_name, affixes, stopwords_file_name, stems_file_name)
#print("\n")
#print(text)

res_wb = xlwt.Workbook()
res_sh = res_wb.add_sheet("Sheet1")

res_sh.write(0, 0, 'words')
res_sh.write(0, 1, 'stems')
j = 1
for i in stem_text.keys():
    word = str(i)
    stemm = str(stem_text[i])
    res_sh.write(j, 0, word)
    res_sh.write(j, 1, stemm)
    j = j + 1
        
output_file_name = input("Name of the output file (result): ") #"results.xls"
res_wb.save(output_file_name)

print("The results of the stemming process are written to a file " + output_file_name + " and saved in the folder where this python file is located")



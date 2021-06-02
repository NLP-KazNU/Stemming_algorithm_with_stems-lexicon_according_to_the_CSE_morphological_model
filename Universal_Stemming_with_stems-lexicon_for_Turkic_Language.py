import re
import os
import xlrd, xlwt

def splitting_by_words(text):
    result = re.findall(r'\w+', text)
    return result

def sorting_endings(endings_file_name):
    endings_wb = xlrd.open_workbook(endings_file_name)
    endings_sh = endings_wb.sheet_by_index(0)
    endings = []
    for rownum in range(endings_sh.nrows-1):
        ending = endings_sh.cell(rownum+1,0).value
        if '\ufeff' in ending:
            ending = ending.replace('\ufeff', '')
        endings.append(ending)

    sorted_endings = sorted(endings, key=len, reverse=True)

    return sorted_endings

def stem(word, endings, stems_file_name):
    stems_file = open(stems_file_name, 'r', encoding="utf-8")
    stems_file = stems_file.read()
    stems_list = splitting_by_words(stems_file)
    
    word_len = len(word)
    min_len_of_word = 2

    if word_len > min_len_of_word:
        n = word_len - min_len_of_word

        if word.lower() in stems_list:
            rez_stem = word

        else:
            i = n+1
            while i > 0:
                word_ending = word[word_len - (i-1):]
                stem = word[:word_len-len(word_ending)]                         
                for ending in endings:
                    if word_ending == ending:
                        if stem.lower() in stems_list:
                            rez_stem = stem
                            i = 0
                if word_ending == '':
                    if stem.lower() in stems_list:
                        rez_stem = stem
                        i = 0
                    else:
                        j = n+1
                        while j > 0:
                            word_ending = word[word_len - (j-1):]
                            stem = word[:word_len-len(word_ending)]
                            for ending in endings:
                                if word_ending == ending:
                                    rez_stem = stem
                                    j = 0
                                    i = 0
                            if word_ending == '':
                                rez_stem = word
                                j = 0
                                i = 0
                            j = j-1
                i = i-1

    else:
        rez_stem = word
                        
    return rez_stem
    

def stemming(tfile_name, endings, stopwords_file_name, stems_file_name):
    text_file = open(tfile_name, 'r', encoding="utf-8")
    text_file = text_file.read()

    with open(stopwords_file_name, "r", encoding="utf-8") as f:
        stopwords_file = f.readlines()
    stopwords_list = []
    for stop_word in stopwords_file:
        if "\n" in stop_word:
            stop_word = stop_word.replace("\n", "")
        stopwords_list.append(stop_word)
        
    text = splitting_by_words(text_file)
    res_text = []

    rim_cifry = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx', 'xxi', 'xxiv']

    for word in text:
        if word.lower() not in res_text:
            if word.isnumeric() or word.lower() in rim_cifry:
                continue
            res_text.append(word)

    result_words  = [word for word in res_text if word.lower() not in stopwords_list]
     
    stem_text = {}
    for word in result_words:
        stemm = stem(word, endings, stems_file_name)
        stem_text.update({word: stemm})
       
    return stem_text
    

stopwords_file_name = input('''Enter the name of the stop-words file (for example "stop_words.txt"): ''')

endings_file_name = input('''Enter the name of the endings file (for example "affixes.xls"): ''')
endings = sorting_endings(endings_file_name)

text_file_name = input('''Enter the name of the text file (for example "text.txt"): ''')
stems_file_name = input('''Enter the name of the vocabulary of correct stems (for example "truestems.txt"): ''')
stem_text = stemming(text_file_name, endings, stopwords_file_name, stems_file_name)

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
        
output_file_name = "results.xls"
res_wb.save(output_file_name)

print('''The results of the stemming process are written to a file "''' + output_file_name + '''" and saved in the folder where this python file is located''')



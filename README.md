# Stemming algorithm with stems-lexicon according to the CSE (Complete Set of Endings) morphology model
Ualsher Tukeyev, Aliya Turganbayeva

The difference between this algorithm and the previous lexicon-free stemming algorithm is: after the stem is selected, it will be additionally checked for the presence in the language stems' list.
In the following, e(w) is the ending of analyzed word w, st(w) is the stem of w, L(w) is the length of w, L[e(w)] is the calculated length of the ending.
The steps of the stemming algorithm with lexicon are as follows:
1. Calculation L(w).
2. Calculation the maximum length of an ending of the analyzed word: L[e(w)] = L(w) – 2, where 2 is the minimum length of the word stem.
3. Selection of the ending e(w) of the length L[e(w)] for analyzed word w.
4. Search e(w) on matching in the list of endings. If it matches, then the stem of the word is selected: st(w) = w – e(w). 
5. Search stem st(w) on matching in the list of stems of language. If it matches, then go to 8; 
6. Otherwise, calculated length of the ending of the analyzed word is decreased by one: L[e(w)] = L[e(w)] - 1.
7. If L[e(w)] < 1, then word w is without the ending. Go to step 8. Otherwise, go to step 3.
8. End.



Instructions for use


To run a python file (file with the .py extension) you need:

1) open command prompt (CMD)

2) enter the following command (path to the folder where the python file is located):

cd C: \ Users \ ASER \ Desktop \ myprogs \ stemming \ github

3) run the python file specifying the file name:

stemming-for-Turkic-languages.py

4) then enter the name of the files that are requested to run the program

4.1) the name of the excel (.xls) file where the affixes are saved

Name of the affix file: affixes.xls

4.2) the name of the text (.txt) file where the source text is saved

Name of the text file: text.txt

4.3) the name of the text (.txt) file where the correct stems (stems) of words are saved

Name of the vocabulary of correct stems: truestems.txt

4.4) the name of the text (.txt) file where you will write the result (text after the stemming process)

Name of the output file (result): output_results.txt


After executing these commands, an inscription is displayed on the screen where it says that the process was successfully completed and the results were saved

'The results of the stemming process are written to a file output_results.txt and saved in the folder where this python file is located'

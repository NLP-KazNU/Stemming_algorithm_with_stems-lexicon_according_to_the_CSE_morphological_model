# Stemming algorithm with stems-lexicon according to the CSE (Complete Set of Endings) morphological model

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

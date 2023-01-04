from ast import List
from naive_search import naive_search
from kmp_search import kmp_search
from kr_search import kr_search
from utils import get_N_words_from_file, get_text_from_file
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(100)
import gc
gc_old = gc.isenabled() # pobierz aktualny stan odśmiecania
# N = [1000, 2000, 3500, 5000, 7500, 10000]
N = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
Wyniki = []
text = get_text_from_file('pan-tadeusz.txt')

for search in(naive_search, kmp_search, kr_search):
    gc.disable() # wyłącz odśmiecanie
    wynikiTemp = []
    for n in N:
        print(n)
        pattern_list = get_N_words_from_file('pan-tadeusz.txt', n)
        # pattern = "".join(pattern_list)
        start = time.time() # pobierz aktualny czas
        for pattern in pattern_list:
            search(pattern, text)
        # search(pattern, text)
        stop = time.time()
        wynikiTemp.append((stop-start))
    if gc_old: gc.enable()
    Wyniki.append(wynikiTemp)

# for i in range(1,4):
#     gc.disable() # wyłącz odśmiecanie
#     wynikiTemp = []
#     for n in N:
#         pattern_list = get_N_words_from_file('pan-tadeusz.txt', n)
#         start = time.time() # pobierz aktualny czas
#         for pattern in pattern_list:

        
#         if(i==1):
#             naive_search(pat, txt)
#         elif(i==2):
#             kmp_search(pat, txt)
#         elif(i==3):
#             kr_search(pat, txt, 101)
#         stop = time.time()
#         wynikiTemp.append((stop-start))
#     if gc_old: gc.enable()
#     Wyniki.append(wynikiTemp)

plt.plot(N,Wyniki[0],label='Naiwny')
plt.plot(N,Wyniki[1],label='KMP')
plt.plot(N,Wyniki[2],label='KR')
plt.legend()
plt.xlabel("Długość listy")
plt.ylabel("Czas wyszukiwania")
# plt.show()
plt.savefig("porownanie.png")

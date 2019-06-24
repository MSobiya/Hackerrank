#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    '''s = []
    for i in range(len(word)):
        s.append(h[alpha.index(word[i])])
    return max(s)*len(s)'''

    maxi = 0
    for i in range(len(word)):
        if maxi <= h[alpha.index(word[i])]:
            maxi = h[alpha.index(word[i])]
    return maxi * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

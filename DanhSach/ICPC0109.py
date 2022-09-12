import math
import sys
import re

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    # s = input().split(" ")
    # sMin = sys.maxsize
    # tMin = sys.maxsize
    # fMin = sys.maxsize
    # for x in s:
    #     if x == '':
    #         break
    #     x = int(x)
    #     if x < fMin:
    #         tMin = sMin
    #         sMin = fMin
    #         fMin = x
    #     elif x < sMin:
    #         tMin = sMin
    #         sMin = x
    #     elif x < tMin:
    #         tMin = x
    # print(fMin + sMin + tMin)
    ss = input()
    s = re.findall('-?\d+\.?\d*', ss)
    sMin = sys.maxsize
    tMin = sys.maxsize
    fMin = sys.maxsize
    for x in s:
        if x == '':
            break
        x = int(x)
        if x < fMin:
            tMin = sMin
            sMin = fMin
            fMin = x
        elif x < sMin:
            tMin = sMin
            sMin = x
        elif x < tMin:
            tMin = x
    print(fMin + sMin + tMin)
    
    

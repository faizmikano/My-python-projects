for tiptop in range(101):
    if tiptop %3==0 and tiptop %5==0:
        print('tiptop')
        continue
    elif tiptop %3==0:
        print('tip')
        continue
    elif tiptop %5==0:
        print('top')
        continue
    print(tiptop)

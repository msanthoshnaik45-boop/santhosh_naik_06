with open("sample2.txt","w+") as f:
    f.write(''' multiple
lines
demonstration''')
    f.seek(0)
    print(f.read())
    f.seek(0)
    print()
    print(f.readlines())

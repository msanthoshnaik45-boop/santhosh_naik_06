with open("sample2.txt","w+") as f:
    f.writelines(["anil"])
    f.seek(0)
    print(f.read())
    f.seek(0)
    print()
    print(f.readlines())

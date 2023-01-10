def ls(l,el):
    for i in range(len(l)):
        if l[i]==el:
            print("Element Found at", i+1)
            return

    print("Element not found")
    return

l = [1,2,3,4,5,6,7,8,9]
ls(l,6)
 
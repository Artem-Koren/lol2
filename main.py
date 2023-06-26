x = str(input())
def sloth(text):
    a = len(text)
    if a % 2 ==0 :
        s1 = text[:len(text)//2]
        s2 = text[len(text)//2:]
        s3 = s2[::-1]
        if s1 == s3:
            print(True)
        else:
            print(False)
    else:
        print(False)
sloth(x)
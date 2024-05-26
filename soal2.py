#Buatlah fungsi rekursif mengetahui suatu kalimat adalah palindrom atau bukan!
kalimat = str(input("Masukkan kata/angka :"))
def palindrom(kalimat):
    if len(kalimat) < 1:
        return True
    else:
        if kalimat[0] == kalimat[-1]:
            return palindrom(kalimat[1:-1])
        else:
            return False
if(palindrom(kalimat) == True):
    print("Palindrom")
else:
    print("Bukan Palindrom")
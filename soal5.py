#Buatlah fungsi rekursif untuk menghitung kombinasi!
bil1 = int((input("Masukkan bilangan 1 :")))
bil2 = int((input("Masukkan bilangan 2 :")))
def bilangan(bil1, bil2):
    if (bil2 == 0 ):
        return 1
    else:
        int(bil1-bil2+1)
        return (bilangan(bil1,bil2-1) * (bil1-bil2+1))

def kombinasi(bil1, bil2):
    if bil2 == 0:
        return 1
    else:
        int((bil1-bil2+1)/ bil2) 
        return (kombinasi(bil1,bil2-1) * (bil1-bil2+1) / (bil2))
bilangan(bil1, bil2) 
print(kombinasi(bil1, bil2))
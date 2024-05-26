## Buatlah fungsi rekursif untuk menghitung jumlah deret ganjil
# dari 1 + 3 + 7 + . . . + n! 
def deret_ganjil(bil1,bil2):
    if bil1 > bil2:
        return 0
    return bil1 + deret_ganjil(bil1 + 2,bil2)

bil1 = 1
bil2 = int(input("Masukkan limit bilangan (n) :"))
print("Jumlah bilangan ganjil dalam rentang :",deret_ganjil(bil1,bil2))
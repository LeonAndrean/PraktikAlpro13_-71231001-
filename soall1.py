#Vidi adalah adik Tono yang sedang belajar bilangan prima. Vidi mengalami kesulitan
#untuk menentukan suatu bilangan bilangan prima atau bukan. Untuk membantu adiknya
#Tono kemudian membuat program untuk pengecekan bilangan prima dengan menggunakan
#fungsi rekursif. Bantulah Tono untuk menyelesaikan tugas tersebut.
angka = int(input("Tono: Masukkan satu angka bulatmu vidi = "))
def prima(data, pembagian=2):
    if data <= 1:
        return False
    if pembagian * pembagian > data:
        return True
    if data % pembagian == 0:
        return False
    return prima(data, pembagian + 1)
def pembagian_terkecil(data, pembagian=2):
    if data % pembagian == 0:
        return pembagian
    return pembagian_terkecil(data, pembagian + 1)

if prima(angka):
    print(f"Tono: jadi angka-{angka} adalah angka prima")
else:
    pembagi = pembagian_terkecil(angka)
    print(f"Tono: angka-{angka}, bukan angka prima, karena bisa dibagi", pembagi)
angka = int(input("Input sebuah bilangan: "))
def sum_of_digits(angka):
    if angka == 0:
        return 0, ""
    else:
        digit_terhkir = angka % 10
        hasil, digit_pertama = sum_of_digits(angka // 10)
        if digit_pertama:
            return hasil + digit_terhkir, digit_pertama + " + " + str(digit_terhkir)
        else:
            return hasil + digit_terhkir, str(digit_terhkir)

jumlah, digit_string = sum_of_digits(angka)
print(f"Jumlah digit dari bilangan {angka} adalah: {digit_string} = {jumlah}")

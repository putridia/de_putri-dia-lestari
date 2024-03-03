# Program mencetak angka 1 sampai 100 dengan ketentuan tertentu

for i in range(1, 101): # jika bilangan kelipatan 3
    if i % 3 == 0:
        print(i**2)
    elif i % 5 == 0: # jika bilangan kelipatan 5
        print(i**3)
    elif i % 3 == 0 and i % 5 == 0: # jika bilangan kelipatan 3 dan 5
        print("buzz")
    else:
        print(i) #jika kriteria diatas tidak terpenuhi
# Program Memeriksa Kata Anagram atau Bukan

def isAnagram(kata1, kata2):
    # mengubah kata menjadi lowercase dan dictionary
    dict1 = {}
    dict2 = {}
    for i in kata1.lower().replace(" ", ""):
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in kata2.lower().replace(" ", ""):
        if i in dict2:
            dict2[i] += 1
        else:
            dict2[i] = 1

    # membandingkan kedua dictionary
    if dict1 == dict2:
        return True
    else:
        return False

# Input
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

# Cek kata anagram
if isAnagram(kata1, kata2):
    print("Anagram")
else:
    print("Bukan Anagram")
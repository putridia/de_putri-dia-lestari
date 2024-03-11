def collect_chars(word, rooms):
    repeat_times = rooms // len(word)
    remainder = rooms % len(word)
    return word * repeat_times + word[:remainder]

print(collect_chars("alta", 10))  # altaaltaal
print(collect_chars("sepulsa", 20))  # sepulsasepulsasepuls
print(collect_chars("sepulsa mantap", 20))  # sepulsamantapsepulsa
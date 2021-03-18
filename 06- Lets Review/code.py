n = int(input())
strings = []
for i in range(n):
    strings.append(input())
for x in strings:
    srt_string = ""
    for char in x[::2]:
        srt_string += char
    srt_string += " "
    for char in x[1::2]:
        srt_string += char
    print(srt_string)

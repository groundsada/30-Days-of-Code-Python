phonebook = {}
for i in range(int(input())):
    x , y = input().split()
    phonebook.update({x : y})
while (True):
    try:
        string  = input().strip()
    except:
        break
    try:
        print(string + "=" + phonebook[string])
    except:
        print("Not found")

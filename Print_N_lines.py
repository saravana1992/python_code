N = 10
file = open("C:/Users/sdamodharan/Desktop/test.txt", "a")#the a opens it in append mode
for i in range(N):
    line = file.next().strip()
    print(line)
file.close()
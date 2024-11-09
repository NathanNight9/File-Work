N = list(input().split())
NN = []

with open("text.txt", "w") as file:
    for i in N:
        file.write(f"{i}\n\n")
        if i.isnumeric():
            NN.append(int(i))
    
    file.write(str(sum(NN)))
    file.write("\n" + str(max(NN)))

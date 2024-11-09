N = list(map(int, input().split()))

with open("text.txt", "w") as file:
    for i in N:
        file.write(f"{i}\n\n")

    file.write(str(sum(N)))
    file.write(("\n" + str(len(N))))
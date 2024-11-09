N = list(map(int, input().split()))

with open("text.txt", "w") as file:
    for i in N:
        file.write(f"{i}\n\n")

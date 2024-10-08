if len(input().split()) > 1:
    print("none")
else:
    for i in range(11):
        table = []
        for j in range(11):
            table.append(i * j)
        print(f"Table de {i}: {' '.join(map(str, table))}")
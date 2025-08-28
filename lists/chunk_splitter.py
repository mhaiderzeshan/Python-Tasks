list_input = list(map(int, input("Enter the list of integers: ").   split()))

chunk_size = int(input("Enter the chunk size: "))

chunks = []
for i in range(0, len(list_input), chunk_size):
    chunk = list_input[i:i + chunk_size]

    while len(chunk) < chunk_size:
        chunk.append(None)   # type: ignore
    chunks.append(chunk)

print(chunks)

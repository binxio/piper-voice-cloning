import glob
import os

chunks = glob.glob('chunk*.txt')
chunks.sort()

i = 0

# Open metadata.csv and ensure it's empty
with open("metadata.csv", "w") as f:
    pass

for chunk in chunks:
    chunk = chunk.strip()
    i += 1
    with open(chunk, 'r') as file:
        content = file.read().strip().rstrip(".")
    data_line = f"{chunk}|{content}"

    with open("metadata.csv", "a") as f:
        f.write(data_line.replace(".txt", "") + "\n")

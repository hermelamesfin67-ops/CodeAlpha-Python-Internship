import os
import shutil
files = os.listdir("source")
os.makedirs("destination",exist_ok=True)
for file in files:
    if file.lower().endswith(".jpg"):
        source_path = os.path.join("source", file)
        destination_path = os.path.join("destination",file)
        shutil.move(source_path, destination_path)
        print(f"{file} was successfully moved!")

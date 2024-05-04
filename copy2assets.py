import os
import shutil

directory = 'uk'


for filename in os.listdir(directory):
    if filename.endswith(".json"):
        with open(os.path.join(directory, filename), 'r') as file:
            if "{}" in file.read():
                print(f"Skipping file {filename}")
            else:
                modname = filename.split("-")[0]
                # assets/modname/lang/uk.json
                new_path = os.path.join('assets', modname, 'lang', 'uk.json')

                os.makedirs(f"assets/{modname}/lang", exist_ok=True)
                shutil.copy(os.path.join(directory, filename), new_path)

                print(f"File {filename} to {new_path}")

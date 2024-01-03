import os, json

def save_to_json(data, filename):
    # Save coordinates dictionary to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

directory_path = "./spectrum"

datas = {}

try:
    # Get the list of files in the specified directory
    file_list = os.listdir(directory_path)

    # Print the list of files
    print("List of files in the directory:")
    for file_name in file_list:
        datas[file_name] = int(file_name.split("-")[1][1:])
    
    save_to_json(datas, "label.json")

except FileNotFoundError:
    print(f"Directory '{directory_path}' not found.")
except PermissionError:
    print(f"Permission error accessing '{directory_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")

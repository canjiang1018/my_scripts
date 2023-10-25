import os

def process_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if "property list uchar int vertex_index" not in line:
                file.write(line)

def process_directory(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".ply"):
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == "__main__":
    base_dir = "/home/brent/brentj/datasets/1020_self-test"
    process_directory(base_dir)
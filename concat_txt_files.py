import os

def concatenate_text_files(folder_path, output_filename="master.txt"):
    output_path = os.path.join(folder_path, output_filename)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for filename in sorted(os.listdir(folder_path)):
            if filename.endswith(".txt") and filename != output_filename:
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    # outfile.write(f"--- {filename} ---\n")
                    outfile.write(infile.read())
                    # outfile.write("\n\n")  # Add spacing between files
                    outfile.write("\n")  # Add spacing between files

    print(f"All .txt files have been concatenated into: {output_path}")

if __name__ == "__main__":
    folder = input("Enter the folder path containing .txt files: ").strip()
    if os.path.isdir(folder):
        concatenate_text_files(folder)
    else:
        print("Invalid folder path.")

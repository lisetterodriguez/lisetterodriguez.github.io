import sys

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        try:
            input_file = sys.argv[1]

            with open (input_file, "r") as file:
                lines = file.readlines()

            selected_lines = [line for line in lines 
                            if not line.strip().startswith("#") and line.strip() != '']
            line_count = len(selected_lines)
            print(line_count)
        except FileNotFoundError:
            print("File does not exist")
if __name__ == "__main__":
    main()
######-----------------------END OF CODE------------------------######
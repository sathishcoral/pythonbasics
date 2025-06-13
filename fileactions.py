

def main():
    
    # Write
    wfile = open("testdata.txt", "w+")
    for i in range(5):
        wfile.write(f"Writing text into file on line {i}\n")

    # append
    wfile = open("testdata.txt", "a+")
    wfile.write(f"Appending new line at the last.")

    # read file
    file = open("testdata.txt", "r")
    if file.mode == "r":
        data = file.readlines()
        for line in data:
            print(line)
            print("---------------")

    wfile.close() 



if __name__ == "__main__":
    main()
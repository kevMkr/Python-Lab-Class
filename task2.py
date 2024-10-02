def writefile(database):
    datainput= input()
    with open(database,'a') as file:
        file.write(datainput + '\n')
    print('Data saved successfully!')

def readfile(database):
    with open(database, 'r') as file:
        readdata=file.read()
        print('Data in the file')
        print(readdata)

def main():
    database='nonedata.txt'
    while True:
        print("\nMenu:")
        print("1. Write data to file")
        print("2. Read data from file")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            writefile(database)
        elif choice == '2':
            readfile(database)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "main":
    main()
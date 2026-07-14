# file = open('example.txt', 'a+')
# data = file.read()
# print(data)
# file.close()

def read_file(filename):
    file = None
    try:
        file = open(filename, 'r')
        data = file.read()
        print(data)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while trying to read '{filename}'.")
    finally:
        if file:
            file.close()

readfilename = input("Enter the filename to read: ")
read_file(readfilename)
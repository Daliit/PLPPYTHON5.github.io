try:
    # Appending to the file
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line.\n")
        file.write("Another appended line with some numbers: 67890.\n")
        file.write("Final appended line.\n")
        print("Three lines appended to 'my_file.txt'.")

    # Reading from the file
    with open("my_file.txt", "r") as file:
        file_contents = file.read()
        print("\nUpdated contents of 'my_file.txt':")
        print(file_contents)

except FileNotFoundError:
    print("File not found. Please ensure 'my_file.txt' exists.")

except PermissionError:
    print("Permission denied. Please check file permissions.")

finally:
    print("End of the program.")

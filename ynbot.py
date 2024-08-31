def display_yes():
    print("""
  _____
 /      \\
|  YES  |
 _____/
    """)

def display_no():
    print("""
  _____
 /      \\
|  NO   |
 _____/
    """)

def main():
    while True:
        answer = input("Enter yes or no: ").lower()
        if answer == "yes":
            display_yes()
        elif answer == "no":
            display_no()
        else:
            print("Invalid input. Please enter yes or no.")

if __name__ == "__main__":
    main()

student = {}
while True:
    print("\n-----STUDENT MANAGER APP-----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks
        print(f"{name} Successfully Added! ")
        

    # View student
    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(f"{name} : {marks}")

    # Check result
    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]
            
            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")
        else: 
            print("Student Not Found!")

    #exit
    elif choice == "4": 
        print("Exiting....")
        break

    else:
        print("Invalid input")


            



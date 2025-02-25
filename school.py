class User:
    """Base class for users in the system."""
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, username, password):
        return self.username == username and self.password == password


class Teacher(User):
    """Teacher class inherits from User."""
    def __init__(self, username, password):
        super().__init__(username, password)
        self.courses = []

    def create_course(self, course_name):
        course = Course(course_name, self)
        self.courses.append(course)
        return course


class Student(User):
    """Student class inherits from User."""
    def __init__(self, username, password):
        super().__init__(username, password)
        self.enrolled_courses = []

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)


class Course:
    """Course class to manage course details."""
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class SchoolManagementSystem:
    """Main class for the school management system."""
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []

    def create_teacher(self, username, password):
        teacher = Teacher(username, password)
        self.teachers.append(teacher)
        return teacher

    def create_student(self, username, password):
        student = Student(username, password)
        self.students.append(student)
        return student

    def find_user(self, username, password):
        for user in self.teachers + self.students:
            if user.authenticate(username, password):
                return user
        return None


# Main program
if __name__ == "__main__":
    sms = SchoolManagementSystem()

    while True:
        print("\n--- School Management System ---")
        print("1. Register as Teacher")
        print("2. Register as Student")
        print("3. Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("--- Teacher Registration ---")
            username = input("Enter username: ")
            password = input("Enter password: ")
            sms.create_teacher(username, password)
            print("Teacher account created successfully!")

        elif choice == "2":
            print("--- Student Registration ---")
            username = input("Enter username: ")
            password = input("Enter password: ")
            sms.create_student(username, password)
            print("Student account created successfully!")

        elif choice == "3":
            print("--- Login ---")
            username = input("Enter username: ")
            password = input("Enter password: ")

            logged_in_user = sms.find_user(username, password)

            if isinstance(logged_in_user, Teacher):
                print(f"Welcome, {logged_in_user.username}!")
                while True:
                    print("\n1. Create Course\n2. Logout")
                    choice = input("Choose an option: ")

                    if choice == "1":
                        course_name = input("Enter course name: ")
                        course = logged_in_user.create_course(course_name)
                        sms.courses.append(course)
                        print(f"Course '{course_name}' created successfully!")

                    elif choice == "2":
                        print("Logged out.")
                        break

                    else:
                        print("Invalid option.")

            elif isinstance(logged_in_user, Student):
                print(f"Welcome, {logged_in_user.username}!")
                while True:
                    print("\n1. Enroll in Course\n2. Logout")
                    choice = input("Choose an option: ")

                    if choice == "1":
                        print("Available Courses:")
                        for idx, course in enumerate(sms.courses):
                            print(f"{idx + 1}. {course.name} (Teacher: {course.teacher.username})")

                        course_choice = int(input("Enter course number: ")) - 1

                        if 0 <= course_choice < len(sms.courses):
                            selected_course = sms.courses[course_choice]
                            logged_in_user.enroll(selected_course)
                            print(f"Enrolled in '{selected_course.name}' successfully!")
                        else:
                            print("Invalid course selection.")

                    elif choice == "2":
                        print("Logged out.")
                        break

                    else:
                        print("Invalid option.")

            else:
                print("Invalid credentials.")

        elif choice == "4":
            print("Thank you for using our management system, Have a Good day!")
            break

        else:
            print("Invalid choice. Please try again.")

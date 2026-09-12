class Student:

    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    def __str__(self):
        return (f"Student ID: {self.student_id}\n"
                f"Student Name: {self.name}\n"
                f"Course: {self.course}\n"
                f"Year Level: {self.year_level}")

class DynamicArray:

    INITIAL_CAPACITY = 5

    def __init__(self):
        self.capacity = DynamicArray.INITIAL_CAPACITY
        self.count = 0
        self.items = self._make_raw_array(self.capacity)

    def _make_raw_array(self, capacity):
        return [None] * capacity

    def _resize(self, new_capacity):
        new_items = self._make_raw_array(new_capacity)
        for i in range(self.count):
            new_items[i] = self.items[i]
        self.items = new_items
        self.capacity = new_capacity
        print(f"[System] Array capacity increased to {self.capacity}.")

    def size(self):
        return self.count

    def is_full(self):
        return self.count == self.capacity

    def is_empty(self):
        return self.count == 0

    def add(self, student):
        if self.is_full():
            print("Array is full.")
            self._resize(self.capacity * 2)
        self.items[self.count] = student
        self.count += 1

    def get(self, index):
        if 0 <= index < self.count:
            return self.items[index]
        return None

    def set(self, index, student):
        if 0 <= index < self.count:
            self.items[index] = student
            return True
        return False

    def index_of(self, student_id):
        for i in range(self.count):
            if self.items[i].student_id == student_id:
                return i
        return -1

    def search(self, student_id):
        idx = self.index_of(student_id)
        if idx == -1:
            return None
        return self.items[idx]

    def remove(self, student_id):
        idx = self.index_of(student_id)
        if idx == -1:
            return False
        for i in range(idx, self.count - 1):
            self.items[i] = self.items[i + 1]
        self.items[self.count - 1] = None
        self.count -= 1
        return True

    def display(self):
        if self.is_empty():
            print("No student records found.")
            return
        print("-" * 50)
        for i in range(self.count):
            student = self.items[i]
            print(f"[{i + 1}] {student.student_id} | {student.name} | "
                  f"{student.course} | Year {student.year_level}")
        print("-" * 50)

    def display_info(self):
        print(f"Current number of students : {self.count}")
        print(f"Current array capacity     : {self.capacity}")

class StudentRecordManager:

    def __init__(self):
        self.records = DynamicArray()

    def run(self):
        while True:
            self._print_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.records.display()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.remove_student()
            elif choice == "6":
                self.records.display_info()
            elif choice == "7":
                print("Exiting Student Record Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 7.")

    def _print_menu(self):
        print("\n================================")
        print("     STUDENT RECORD MANAGER")
        print("================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")

    def _get_non_empty_input(self, prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty. Please try again.")

    def _get_year_level(self):
        while True:
            value = input("Year Level: ").strip()
            if value.isdigit() and 1 <= int(value) <= 6:
                return int(value)
            print("Invalid year level. Please enter a whole number (e.g., 1-6).")

    def add_student(self):
        print("\n-- Add Student --")
        student_id = self._get_non_empty_input("Student ID: ")

        if self.records.search(student_id) is not None:
            print(f"A student with ID '{student_id}' already exists.")
            return

        name = self._get_non_empty_input("Student Name: ")
        course = self._get_non_empty_input("Course: ")
        year_level = self._get_year_level()

        new_student = Student(student_id, name, course, year_level)
        self.records.add(new_student)
        print(f"Student '{name}' added successfully.")

    def search_student(self):
        print("\n-- Search Student --")
        student_id = self._get_non_empty_input("Enter Student ID to search: ")
        student = self.records.search(student_id)
        if student:
            print("\nStudent Found:")
            print(student)
        else:
            print(f"No student found with ID '{student_id}'.")

    def update_student(self):
        print("\n-- Update Student --")
        student_id = self._get_non_empty_input("Enter Student ID to update: ")
        student = self.records.search(student_id)
        if not student:
            print(f"No student found with ID '{student_id}'.")
            return

        print("Leave a field blank to keep its current value.")
        new_name = input(f"Student Name [{student.name}]: ").strip()
        new_course = input(f"Course [{student.course}]: ").strip()
        new_year = input(f"Year Level [{student.year_level}]: ").strip()

        if new_name:
            student.name = new_name
        if new_course:
            student.course = new_course
        if new_year:
            if new_year.isdigit() and 1 <= int(new_year) <= 6:
                student.year_level = int(new_year)
            else:
                print("Invalid year level entered; keeping the old value.")

        print("Student record updated successfully.")

    def remove_student(self):
        print("\n-- Remove Student --")
        student_id = self._get_non_empty_input("Enter Student ID to remove: ")
        if self.records.remove(student_id):
            print(f"Student with ID '{student_id}' removed successfully.")
        else:
            print(f"No student found with ID '{student_id}'.")

def main():
    manager = StudentRecordManager()
    manager.run()

if __name__ == "__main__":
    main()
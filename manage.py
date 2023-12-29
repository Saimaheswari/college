import streamlit as st

# Function to add a new course
def add_course(course_name, course_code):
    courses.append({"Name": course_name, "Code": course_code})

# Function to add a new student
def add_student(student_name, student_id, course):
    students.append({"Name": student_name, "ID": student_id, "Course": course})

# Function to display all courses
def display_courses():
    st.subheader("List of Courses:")
    for course in courses:
        st.write(f"{course['Name']} ({course['Code']})")

# Function to display all students
def display_students():
    st.subheader("List of Students:")
    for student in students:
        st.write(f"{student['Name']} (ID: {student['ID']}, Course: {student['Course']})")

# Main Streamlit app
st.title("College Management System")

# Initialize empty lists for courses and students
courses = []
students = []

# Sidebar for navigation
menu = ["Home", "Add Course", "Add Student", "Display Courses", "Display Students"]
choice = st.sidebar.selectbox("Menu", menu)

# Handle different menu choices
if choice == "Home":
    st.header("Welcome to the College Management System")

elif choice == "Add Course":
    st.header("Add a New Course")
    course_name = st.text_input("Course Name")
    course_code = st.text_input("Course Code")
    if st.button("Add Course"):
        add_course(course_name, course_code)
        st.success("Course added successfully!")

elif choice == "Add Student":
    st.header("Add a New Student")
    student_name = st.text_input("Student Name")
    student_id = st.text_input("Student ID")
    # Dropdown to select a course for the student
    selected_course = st.selectbox("Select Course", [course["Name"] for course in courses])
    if st.button("Add Student"):
        add_student(student_name, student_id, selected_course)
        st.success("Student added successfully!")

elif choice == "Display Courses":
    st.header("Courses")
    display_courses()

elif choice == "Display Students":
    st.header("Students")
    display_students()


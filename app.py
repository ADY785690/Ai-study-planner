import streamlit as st
from datetime import date

st.title("📚 AI Study Planner")

subjects = st.text_area(
    "Enter Subjects (comma separated)",
    "DSA, DBMS, OS, CN"
)

exam_date = st.date_input(
    "Exam Date",
    min_value=date.today()
)

hours = st.number_input(
    "Study Hours Per Day",
    min_value=1,
    max_value=24,
    value=4
)

if st.button("Generate Study Plan"):

    subject_list = subjects.split(",")

    st.subheader("Study Schedule")

    for subject in subject_list:
        st.write(
            f"✅ {subject.strip()} : {hours/len(subject_list):.1f} hrs/day"
        )

    st.success("Study Plan Generated Successfully!")

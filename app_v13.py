import streamlit as st
import pandas as pd
from rota_generator_v13 import load_staff_availability, load_tasks, generate_rota
from utils_v13 import display_rota, display_total_hours

st.title("🔁 Rota Generator – V13")

staff_file = st.file_uploader("Upload Staff Preferences CSV", type="csv")
task_file = st.file_uploader("Upload Task Details CSV", type="csv")

if staff_file and task_file:
    staff_df = pd.read_csv(staff_file)
    task_df = pd.read_csv(task_file)

    staff = load_staff_availability(staff_df)
    tasks = load_tasks(task_df)

    rota, total_hours = generate_rota(staff, tasks)

    display_rota(rota)
    display_total_hours(total_hours)

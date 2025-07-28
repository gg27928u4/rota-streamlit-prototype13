# Rota Generator – V13 Instructions

## Input CSVs:

### sample_staff_data_v13.csv
Columns:
- Name
- Available Days (comma-separated)
- Available Times (comma-separated 24h integers, e.g. 9,10,11)

### task_input_template_v13.csv
Columns:
- Task Name
- Day (e.g. Monday)
- Start Time (e.g. 9:00)
- Duration (in hours)
- People Required

## Main File
Set `app_v13.py` as your main file in Streamlit.

## Output
- Rota table (daily grid)
- Total assigned hours
- Download button for hours CSV

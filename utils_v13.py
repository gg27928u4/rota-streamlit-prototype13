import pandas as pd
import streamlit as st

def display_rota(rota):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    times = sorted(rota.keys(), key=lambda x: int(x.split(":")[0]))

    table = []
    for time in times:
        row = {"Time": time}
        for day in days:
            row[day] = ", ".join(rota[time][day])
        table.append(row)

    df = pd.DataFrame(table)
    st.markdown("### 📅 Generated Rota")
    st.dataframe(df)

def display_total_hours(total_hours):
    st.markdown("### ⏰ Total Hours Per Staff")
    st.dataframe(total_hours)

    csv = total_hours.to_csv(index=False).encode('utf-8')
    st.download_button("Download Rota CSV", csv, "rota_total_hours.csv", "text/csv")

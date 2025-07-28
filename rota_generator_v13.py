import pandas as pd

def load_staff_availability(df):
    staff = []
    for _, row in df.iterrows():
        available_days = [day.strip() for day in row["Available Days"].split(",")]
        available_times = [int(time.strip().replace(":00", "")) for time in row["Available Times"].split(",")]
        staff.append({
            "name": row["Name"],
            "available_days": available_days,
            "available_times": available_times,
            "assigned_hours": 0
        })
    return staff

def load_tasks(df):
    tasks = []
    for _, row in df.iterrows():
        task = {
            "name": row["Task Name"],
            "day": row["Day"],
            "start_time": int(str(row["Start Time"]).split(":")[0]),
            "duration": int(row["Duration (hours)"]),
            "people_required": int(row["People Required"])
        }
        tasks.append(task)
    return tasks

def generate_rota(staff, tasks):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    times = list(range(9, 17))

    rota = {f"{hour}:00": {day: [] for day in days} for hour in times}

    for task in tasks:
        assigned_people = []
        for member in sorted(staff, key=lambda x: x["assigned_hours"]):
            if (task["day"] in member["available_days"] and
                all(task["start_time"] + i in member["available_times"] for i in range(task["duration"])) and
                member["name"] not in assigned_people and
                len(assigned_people) < task["people_required"]):

                for i in range(task["duration"]):
                    hour = task["start_time"] + i
                    if hour in range(9, 17):
                        rota[f"{hour}:00"][task["day"]].append(member["name"])
                member["assigned_hours"] += task["duration"]
                assigned_people.append(member["name"])
                if len(assigned_people) == task["people_required"]:
                    break

    total_hours = pd.DataFrame([{"Name": m["name"], "Assigned Hours": m["assigned_hours"]} for m in staff])
    return rota, total_hours

def make_sms(task: dict):
    water = f" Planned volume: {task['water_liters']:,} L." if task.get("water_liters", 0) else ""
    return (
        f"Zöld Debrecen Task {task['task_id']}: {task['label']} in {task['area']} "
        f"at {task.get('scheduled_time', 'scheduled time')}.{water} "
        "Reply DONE [litres], SKIP or ISSUE."
    )

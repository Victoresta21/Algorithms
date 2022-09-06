def study_schedule(permanence_period, target_time):
    students_count = 0
    try:
        for student in permanence_period:
            start = student[0]
            finish = student[1]
            if start <= target_time <= finish:
                students_count += 1
        return students_count
    except TypeError:
        return None

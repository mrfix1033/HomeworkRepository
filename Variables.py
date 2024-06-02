number_of_completed_homeworks = 12
number_of_spent_hours = 1.5
course_name = "Python"
time_for_one_task = number_of_spent_hours / number_of_completed_homeworks
print(f"Курс: {course_name}",
      f"всего задач: {number_of_completed_homeworks}",
      f"затрачено часов: {number_of_spent_hours}",
      f"среднее время выполнения {time_for_one_task}ч.", sep=', ')

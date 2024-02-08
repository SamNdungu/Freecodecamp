def add_time(start_time, duration, target_day=None):

  new_time = ""

  # Conversion of Start 12-hour format to 24-hour format
  start_format = start_time.split(" ")
  start_time_components = start_format[0].split(":")
  start_am_pm = start_format[1]
  start_hour = int(start_time_components[0])
  start_minute = int(start_time_components[1])

  if start_am_pm == "PM":
    start_hour = start_hour + 12

  # Conversion of Start hours into minutes
  start_minute = start_minute + (60 * start_hour)

  # Conversion of duration hours into minutes
  duration_components = duration.split(":")
  duration_hour = int(duration_components[0])
  duration_minute = int(duration_components[1])
  duration_minute = duration_minute + (60 * duration_hour)

  # Total minutes
  total_minutes = start_minute + duration_minute

  # Minute calculation
  final_minutes = total_minutes % 60
  hours = int(total_minutes / 60)
  if len(str(final_minutes)) == 1:
    new_time = "0" + str(final_minutes)
  elif len(str(final_minutes)) == 2:
    new_time = str(final_minutes)

  # Days calculation
  hour = hours % 24
  days = int(hours / 24)

  # Hour and AM/PM calculation
  final_hours = hour % 12
  if int(hour / 12) == 0:
    final_am_pm = 'AM'
    if final_hours == 0:
      final_hours = 12
  else:
    final_am_pm = 'PM'
    if final_hours == 0:
      final_hours = 12
  new_time = str(final_hours) + ':' + new_time + ' ' + final_am_pm

  # Calculation of day of day of Week
  if target_day is not None:
    days_of_week = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday'
    ]
    pos = 0
    while True:
      if target_day.lower() == days_of_week[pos].lower():
        break
      pos = pos + 1
    new_day_of_week = days_of_week[((pos + (days % 7)) % 7)]
    new_time = new_time + ", " + new_day_of_week

  # Final output
  if days == 1:
    new_time = new_time + " (next day)"
  elif days > 1:
    days = str(days)
    new_time = new_time + " (" + days + " days later)"

  return new_time


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))

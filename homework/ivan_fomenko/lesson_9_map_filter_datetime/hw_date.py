import datetime

date_str = 'Jan 15, 2023 - 12:05:33'

# Распечатайте полное название месяца из этой даты

date_python = datetime.datetime.strptime(date_str, '%b %d, %Y - %H:%M:%S')
date_human_month = date_python.strftime('Month: %B')

print(date_human_month)


# Распечатайте дату в таком формате: "15.01.2023, 12:05"
date_human_format = date_python.strftime('%y.%m.%Y, %H:%M')
print(date_human_format)
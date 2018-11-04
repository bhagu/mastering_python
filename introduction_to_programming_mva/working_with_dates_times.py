'''
    This script has been created as part of the introduction to python training by microsoft virtual academy
    This section covers how to handle dates and times in python
'''

# the datetime library allows us to get the current date and time
import datetime

# print today's date
currentDate = datetime.date.today()
print(currentDate)

print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

print(currentDate.strftime('%d %b, %Y'))

birthDay = input('Enter your birthday (dd/mm/yyyy format): ')
birthDate = datetime.datetime.strptime(birthDay, '%d/%m/%Y').date()

print('\n' , birthDay)
print('\n', birthDate)

print(currentDate - birthDate)

# handling times
currentTime = datetime.datetime.now()

print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

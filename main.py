import calendar

f = open("test.txt", 'a')

name = input("What is your name?: ")
age = input("What is your age?: ")
gender = input("What is your gender?: ")
country = input("Which country do you live in?: ")
city = input("Which city do you live in?: ")
phoneNumber = input("What is your phonenumber?: ")
eMail = input("What is your E-Mail?: ")
Height = input("How tall are you in centimeters?: ")
Weight = input("How much do you weigh in kilograms?: ")
Smoke = input("Do you smoke? If yes, please specify how many cigarettes you approximately smoke per day: ")
Diabetes = input("Do you have any sort/type of diabetes?: ")
Hypertension = input("Do you have Hypertension?: ")
CardiacDiseases = input("Do you have any cardiac diseases?: ")
other = input("Do you have any other conditions?: ")
Operation = input("Which area of your body do you wished to have changed? please specify: ")
Platform = input("We can have our online consultation in WhatsApp, Instagram, Skype, Zoom, or Facebook Messenger. In which platform, do you wish to have the consultation?")
OnlineConsultation = input("What is your account information on this platform?: ")
print("The calendar for the year 2021 is: " + calendar.calendar(2021, 2, 1, 6))
Date = input("Please have a look at the calendar, and choose a date for the online consultation: ")



f.write(f"Name: {name}\n")
f.write(f"Age: {age}\n")
f.write(f"Gender: {gender}\n")
f.write(f"The patient reside in: {country}\n")
f.write(f"In the city of: {city}\n")
f.write(f"The patient's phonenumber is: {phoneNumber}\n")
f.write(f"The patient's email is: {eMail}\n")
f.write(f"The height of the patient is :{Height}\n")
f.write(f"The weight of the patient is: {Weight}\n")
f.write(f"Does the patient smoke, if yes, how much?: {Smoke}\n")
f.write(f"Does the patient has Diabetes?: {Diabetes}\n")
f.write(f"Does the Patient has Hypertension?: {Hypertension}\n")
f.write(f"Does the patient has any sort of cardiac diseases?: {CardiacDiseases}\n")
f.write(f"Does the patient has any other condition?: {other}\n")
f.write(f"Which operation or area of the body does the patient wish the get surgery on?: {Operation}\n")
f.write(f"The platform for the consultation is: {Platform}\n")
f.write(f"The patient's preferred platform for the online consultation is: and their account information: {OnlineConsultation}\n")
f.write(f"{Date}\n")

# if date is true
#   set date
# print("please specify your wished time, then i'll get back to you about the specific time")

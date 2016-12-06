import time

print("Milloin olet syntynyt?"))
birthday = input("esim. 01.01.2016 on 1. tammikuuta 2016")
if birthday.isalpha() == False and int(birthday) == 6:
    generate_hetu()
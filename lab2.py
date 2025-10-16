#1
# parol = input("Vvedi parol: ")
#Проверка длины пароля
# if len(parol) >= 8:
#     print("Parol prinyat")
# if len(parol) < 8:
#     print("Slishkom korotkiy parol")

#2
# status = input("online or offline? ")
# if status == "online":
#     print("Svyaz ustanovlena.")
# else:
#     print("Svyaz potyarena.")

#3
# num = int(input("Vvedi chislo 1-100: "))
# if num > 100 and num <1:
#     print("Oshibka vvoda.")
# if num >= 1 and num <= 30:
#     print("Nizkiy uroven uqrozi")
# elif num >= 31 and num <= 70:
#     print("Sredniy uroven uqrozi.")
# else:
#     print("Kriticheskiy uroven uqrozi.")

#4
# checksum_original = input("Vvedi fayl: ")
# checksum_current = input("Vvedi tekushiy fayl: ")
# status = "Fayl ne izmenen" if checksum_current==checksum_original else "Fayl povrejden"
# print(status)

#5
# event_code = input("Vvedi kod sobitiy: ")
# match event_code:
#     case "ERR":
#         print("Oshibka sistemi.")
#     case "WRN":
#         print("Preduprejdeniye.")
#     case _:
#         print("Neizvestniy kod.")
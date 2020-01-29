from picamera import PiCamera
import datetime as dt
import time

text = ""
text = text + dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ": " + "Experiment started" + "\n"
# http://www.gitlab.sciencein.cz/esero_public_projects
# camera settings
camera = PiCamera()
camera.resolution = (2592, 1944)
text = text + dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ": " + "Camera was set" + "\n"

# taking pictures
names = ['Marie Balíková', 'Tatiana Beszedéšová', 'Michael Bílek', 'Adéla Bradáčová', 'Petra Dobešová', 'Barbora Doušková', 'Matěj Genčur', 'Šimon Hanák', 'Viktorie Hanušová', 'Ondřej Hůrka', 'Martin Jiřík', 'Kristýna Ela Kadlečíková', 'Lukáš Kuba', 'Vojtěch Mareš', 'Sofie Martinák', 'Tereza Mičánková', 'Nela Ostrá', 'Roman Otych', 'Magdalena Pompová', 'Jakub Procházka', 'Ondřej Rada', 'Daniel Roman', 'Victoria Staňová', 'Martin Synek', 'Štěpán Šicner', 'Martina Šmerková', 'Tadeáš Tuček', 'Pavel Václavek', 'Zina Vránová', 'Adéla Vrbková', 'Agáta Wendrinska', 'Marta Vostalová', 'iří Pecl', 'Markéta Andrlová', 'Lucie Andrýsková', 'Zuzana Boháčková', 'Kristýna Bradáčová', 'Vít Černý', 'Martin Dvořák', 'Anna Galvasová', 'Petr Geršl', 'Filip Hanus', 'Jana Chalupská', 'Lukáš Joukl', 'Oliver Klimeš', 'Marek Laštovic', 'Filip Maxa', 'Tereza Nováková', 'Vít Míček', 'Anna Policerová', 'Veronika Pompová', 'Markéta Poledňová', 'Markéta Růžičková', 'Lukáš Řezanina', 'Anna Skřičková', 'Pavel Svoboda', 'Karolína Veselská', 'Lucie Vrabcová', 'Nicol Renerová', 'Michael Kureš', 'Michaela Kalousková', 'Tadeáš Němec', 'Ludmila Kučerová', 'Bedřich Prokeš', 'Matěj Šicner', 'Martin Doušek', 'Ondřej Hanák', 'Vojtěch Holík', 'Ester Hrnčířová', 'Lubomír Janda', 'Tomáš Ježek', 'Zuzana Juřenčáková', 'Jan Klapetek', 'Klára Kočí', 'Klára Komrsková', 'Lukáš Kos', 'Ladislav Kostelan', 'Tereza Koupá', 'Štepán Křetínký', 'Josefína Kvíčalová', 'Benjamin Levíček', 'Ella Mikulková', 'Eliška Mrázková', 'Edita Munzarová', 'Dominika Múčková', 'Lenka Petrášová', 'Barbora Pospíšilová', 'Šimon Martin Prudil', 'Tereza Pučová', 'Hana Rousová', 'Alžběta Slaná', 'Barbora Špalková', 'Daniela Šteflíčková', 'Pavel Šťastný', 'Filip Tatíček', 'Kateřina Zelinková', 'Veronika Svobodová', 'Miroslav Tesař', 'Jarmila Havlíčková']
for a in names:
    try:
        filename = (str(a) + ".jpg")
        camera.annotate_text=filename + dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S \n " + str(a))
        camera.capture(filename)
        text = text + dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ": " + "Image " + filename + " was token" + "\n"
    except Exception as e:
        print(e)
        text = text + dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ": " + str(e) + "\n"
    time.sleep(1)
print("\n")
print(text)
with open("log.txt", mode="w", encoding="utf-8") as file:
    print(text, file=file)
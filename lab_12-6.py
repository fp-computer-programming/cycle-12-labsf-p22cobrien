# Auhtor: CMOB 2/23/2022

from shutil import get_archive_formats


grades = {'End S1 Labs':100,'Start S2 Labs':100,'cycle 10 labs':0,'Mid-year Project Proposal':100,'cycle 10 practice quiz':100,'cycle 10 quiz':88}

print(grades.values())

for (k, v) in grades.items():
    print(k,v)


for (k,v) in grades.items():
    if v > 70:
        print(k,v)

for (k,v) in grades.items():
    if v < 50:
        print(k,v)
scores = [65, 85, 90, 78, 88, 92, 56]

scoremorethan70 = [x for x in scores if x > 79]

total = len(scoremorethan70)

print(f"Total number of students who scored more than 70: {total}")
scorelessorequal = [x for x in scores if x <= 70]

total = len(scoremorethan70)
totalless =len(scorelessorequal)

print(f"Total student who scored more than 70: {total}")
print(f"Total student who scored less than or equal to 70:{totalless}")
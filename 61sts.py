scores = [65, 85, 90, 78, 88, 92, 56]

scoremorethan70 = [x for x in scores if x > 79]

total = len(scoremorethan70)

print(f"Total number of students who scored more than 70: {total}")
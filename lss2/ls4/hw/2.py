subjects = ["математика", "физика", "химия", "литература", "история", "география"]

disliked_subjects = input("Введите предметы, которые вам не нравятся, через запятую: ").split(",")

for subject in disliked_subjects:
    subject = subject.strip().lower()
    if subject in subjects:
        subjects.remove(subject)

print("Обновленный список предметов:", subjects)

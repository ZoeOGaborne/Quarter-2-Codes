num_st = int(input("Enter number of students: "))
num_sub = int(input("Enter number of subjects: "))

t_class_avg = 0

for i in range(1, num_st + 1):
    print("\nStudent", i)
    t_score = 0

    for j in range(1, num_sub + 1):
        score = float(input(f"Enter score {j}: "))
        t_score += score

    st_avg = t_score / num_sub
    print(f"Average for student {i} = {st_avg:.1f}")

    t_class_avg += st_avg

class_avg = t_class_avg / num_st
print(f"\nClass average = {class_avg:.1f}")
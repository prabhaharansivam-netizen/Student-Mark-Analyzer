Empty_List = []
Marks = [99, 95, 91, 94, 92]
print(Marks)

print(len(Marks))

print("First Mark :", Marks[0])
print("Last Mark :", Marks[-1])

Reversed_Marks = Marks[::-1]
print(Reversed_Marks)

def match_marks(mark_List):
    count = 0
    matched_marks = []

    for mark in mark_List:
        mark_text = str(mark)
 
        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            matched_marks.append(mark)
 
    print("Marks with first and last digit same:", matched_marks)
    return count
 
same_digit_count = match_marks([88, 72, 99, 65, 77])
print("Number of matching marks:", same_digit_count)

total = 0
 
for mark in Marks:
    total += mark
 
average = total / len(Marks)
 
print("Sum of marks:", total)
print("Average marks:", average)

Marks.sort()
 
print("Smallest mark is:", Marks[0])
print("Largest mark is:", Marks[-1])
 

print("")
print("===== STUDENT MARKS LIST ANALYZER =====")
print("Sorted Marks:", Marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Lowest Mark:", Marks[0])
print("Highest Mark:", Marks[-1])
print("=======================================")

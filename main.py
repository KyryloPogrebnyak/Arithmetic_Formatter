from arithmetic_arranger import arithmetic_arranger

problems = eval(input("Enter the list of problems (no longer than 5 items): "))
display_answer = input("Do you want to display the results? (True/False): ")

if display_answer.lower() == "true":
    display_answer = True
else:
    display_answer = False

print(arithmetic_arranger(problems, display_answer))
import os
 
 
def get_letter_grade(student_type, score):
    # Return the letter grade, or raise ValueError for an unknown student type
    if student_type == "GRAD":
        if score >= 95:
            return "H"
        elif score >= 80:
            return "P"
        elif score >= 70:
            return "L"
        else:
            return "F"
    elif student_type == "UNDERGRAD":
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    else:
        raise ValueError("Unknown student category detected (" + student_type + ").")
 
 
def main():
    # Ask the user for the input file until it exists
    input_name = input("Please enter the name of the input data file: ")
    while not os.path.exists(input_name):
        print("File not found. Please try again.")
        input_name = input("Please enter the name of the input data file: ")
 
    # Ask the user for the output file
    output_name = input("Please enter the name of the output data file: ")
 
    # Ask about the curve until the answer is Y or N
    answer = input("Would you like to curve the grades? (Y/N) ").strip().upper()
    while answer != "Y" and answer != "N":
        answer = input("Would you like to curve the grades? (Y/N) ").strip().upper()
 
    # If Y, ask for the score that counts as 100 (number must be positive)
    curve_score = None
    if answer == "Y":
        while curve_score is None:
            try:
                value = float(input("Please enter the score that should map to a '100%' grade: "))
                if value > 0:
                    curve_score = value
                else:
                    print("The score must be greater than 0. Please try again.")
            except ValueError:
                print("That is not a valid number. Please try again.")
 
    # Read the given input file
    infile = open(input_name, "r")
    text = infile.read().strip()
    infile.close()
    lines = text.split("\n")
 
    # Grade each student (3 lines per student)
    results = []
    try:
        if len(lines) % 3 != 0:
            raise ValueError("Incomplete student record found.")
 
        for i in range(0, len(lines), 3):
            student_type = lines[i].strip()
            name = lines[i + 1].strip()
            grade_text = lines[i + 2].strip()
 
            try:
                score = float(grade_text)
            except ValueError:
                raise ValueError("Invalid grade detected (" + grade_text + ").")
            if score < 0 or score > 100:
                raise ValueError("Grade out of range detected (" + grade_text + ").")
 
            # Apply the curve if requested
            if curve_score is not None:
                score = score * 100 / curve_score
 
            results.append(name)
            results.append(get_letter_grade(student_type, score))
    except ValueError as error:
        print(error)
        print("Error occurred while determining letter grade. Aborting.")
        print("Please fix the problems in the input file and try again.")
        return
 
    # Write the output file (name on one line, letter on the next)
    outfile = open(output_name, "w")
    for item in results:
        outfile.write(item + "\n")
    outfile.close()
 
    print("All data was successfully processed and saved to the requested output file.")
 
 
main()

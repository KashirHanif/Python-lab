professors = {
    "P1": ["S1", "S2"],
    "P2": ["S2", "S3"],
    "P3": ["S3", "S4"],
    "P4": ["S1", "S4"]
}

subjects = ["S1", "S2", "S3", "S4"]

def is_valid(professor, subject, assignment):
    return subject not in assignment.values()

def backtrack(prof_list, assignment):
    if len(assignment) == len(prof_list):
        return assignment

    current_prof = prof_list[len(assignment)]

    for subject in professors[current_prof]:
        if is_valid(current_prof, subject, assignment):
            assignment[current_prof] = subject
            result = backtrack(prof_list, assignment)
            if result:
                return result
            del assignment[current_prof]  # backtrack

    return None

prof_list = list(professors.keys())
assignment = backtrack(prof_list, {})

if assignment:
    print("Valid Assignment Found:")
    for prof, subject in assignment.items():
        print(f"{prof} → {subject}")
else:
    print("No valid assignment found.")

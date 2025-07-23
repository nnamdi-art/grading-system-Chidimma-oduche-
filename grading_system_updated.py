
def get_grade(score):
    if 70 <= score <= 100:
        return 'A'
    elif 60 <= score < 70:
        return 'B'
    elif 50 <= score < 60:
        return 'C'
    elif 45 <= score < 50:
        return 'D'
    elif 40 <= score < 45:
        return 'E'
    elif 0 <= score < 40:
        return 'F'
    else:
        return 'Invalid score'

# Example usage
scores = [95, 67, 53, 47, 42, 20, 110, -3]

for score in scores:
    grade = get_grade(score)
    print(f"Score: {score} => Grade: {grade}")


def get_grade(score):
    if 70 <= score <= 100:
        return 'A'
    elif 60 <= score < 70:
        return 'B'
    elif 50 <= score < 60:
        return 'C'
    elif 40 <= score < 50:
        return 'D'
    elif 0 <= score < 40:
        return 'E'
    else:
        return 'Invalid score'

# Example usage
scores = [95, 67, 53, 45, 20, 110, -5]

for score in scores:
    grade = get_grade(score)
    print(f"Score: {score} => Grade: {grade}")

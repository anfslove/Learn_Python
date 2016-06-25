teachers = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],'Kenneth Love': ['Python Basics', 'Python Collections']}
print(teachers.keys())
def most_classes(teachers):
    max_count = 0
    r_teacher = {}
    for key in teachers:
        if len(teachers[key]) > max_count:
            max_count = len(teachers[key])
            r_teacher[key] = teachers[key]

    return r_teacher

most_classes(teachers)
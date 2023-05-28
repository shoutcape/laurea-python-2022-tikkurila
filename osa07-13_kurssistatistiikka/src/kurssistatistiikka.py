import urllib.request
import json
from math import floor

def hae_kaikki():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    courses = json.loads(data)
    active = []
    for course in courses:
        if course['enabled'] == True:
            tup = (course['fullName'], course['name'], course['year'], sum(course['exercises']))
            active.append(tup)
    return active

def hae_kurssi(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_request.read()
    course = json.loads(data)
    # json_formatted_str = json.dumps(course, indent=2)
    # print(json_formatted_str)
    course_info = {}
    weeks = 0
    students = 0
    hours = 0
    exercises = 0
    for week, data in course.items():
        weeks += 1
        if data['students'] > students:
            students = data['students']
        hours += data['hour_total']
        exercises += data['exercise_total']
    hours_average = floor(hours/students)
    exercises_average = floor(exercises/students)

    course_info['viikkoja'] = weeks
    course_info['opiskelijoita'] = students
    course_info['tunteja'] = hours
    course_info['tunteja_keskimaarin'] = hours_average
    course_info['tehtavia'] = exercises
    course_info['tehtavia_keskimaarin'] = exercises_average

    return course_info


if __name__ == "__main__":
    print(hae_kaikki())
    print(hae_kurssi("docker2019"))

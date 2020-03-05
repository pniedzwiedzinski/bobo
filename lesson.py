import json
import requests

from datetime import datetime


LESSON_PLAN_ENDPOINT = "https://kapskypl.github.io/planyn-backend/classes/3E.json"

LESSON_HOURS = (
    { "start": "7.10", "end": "7.55" },
    { "start": "8.00", "end": "8.45" },
    { "start": "8.50", "end": "9.35" },
    { "start": "9.50", "end": "10.35" },
    { "start": "10.40", "end": "11.25" },
    { "start": "11.30", "end": "12.15" },
    { "start": "12.30", "end": "13.15" },
    { "start": "13.20", "end":  "14.05" },
    { "start": "14.10", "end": "14.55" },
    { "start": "15.00", "end": "15.45" },
)

def get_today_lessons():
    lessons = requests.get(LESSON_PLAN_ENDPOINT).json()
    return lessons[datetime.today().weekday()]

def get_lessons_start():
    today_lessons = get_today_lessons()
    start_hour = min([index for index, school_subject in enumerate(today_lessons) if school_subject and len(school_subject) > 0])

    return start_hour 

def get_lessons_end():
    today_lessons = get_today_lessons()
    end_hour = max([index for index, school_subject in enumerate(today_lessons) if school_subject and len(school_subject) > 0])

    return end_hour
    

start_hour = get_lessons_start()
end_hour = get_lessons_end()

print ("Dzisiaj lekcje trwają od " + (LESSON_HOURS[start_hour]["start"]) + " do " + (LESSON_HOURS[end_hour]["end"]))
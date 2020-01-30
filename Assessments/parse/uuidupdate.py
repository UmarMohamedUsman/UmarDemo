#!/usr/bin/env python3

import cat_data
import assessment
import output
import json
import pprint
import re
import os
import uuid

from jinja2 import Environment
from jinja2 import FileSystemLoader

def convert_text(name):
    s1 = re.sub('[^0-9a-zA-Z]+', ' ', name).lower()
    s2 = re.sub('\s+', '_', s1)
    return str(re.sub('_$','', s2))

def getdate():
    import datetime
    return datetime.datetime.now().strftime('%Y-%m-%d')

with open("../aar/assessment.uuid.json", "r") as assessment_file:
    my_assessment = assessment.assessment_from_dict(json.load(assessment_file))

for category in my_assessment.category:
    category.id = str(uuid.uuid4())
    for question in category.questions:
        question.id = str(uuid.uuid4())
        for choice in question.choices:
            choice.id = str(uuid.uuid4())

with open("../aar/assessment.json", "w") as assessment_file:
    json.dump(assessment.assessment_to_dict(my_assessment), assessment_file, indent=True)
        
#with open("../aar/output_new.json", "w") as output_file:
#    json.dump(output.output_to_dict(my_output), output_file, indent=True)
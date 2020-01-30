#!/usr/bin/env python3

import cat_data
import assessment
import output
import json
import pprint
import re
import os

from jinja2 import Environment
from jinja2 import FileSystemLoader

def convert_text(name):
    s1 = re.sub('[^0-9a-zA-Z]+', ' ', name)
    s2 = re.sub('\s+', '-', s1)
    return str(re.sub('-$','', s2)).lower()

def getdate():
    import datetime
    return '10/16/2019'
   # return datetime.datetime.now().strftime('%m/%d/%Y')

with open("./aar/assessment.json", "r") as assessment_file:
    my_assessment = assessment.assessment_from_dict(json.load(assessment_file))

j2_env = Environment(loader=FileSystemLoader('./parse/templates'),                                                                                                                            
                     trim_blocks=True, lstrip_blocks=True)

article_template = j2_env.get_template('article.md.j2')
choice_template = j2_env.get_template('choice.md.j2')

for category in my_assessment.category:
    print(convert_text(category.name))
    for question in category.questions:
        if not question.heading:
            question.heading = question.title

        category_name = convert_text(category.name)
        question_name=convert_text(question.heading)

        guidance_directory = "./output/"+category_name
        include_directory = "./output/includes/aar_guidance/"
        if not os.path.exists(guidance_directory):
            os.makedirs(guidance_directory)

        if not os.path.exists(include_directory):
            os.makedirs(include_directory)

        article = article_template.render(question=question, getdate=getdate)
        
        f = open("./output/"+category_name+"/"+question_name+".md", "w")
        f.write(article)
        f.close()

        for choice in question.choices:
            file_name=choice.id+".md"
            guidance_file = choice_template.render(choice=choice, getdate=getdate)

            g = open(include_directory + file_name, "w")
            g.write(guidance_file)
            g.close()
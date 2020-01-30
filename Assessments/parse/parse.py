#!/usr/bin/env python3

import cat_data
import assessment
import output
import json
import pprint
import re

def convert_text(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub('\s+', '_', s1)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s2).lower()

with open("../cat_review.json", "r") as cat_file:
    cat_data = cat_data.cat_data_from_dict(json.load(cat_file))

with open("../aar/assessment.orig.json", "r") as assessment_file:
    my_assessment = assessment.assessment_from_dict(json.load(assessment_file))

#with open("../aar/output.json", "r") as output_file:
#    my_output = output.output_from_dict(json.load(output_file))

for p in cat_data.pillars:
    if p.questions:
        for q in p.questions:
            question_id = convert_text(q.question)
            question=assessment.Question(id=question_id, title=q.question)

            i = 0
            new_output = []
            new_choices = []
            for c in q.choices:
                choice_id = convert_text(p.pillar) + "_" + question_id + str(i)
                choice_title = c.choice
                seperator = ' '
                choice_answer_tooltip = seperator.join(c.risks)

                if c.recommendations:
                    out_content = seperator.join(c.recommendations)
                else:
                    out_content = ""

                choice = assessment.Choice(id=choice_id, title=choice_title, 
                    answer_tooltip=choice_answer_tooltip, output=out_content)
                new_choices.append(choice)
                i+=1
            #    print(question.title)
            #print(new_choices)
            #section.choices += new_choices
        
            for category in my_assessment.category:
                if p.pillar == category.name:
                    print(p.pillar)
                    if not any(d.id == question_id for d in category.questions):
                        #print("Appending", question_id,"to", p.pillar)
                        question.choices = new_choices
                        category.questions.append(question)
                        #print(category.questions)
                    else:
                        for question in category.questions:
                            if question_id == question.id:
                                #print("Adding", new_choices, "to", question.id, "in", p.pillar)
                                question.choices += new_choices

#pprint.pprint(assessment.assessment_to_dict(my_assessment))
with open("../aar/assessment.json", "w") as assessment_file:
    json.dump(assessment.assessment_to_dict(my_assessment), assessment_file, indent=True)
    
#with open("../aar/output_new.json", "w") as output_file:
#    json.dump(output.output_to_dict(my_output), output_file, indent=True)
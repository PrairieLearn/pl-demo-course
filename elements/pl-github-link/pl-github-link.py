import random
import chevron


def prepare(element_html, data):
    qid = data['options']['question_path'].split("questions",1)[1]
    path_name = "https://github.com/PrairieLearn/pl-demo-course/tree/master/questions" + qid
    data["params"]["path_name"] =  path_name
    return data

def render(element_html, data):
    html_params = {
        'path_name': data['params']['path_name'],
    }
    with open('pl-github-link.mustache', 'r') as f:
        return chevron.render(f, html_params).strip()

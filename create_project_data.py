# from sqlalchemy import *
import os
import requests
import json
import csv
import click
from jinja2 import Template

val_cap = 'captions/captions_val2017.json'
trn_cap = 'captions/captions_train2017.json'
task_template = 'templates/template.html'
tutorial_template = 'templates/tutorial.html'
ldesc_template = 'templates/long_description.md'
results_html_template = 'templates/results.html'
results_js_template = 'templates/results.js'

@click.command()
@click.option('--language', help='Language project to create', prompt='Language project')
def create_cocohub_project_metadata(language):
    project_info = {
        "name": f"{language} Language Project",
        "short_name": f"{language}",
        "description": f"We are translating MS-COCO captions to {langauge}",
        "question": f"What is the {language} translation of this sentence?"
    }
    with open(f'project.json', 'w') as project_file:
        json.dump(project_info, project_file)
    if os.path.isfile(f"project.json"):
        print(f"project file created: project.json")

    if not os.path.isfile(f"template.html"):
        tmp = Template(open(task_template, 'r').read())
        result = tmp.render(language=language)
        with open(f'template.html', 'w') as f:
            f.write(result)

    if not os.path.isfile(f"tutorial.html"):
        tmp = Template(open(tutorial_template, 'r').read())
        result = tmp.render(language=language)
        with open(f'tutorial.html', 'w') as f:
            f.write(result)

    if not os.path.isfile(f"long_description.md"):
        tmp = Template(open(tutorial_template, 'r').read())
        result = tmp.render(language=language)
        with open(f'long_description.md', 'w') as f:
            f.write(result)

    if not os.path.isfile(f"results.html"):
        tmp = Template(open(results_html_template, 'r').read())
        result = tmp.render(language=language)
        with open(f'results.html', 'w') as f:
            f.write(result)

    if not os.path.isfile(f"results.js"):
        tmp = Template(open(results_js_template, 'r').read())
        result = tmp.render(language=language)
        with open(f'results.js', 'w') as f:
            f.write(result)


    field_names = ['question', 'caption_id', 'image_id', 'id', 'caption']
    if not os.path.isfile(f"projects/{language}_tasks.csv"):
        with open(f'projects/{language}_tasks.csv', 'w') as task_file:
            csvwriter = csv.DictWriter(task_file, delimiter=',', fieldnames=field_names)
            csvwriter.writerow(dict((fn,fn) for fn in field_names))
            coco_captions = json.load(open(val_cap, 'r'))['annotations'] + json.load(open(trn_cap, 'r'))['annotations']
            for row in coco_captions:
                row.update({'question': project_info['question']})
                csvwriter.writerow(row)
        print(f"Success! {language} file created.")
    else:
        print(f'Project files for {language} exist.. moving on')

if __name__ == '__main__':
    create_cocohub_project_metadata()

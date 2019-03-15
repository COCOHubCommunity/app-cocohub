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

@click.command()
@click.option('--language', help='Language project to create', prompt='Language project')
def create_cocohub_project_metadata(language):
    project_info = {
        "name": "{} Language Project".format(language),
        "short_name": "{}".format(language),
        "description": "We are translating MS-COCO captions to {}".format(language),
        "question": "Translate this sentence to {}".format(language)
    }
    if not os.path.isfile(f"projects/{language}_project.json"):
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

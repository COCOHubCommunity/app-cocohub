. /opt/cocohub/venv/bin/activate
language="$1"
project="$language"_project.json
template="$language"_template.html
tutorial="$language"_tutorial.html
long_description="$language"_long_description.md
tasks="$language"_tasks.csv

python create_project_data.py --language $language && \
    pbs create_project && \
    pbs update_project && \
    pbs add_tasks --task-file projects/$tasks && \
    rm projects/$tasks

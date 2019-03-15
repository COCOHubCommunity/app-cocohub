. /opt/cocohub/venv/bin/activate
language="$1"
project="$language"_project.json
template="$language"_template.html
tutorial="$language"_tutorial.html
long_description="$language"_long_description.md
tasks="$language"_tasks.csv

python create_project_data.py --language $language && \
    pbs create_project --project projects/$project && \
    pbs update_project --project projects/$project --task-presenter projects/$template --tutorial projects/$tutorial --long-description projects/$long_description && \
    pbs add_tasks --project projects/$project --task-file projects/$tasks && \
    rm projects/$tasks

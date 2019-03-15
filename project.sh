. /opt/cocohub/venv/bin/activate
language="$1"
python create_project_data.py --language $language
pbs create_project --project projects/"$language"_project.json
pbs update_project --project projects/"$language"_project.json --task-presenter projects/"$language"_template.html --tutorial projects/"$language"_tutorial.html --long-description projects/"$language"_long_description.md
pbs add_tasks --project projects/"$language"_project.json --task-file projects/"$language"_tasks.csv
rm projects/"$language"_tasks.csv

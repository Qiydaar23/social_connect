rm finaldeploymentsc.zip
. .venv2/bin/activate
pip freeze > requirements.txt
python manage.py collectstatic --noinput
zip -r finaldeploymentsc.zip . -x "*git*" "*.venv2*"

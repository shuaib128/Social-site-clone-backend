echo " BUILD START"
python -m install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo " BUILD END"
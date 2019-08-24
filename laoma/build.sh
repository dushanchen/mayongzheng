cd /root/project/mayongzheng/laoma
git fetch 
git merge origin/master

cd laoma
python3 manage.py migrate --settings=project.settings_prod
python3 manage.py collectstatic --settings=project.settings_prod


supervisorctl restart project
service nginx restart

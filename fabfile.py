from __future__ import with_statement
from fabric.api import env, cd, prefix, run, sudo

env.use_ssh_config = True
env.hosts = ['ec2']

project_dir = '/www/outing-box-repo/'

def start_ob():
    sudo('service gunicorn start')
    sudo('service nginx start')

def stop_ob():
    sudo('service nginx stop')
    sudo('service gunicorn stop')

def restart_ob():
    sudo('service gunicorn restart')
    sudo('service nginx restart')

def sync_code():
    with cd(project_dir):
        run('git pull')

def sync_static():
    with cd(project_dir):
        with prefix('source .env'):
            run('python manage.py collectstatic --noinput')

def deploy():
    sync_code()
    sync_static()

    restart_ob()

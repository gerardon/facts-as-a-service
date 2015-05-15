# coding: utf-8
from unipath import Path

from fabric.api import env, task, put, sudo, cd, abort, require


@task
def app_setup():
    sudo('mkdir -m 755 -p {0}'.format(env.RELEASES))
    sudo('chown -R deploy:www-data {0}'.format(env.RELEASES.parent()))

    with cd('/etc/nginx/sites-enabled/'):
        sudo('ln -sf {current}/host/nginx.vhost {app_name}.vhost'.format(
            current=env.RELEASES.child('current'),
            app_name=env.app_name
        ))

    with cd('/etc/supervisor/conf.d'):
        sudo('ln -sf {current}/host/supervisord.conf {app_name}.conf'.format(
            current=env.RELEASES.child('current'),
            app_name=env.app_name
        ))


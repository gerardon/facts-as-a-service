# coding: utf-8
from fabric.api import env, task, run, sudo, cd, settings, prefix


@task
def live():
    env.user = 'ubuntu'

    release = remote_clone()
    prepare_virtualenv(release)
    requirements = env.RELEASES.child(release, 'requirements.txt')
    pip('install -r {requirements}'.format(requirements=requirements), release=release)

    with cd(env.RELEASES):
        run('rm -rf current')
        run('ln -s {release} current'.format(release=release))

    restart_services()


@task
def restart_services():
    env.user = 'ubuntu'

    sudo('service nginx restart')
    sudo('supervisorctl reload')


def remote_clone():
    release = run('date +%Y-%m-%d-%Hh%Mm%Ss')

    run('ssh-keyscan github.com >> ~/.ssh/known_hosts')
    run('git clone {git_uri} {release_dir}'.format(
        git_uri=env.GIT_URI,
        release_dir=env.RELEASES.child(release)
    ))

    return release


def prepare_virtualenv():
    sudo('pip install virtualenv')

    with settings(hide('warnings'), user='deploy', warn_only=True):
        with cd(env.RELEASES.child(release)):
            run('virtualenv --no-site-packages --unzip-setuptools .')


def pip(command, flags='', release='current'):
    assert command
    with settings(hide('warnings'), user='deploy', warn_only=True):
        with cd(env.RELEASES.child(release)):
            with prefix('source bin/activate'):
                run('pip {command} {flags}'.format(
                    command=command,
                    flags=flags,
                ))

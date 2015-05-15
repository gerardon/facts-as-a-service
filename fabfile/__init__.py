# coding: utf-8
from unipath import Path

from fabric.api import env, task


@task
def go():
    env.site = 'facts.posdojo.us'
    env.hosts = [env.site]
    env.environment = 'production'
    env.app_name = 'facts_as_a_service'
    env.RELEASES = Path('/opt').child(env.app_name, 'releases')
    env.GIT_URI = 'git@github.com:gerardon/facts-as-a-service.git'

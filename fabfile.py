from sitesetup.fab.config import init_file
from sitesetup.fab.tasks import *
from fabric.context_managers import cd
from fabric.decorators import task
from fabric.operations import sudo

init_file('fabfile.cfg')


"""The code below was originally copied from schademodule"""

@task
def production_taskserver():
    """Sets the deployment type to staging: taskserver. Run this task before any other tasks."""
    init_deployment_type('production')

    # Manually set buildout file, by default it takes <deployment_type>.cfg.
    #print dir(config)
    #config.init_config({'buildout-file': 'staging-taskserver.cfg'})
    # doesn't work, manually run: ln -s staging-taskserver.cfg buildout.cfg

    # Take the task_host
    env.hosts = [config('task_host')]
    print 'user %s' % env.user
    env.user = 'jack.ha'
    # if config('user'):
    #     print 'user %s' % config('user')
    #     env.user = 'jack.ha'  #config('user')

@task
def staging_taskserver():
    """Sets the deployment type to staging: taskserver. Run this task before any other tasks."""
    init_deployment_type('staging')

    # Manually set buildout file, by default it takes <deployment_type>.cfg.
    #print dir(config)
    #config.init_config({'buildout-file': 'staging-taskserver.cfg'})
    # doesn't work, manually run: ln -s staging-taskserver.cfg buildout.cfg

    # Take the task_host
    env.hosts = [config('task_host')]
    if config('user'):
        env.user = config('user')

@task
def update_task():
    with cd(config('basedir')):
        sudo("git checkout master", user='buildout')
        sudo("git pull", user='buildout')
        sudo("bin/develop up", user='buildout')
        sudo("bin/buildout", user='buildout')
        sudo("bin/django syncdb", user='buildout')
        sudo("bin/django migrate", user='buildout')
        # sudo("bin/supervisorctl stop gunicorn", user='buildout') # if it runs
        # sudo("bin/supervisorctl restart celeryd", user='buildout')  # Only for task server
        sudo("bin/supervisorctl restart task_200", user='buildout')  # Only for task server

from fabric.api import local, run, lcd, cd, env, task, settings


@task
def localhost():
    env.run_command = local
    env.cd_command = lcd


@task
def remote():
    env.hosts['monobotsoft.es']
    env.run_command = run
    env.cd_command = cd


def mkdir(dirname):
    with settings(warn_only=True):
        env.run('mkdir {dirname}'.format(dirname=dirname))


@task
def construye():
    dirname = 'midirectorio'
    env.run('mkdir {dirname}'.format(dirname=dirname))
    with lcd('~/{dirname}'.format(dirname=dirname)):
        for x in range(1, 26):
            mkdir(dirname='{}_{}'.format(dirname, x))


@task
def destruye():
    dirname = 'midirectorio'
    env.run('rm {dirname} -rf'.format(dirname=dirname))

from lib.console import config

def main(*args):
    try:
        if config.ENV_PATH_ALL:
            pass
        else:
            raise Exception("Cannot install module without known installation path")
    except:
        raise Exception("Cannot install module without known installation path")

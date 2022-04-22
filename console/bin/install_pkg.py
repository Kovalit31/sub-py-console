from lib.console import config

def main(*args):
    try:
        if config.PATH:
            pass
        else:
            raise Exception("Cannot install module without known installation path")
    except:
        raise Exception("Cannot install module without known installation path")

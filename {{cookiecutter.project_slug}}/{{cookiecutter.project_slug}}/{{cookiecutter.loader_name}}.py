#! /usr/bin/env python

import argparse
import sys
import logging
from logging import config
from ndexutil.config import NDExUtilConfig
import {{ cookiecutter.project_slug }}

logger = logging.getLogger(__name__)


def _parse_arguments(desc, args):
    """
    Parses command line arguments
    :param desc:
    :param args:
    :return:
    """
    help_fm = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(description=desc,
                                     formatter_class=help_fm)
    parser.add_argument('--profile', help='Profile in configuration '
                                          'file to use to load '
                                          'NDEx credentials which means'
                                          'configuration under [XXX] will be'
                                          'used '
                                          '(default {{ cookiecutter.project_slug }})',
                        default='{{ cookiecutter.project_slug }}')
    parser.add_argument('--logconf', default=None,
                        help='Path to python logging configuration file in this'
                             'format: https://docs.python.org/3/library/logging.config.html#logging-config-fileformat '
                             '(default None)')
    parser.add_argument('--conf', help='Configuration file to load '
                                       '(default ~/' + NDExUtilConfig.CONFIG_FILE)
    parser.add_argument('--version', action='version',
                        version=('%(prog)s ' + {{ cookiecutter.project_slug }}.__version__))

    return parser.parse_args(args)


class NDExContentLoader(object):
    """
    Class to load content
    """
    def __init__(self, args):
        """

        :param args:
        """
        pass

    def _parse_config(self, profile, conf_file):
            """
            Parses config
            :return:
            """
            ncon = NDExUtilConfig(conf_file)
            con = ncon.get_config()
            self._user = con.get(profile, NDExUtilConfig.USER)
            self._pass = con.get(profile, NDExUtilConfig.PASSWORD)
            self._server = con.get(profile, NDExUtilConfig.SERVER)


    def run(self):
        """
        Runs content loading for {{ cookiecutter.project_name }}
        :param theargs:
        :return:
        """
        return 0

def main(args):
    """
    Main entry point for program
    :param args:
    :return:
    """
    desc = """
    Version {version}

    Loads {{ cookiecutter.project_name }} data into NDEx (http://ndexbio.org).
    
    
    """.format(version={{ cookiecutter.project_slug }}.__version__)
    theargs = _parse_arguments(desc, args[1:])
    theargs.program = args[0]
    theargs.version = {{ cookiecutter.project_slug }}.__version__

    try:
        if theargs.logconf is not None:
            logging.config.fileConfig(theargs.logconf)
        return run(theargs)
    except Exception as e:
        logger.exception('Caught exception')
    finally:
        logging.shutdown()
    return 0


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv))

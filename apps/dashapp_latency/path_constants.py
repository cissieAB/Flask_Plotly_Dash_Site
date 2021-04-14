from os.path import abspath, dirname, join

BASE_DIR = abspath(dirname(__file__))
PARENT_DIR = abspath(dirname(BASE_DIR))   # get the location of the parent folder
PATH_PREFIX = join(PARENT_DIR, "data/latency")

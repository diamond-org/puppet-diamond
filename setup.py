import os
import re
from setuptools import setup
from distutils.dir_util import copy_tree


# from https://github.com/flask-admin/flask-admin/blob/master/setup.py
def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('__meta__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    version=grep('__version__'),
    name='puppet_diamond',
    description="puppet_diamond",
    scripts=[
        "bin/get_puppet_certs.py",
        "bin/generate_sshd_keys.sh",
        "bin/get_submodules.sh",
        "bin/add_submodule.sh",
        "bin/domo-test.sh",
        "bin/domo-apply.sh",
        "bin/domo-sync.sh",
        "bin/domo-new.sh",
    ],
    # packages=["domo"],
    long_description="""puppet_diamond""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author=grep('__author__'),
    author_email=grep('__email__'),
    url=grep('__url__'),
    install_requires=read('requirements.txt'),
    license='MIT',
    zip_safe=False,
)

copy_tree("skels", os.path.join(os.environ["VIRTUAL_ENV"], "share/skels"))
copy_tree("puppet", os.path.join(os.environ["VIRTUAL_ENV"], "share/puppet"))

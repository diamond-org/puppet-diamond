from setuptools import setup
from distutils.dir_util import copy_tree

import os

version = '0.1'

setup(version=version,
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
    author='Ian Dennis Miller',
    author_email='iandennismiller@gmail.com',
    url='http://www.iandennismiller.com',
    install_requires=[
        "mr.bob==0.1a9",
        "distribute==0.7.3",
        "Fabric==1.10.2",
        "Sphinx==1.3.3",
        "GitPython==1.0.1",
        "alabaster==0.7.6",
    ],
    license='Proprietary',
    zip_safe=False,
)

copy_tree("skels", os.path.join(os.environ["VIRTUAL_ENV"], "share/skels"))
copy_tree("puppet", os.path.join(os.environ["VIRTUAL_ENV"], "share/puppet"))

Quick Start
===========

Installation
------------

There are three steps to installing Puppet-Diamond:

1. Install the Puppet-Diamond software
2. Create a global Puppet-Diamond configuration
3. Initialize a directory that stores the Puppet Master configuration

::

    mkvirtualenv puppet-diamond
    pip install Puppet-Diamond
    domo-new.sh puppet-diamond
    domo-new.sh puppetmaster


Basic Usage
-----------

1. sync the local config to the puppet master
2. test the config
3. apply the config

::

    domo-sync.sh
    domo-test.sh host1.example.com
    domo-apply.sh host1.example.com

Creating new assets
-------------------

Follow the setup procedure described in the relevant projecs:

1. :doc:`../guide/profile`
2. :doc:`../guide/provisioning`
3. :doc:`../guide/puppet-module`
4. :doc:`../guide/diamond-module`

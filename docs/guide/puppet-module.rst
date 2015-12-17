Creating a Puppet Module
========================

A Puppet Module is used to control a server resource, like a daemon, an OS package, or hardware.

Puppet-Diamond environment
--------------------------

Enter the Puppet-Diamond virtual environment and import your configuration settings.

::

    workon puppet-diamond
    source ~/.puppet-diamond

Scaffold initial files
----------------------

The first step is to scaffold a new module. The general form of the command is:

::

    domo-new.sh diamond-module ${SERVICE_NAME}

The following example demonstrates creating a puppet module for Postfix.

::

    domo-new.sh diamond-module postfix

Add to a host
-------------

Add the new module class to a profile, located in ``${PD_PATH}/${PD_MASTER}/profiles``.

::

    class {"postfix": ;}

Sync and Apply
--------------

Sync to the puppetmaster and apply the changes to the client.

::

    domo-sync.sh
    domo-test.sh ${PUPPET_HOST}.example.com
    domo-apply.sh ${PUPPET_HOST}.example.com

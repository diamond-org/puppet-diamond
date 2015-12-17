Creating a Flask-Diamond Module
===============================

A Flask-Diamond Module will enable a Flask-Diamond application to be installed using Puppet-Diamond onto a host in your enterprise.

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

    domo-new.sh diamond-module ${APPLICATION_NAME}

The following example demonstrates creating a diamond module for an application called *my-diamond-app*.

::

    domo-new.sh diamond-module my-diamond-app

SSH deploy keys
---------------

Create application SSH deploy keys.

::

    cd ${PD_PATH}/${PD_MASTER}/diamond/${APPLICATION_NAME}
    ssh-keygen -t rsa -f files/ssh/id_rsa
    open ${PD_GIT_WEB_URL}/${PD_GIT_GROUP}/${APPLICATION_NAME}/deploy_keys/new
    pbcopy < files/ssh/id_rsa.pub

Add to a host
-------------

Add the new module class to a profile, located in ``${PD_PATH}/${PD_MASTER}/profiles``.

::

    class {"my-diamond-app": ;}

Sync and Apply
--------------

Sync to the puppetmaster and apply the changes to the client.

::

    domo-sync.sh
    domo-test.sh ${PUPPET_HOST}.example.com
    domo-apply.sh ${PUPPET_HOST}.example.com

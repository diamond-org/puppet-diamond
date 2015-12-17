Provisioning a Host
===================

When you need more computing resources, you must allocate them in a process called *provisioning*.  This is the process of creating new hosts.

Overview
--------

A new host is provisioned in two stages:

1. The virtual host is created using Vagrant
2. The newly created host is configured using Puppet

Cloud Providers
---------------

The virtual host may be created using any provider that Vagrant is capable of interfacing with.  Digital Ocean is provided as part of Puppet-Diamond.  However, Linux KVM, Xen, and Amazon EC2 have been shown to work with Puppet-Diamond too.

Digital Ocean
~~~~~~~~~~~~~

Scaffold a new configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

	export HOSTNAME=host1
	domo-new.sh digitalocean-host $HOSTNAME
	domo-sync.sh

Create the host
^^^^^^^^^^^^^^^

::

	cd $PD_PATH/$PD_MASTER/hosts/$HOSTNAME
    get_puppet_certs.py $HOSTNAME
    generate_sshd_keys.sh
	vagrant up --provider=digital_ocean

DNS
^^^

Create an A record with this IP in the DNS control on Digital Ocean.
Go to `domains list <https://cloud.digitalocean.com/networking#actions-ptr>`_ and click to view all PTR records.
Click **add record** and then `add A record <https://cloud.digitalocean.com/domains/111232#add_a_record>`_.
Finally, paste the IP address and hostname.

Linux KVM
~~~~~~~~~

It is also possible to run your own virtual cloud with any moderately equipped Linux machine.  Puppet-Diamond supports this, but the documentation is forthcoming.

First-run tasks
---------------

There are a few tasks that should be run each time a new host is provisioned.

set password for domo user
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

	vagrant ssh
	passwd domo

update packages
~~~~~~~~~~~~~~~

::

	vagrant ssh
	apt-get update
	apt-get upgrade -y
	reboot

run puppet one last time
~~~~~~~~~~~~~~~~~~~~~~~~

::

	domo-apply.sh $HOSTNAME

Debugging
---------

It may be necessary to debug the puppet master.  In that case, try some of the following:

Try re-provisioning with puppet.

::

	vagrant provision

See that the cert is really listed on the puppet master.

::

	ssh $PD_PUPPETMASTER_SSH_HOST
	puppet cert list --all

Restart the puppet master server.

::

	ssh $PD_PUPPETMASTER_SSH_HOST
	service puppetmaster restart

View the logs

::

	ssh $PD_PUPPETMASTER_SSH_HOST
	tail -f /var/log/syslog

Log on to the new node and poke around

::

	vagrant ssh

Next Steps
----------

Now that you have provisioned a host, you can create new modules to configure it for specific purposes.  There are two main types of modules supported by Puppet-Diamond:

- :doc:`puppet-module`
- :doc:`diamond-module`

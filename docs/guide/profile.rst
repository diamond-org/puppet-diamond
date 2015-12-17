Creating a Profile
==================

A "profile" is a type of host with the configuration you specify.

There might be many hosts that implement the same profile.  For example, you may have multiple application servers behind a load balancer.  To implement such a setup, you would need two profiles: an application server profile and a load balancer profile.

A profile may be used to provision new hosts on any cloud:

- a commercial host like Digital Ocean
- locally using a KVM setup

Scaffold a Profile
------------------

The general form for creating a new profile looks like this

::

    domo-new.sh profile $PROFILE_TYPE

So to create a new profile called *application-server* that will be tailored for running applications:

::

    domo-new.sh profile application-server

Next Steps
----------

Once you have a profile, you need to create at least one host that uses the profile.  See the following for more information about that.

:doc:`provisioning`

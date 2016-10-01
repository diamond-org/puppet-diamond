# -*- coding: utf-8 -*-
# Puppet-Diamond (c) Ian Dennis Miller

import pkg_resources


class PuppetDiamond:
    def __init__(self):
        pass

    def init():
        """
        create a fresh puppet master configuration
        """
        pd = PuppetDiamond()
        pd.init_folders()

    def list_skels():
        """
        list available skels.
        """
        print("Available skels:\n")
        for skel in pkg_resources.resource_listdir('puppet_diamond', 'skels'):
            print("- {0}".format(skel))
        print("")

    def dryrun():
        """
        perform dry run on host (make no changes)
        """
        pd = PuppetDiamond()

        # source $HOME/.puppet-diamond
        # SSH_HOST=$1
        # ssh ${PD_PUPPETMASTER_SSH_USER}@${SSH_HOST} "sudo puppet agent --test --noop"


    def apply():
        """
        apply configuration to host
        """
        pd = PuppetDiamond()
        pd.apply()

    def certs():
        """
        create puppet certs on PuppetMaster and retrieve them
        """
        pd = PuppetDiamond()
        pd.certs()

    def scaffold(ctx):
        """
        create an empty file
        """
        title = raw_input("Title: ")
        author = raw_input("Author(s): ")
        year = raw_input("Year: ")

        pd = PuppetDiamond()
        pd.create_from_template(title, author, year)

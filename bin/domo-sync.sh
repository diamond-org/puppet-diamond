#!/bin/bash
# Puppet-Diamond
# http://diamond-methods.org/puppet-diamond.html

source $HOME/.puppet-diamond

SRC_PATH_MANIFESTS="${PD_PATH}/${PD_MASTER}/profiles"
SRC_PATH_MANIFESTS_DIAMOND="${VIRTUAL_ENV}/share/puppet"

SRC_PATH_MODULES="${PD_PATH}/${PD_MASTER}/modules"
SRC_PATH_DIAMOND_MODULES="${SRC_PATH_MODULES}/diamond"
SRC_PATH_PUPPET_MODULES="${SRC_PATH_MODULES}/puppet"
SRC_PATH_CORE_MODULES="${SRC_PATH_MODULES}/core"

echo
echo "1. sync hosts: ${SRC_PATH_MANIFESTS} -> ${PD_PUPPETMASTER_MANIFEST_PATH}/nodes"
rsync -av --exclude '.git*' --delete ${SRC_PATH_MANIFESTS}/ ${PD_PUPPETMASTER_SSH_USER}@${PD_PUPPETMASTER_SSH_HOST}:${PD_PUPPETMASTER_MANIFEST_PATH}/nodes

echo
echo "2. sync puppet-diamond: ${SRC_PATH_MANIFESTS_DIAMOND} -> ${PD_PUPPETMASTER_MANIFEST_PATH}"
rsync -av --exclude '.git*' ${SRC_PATH_MANIFESTS_DIAMOND}/* ${PD_PUPPETMASTER_SSH_USER}@${PD_PUPPETMASTER_SSH_HOST}:${PD_PUPPETMASTER_MANIFEST_PATH}

echo
echo "3. sync core modules: ${SRC_PATH_CORE_MODULES} -> ${PD_PUPPETMASTER_MODULE_PATH}"
rsync -av --exclude '.git*' ${SRC_PATH_CORE_MODULES}/ ${PD_PUPPETMASTER_SSH_USER}@${PD_PUPPETMASTER_SSH_HOST}:${PD_PUPPETMASTER_MODULE_PATH}

echo
echo "4. sync diamond modules: ${SRC_PATH_DIAMOND_MODULES} -> ${PD_PUPPETMASTER_MODULE_PATH}"
rsync -av --exclude '.git*' ${SRC_PATH_DIAMOND_MODULES}/ ${PD_PUPPETMASTER_SSH_USER}@${PD_PUPPETMASTER_SSH_HOST}:${PD_PUPPETMASTER_MODULE_PATH}

echo
echo "5. sync puppet modules: ${SRC_PATH_PUPPET_MODULES} -> ${PD_PUPPETMASTER_MODULE_PATH}"
rsync -av --exclude '.git*' ${SRC_PATH_PUPPET_MODULES}/ ${PD_PUPPETMASTER_SSH_USER}@${PD_PUPPETMASTER_SSH_HOST}:${PD_PUPPETMASTER_MODULE_PATH}

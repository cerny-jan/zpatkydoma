#!/bin/sh

# this is base on https://github.com/pyvec/python.cz/blob/master/deployment/deploy.sh

# This script should be executed on the CI machine.
if [ -z "$CI" ]; then
    exit
fi


# Decrypting private key
openssl aes-256-cbc -K $encrypted_17b712f42c00_key -iv $encrypted_17b712f42c00_iv -in deployment/id_rsa_zpatkydoma_deployment.enc -out deployment/id_rsa_zpatkydoma_deployment -d
chmod 600 deployment/id_rsa_zpatkydoma_deployment

# Run the 'update.sh' script remotely.
ssh 'app@node-14.rosti.cz' -p '14232' -o 'StrictHostKeyChecking no' -i 'deployment/id_rsa_zpatkydoma_deployment' '/srv/app/deployment/update.sh'


# Remove decrypted private key
rm deployment/id_rsa_zpatkydoma_deployment

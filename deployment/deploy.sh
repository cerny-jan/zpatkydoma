#!/bin/sh

# this is base on https://github.com/pyvec/python.cz/blob/master/deployment/deploy.sh

# This script should be executed on the CI machine.
if [ -z "$CI" ]; then
    exit
fi


# Decrypting private key
openssl aes-256-cbc -K $encrypted_f2ef1a2b0bb8_key -iv $encrypted_f2ef1a2b0bb8_iv -in deployment/zpatkydoma_deployment.enc -out deployment/zpatkydoma_deployment -d

# Run the 'update.sh' script remotely.
ssh 'app@node-14.rosti.cz' -p '14232' -o 'StrictHostKeyChecking no' -i 'deployment/zpatkydoma_deployment' '/srv/app/deployment/update.sh'


# Remove decrypted private key
rm deployment/id_rsa_pyvec_deployment

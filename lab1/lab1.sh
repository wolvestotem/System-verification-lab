#!/usr/bin/env bash
 
# Write your commands here
rm -rf bash-playground 
mkdir bash-playground
cp *.cpp bash-playground
cd bash-playground
mkdir backup
ls | grep "lab" | xargs cp -t backup
make --version | grep "^GNU" | xargs -I '{}' echo '{}' >> VERSIONS
gcc --version | grep "^gcc" | xargs -I '{}' echo '{}' >> VERSIONS

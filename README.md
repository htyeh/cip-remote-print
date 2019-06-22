# Print directly from your PC with CIP printers

## How it works

Your files are transfered to the CIP server, an ssh session is performed where one of the shell script located on the server is called. Subsequently the printed files are (optionally) removed.

## What you need

 1. Paramiko module
 2. An ssh keypair on your PC (guide for generating an ssh keypair: https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key)

## Setup before usage

 1. Get Paramiko (pip3 install paramiko)
 2. Copy your public key to the CIP server (under ~/.ssh/ type ssh-copy-id *username*@remote.cip.ifi.lmu.de)
 3. Fill in your CIP username in the first line of **print.py**
 4. Move the directory **Print_Works** to your CIP server (exp. mv Print_Works *username*@remote.cip.ifi.lmu.de:~/), the default location is **HOME**, otherwise manually change the paths in **print.py**

## Printing

 1. Draw your files to print into this directory, **make sure there is no space in any file names**
 2. Run **print.py**
 3. Answering **Print successful?(Y/N)** with **Y** will delete printed files in this directory
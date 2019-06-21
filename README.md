# Print directly from your PC with CIP printers

# How it works

## Your files are transfered to the CIP computer, an *ssh session* is performed where one of the *shell script* located on the CIP computer is called. Subsequently the printed files are (optionally) removed.

# What you need

## 1. Paramiko module
## 2. An ssh keypair on your PC (guide for generating an ssh keypair: https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key)

# Instructions

## 1. Get Paramiko (pip3 install paramiko)
## 2. Copy your public key to the CIP server (under ~/.ssh/ type ssh-copy-id *username*@remote.cip.ifi.lmu.de)
## 3. Fill in your CIP username in the first line of *print.py*
## 4. Move the directory *Print_Works* to your CIP computer (exp. mv Print_Works *username*@remote.cip.ifi.lmu.de:~/), the default location HOME, otherwise change the paths in *print.py*
## 5. Draw your files to print into this directory, *make sure there is no space in any file names*
## 6. Run *print.py*
## 7. Answering *Print successful?(Y/N)* with *Y* will delete printed files in this directory
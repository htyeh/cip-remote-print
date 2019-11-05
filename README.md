# Print directly from your PC with CIP printers

## How it works

1. PDFs in this directory are transfered to the CIS server
2. An ssh session is performed and the PDFs are sent to one of the printers
3. If the print succeeds, you can optionally remove the files from this directory

## What you need

 1. Python Paramiko module (to perform ssh and execute commands)
 2. An ssh keypair on your PC (to ensure passwordless remote connection, guide for generating an ssh keypair: https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key)

## Setup before usage

 1. Get Paramiko (pip3 install paramiko)
 2. Copy your public key to the CIP server (under ~/.ssh/ type ssh-copy-id *username*@remote.cip.ifi.lmu.de)
 3. Fill in your CIP username in the first line of **print.py**
 4. Move the directory **Print_Works** to your CIP server (exp. mv Print_Works *username*@remote.cip.ifi.lmu.de:~/), the default location is **HOME**, otherwise manually change the paths in **print.py**

## Printing

 1. Move some PDFs to this directory, **make sure there are no spaces in file names**
 2. Run **print.py**
 3. Answering **Print successful?(Y/N)** with **Y** or **y** will delete all PDFs in **Print_Works** on the server and in this directory
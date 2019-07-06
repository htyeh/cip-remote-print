myusername=""   # fill in your CIP login name

import os, getpass, paramiko

def cip_pr(printer_name):
    cd_pr_cmd = "cd Print_Works; lpr -P " + printer_name + " *.pdf"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username=myusername)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cd_pr_cmd)
    ssh.close()

def rm_prted_files(rm_local):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username=myusername)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Print_Works; rm *.pdf")
    ssh.close()
    if rm_local:
        os.system("rm *.pdf")


cpcmd = "scp *.pdf " + myusername + "@remote.cip.ifi.lmu.de:~/Print_Works"
os.system(cpcmd)

invalid_printer = True
while invalid_printer:
    print("\t1. Gobi")
    print("\t2. Kalahari")
    print("\t3. Sibirien")
    print("\t4. Antarktis")
    printer = input("Drucker wählen: ")
    if printer == "1":
        cip_pr("gobi")
        invalid_printer = False
    elif printer == "2":
        cip_pr("kalahari")
        invalid_printer = False
    elif printer == "3":
        cip_pr("sibirien")
        invalid_printer = False
    elif printer == "4":
        cip_pr("antarktis")
        invalid_printer = False
    else:
        continue

print_success = input("Print successful?(Y/N) --")
if print_success.lower() == "y":
    rm_prted_files(True)
else:
    rm_prted_files(False)

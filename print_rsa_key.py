
### fill in the username ###
### in each func+line 46 ###


import os, getpass, paramiko

def gobi_pr():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username="")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Desktop/Druckaufträge; ./gobi_pr_all.sh")
    ssh.close()

def klhr_pr():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username="")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Desktop/Druckaufträge; ./klhr_pr_all.sh")
    ssh.close()

def sbrn_pr():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username="")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Desktop/Druckaufträge; ./sbrn_pr_all.sh")
    ssh.close()

def atkt_pr():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username="")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Desktop/Druckaufträge; ./atkt_pr_all.sh")
    ssh.close()

def rm_prted_files(rm_local):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username="")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Desktop/Druckaufträge; rm *.pdf")
    ssh.close()
    if rm_local:
        os.system("rm *.pdf") # manually enable

### fill in the username ###
os.system("scp *.pdf @remote.cip.ifi.lmu.de:~/Desktop/Druckaufträge")

invalid_printer = True
while invalid_printer:
    print("\t1. Gobi")
    print("\t2. Kalahari")
    print("\t3. Sibirien")
    print("\t4. Antarktis")
    printer = input("Drucker wählen: ")
    if printer == "1":
        gobi_pr()
        invalid_printer = False
    elif printer == "2":
        klhr_pr()
        invalid_printer = False
    elif printer == "3":
        sbrn_pr()
        invalid_printer = False
    elif printer == "4":
        atkt_pr()
        invalid_printer = False
    else:
        continue

print_success = input("Print successful?(Y/N) --")
if print_success.lower() == "y":
    rm_prted_files(True)
else:
    rm_prted_files(False)

# 1 cp files to cip
# 2 paramiko login
# 3 execute shell script
# 4 rm local prtd files if success

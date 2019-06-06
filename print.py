import os, sys, getpass
try:
    import paramiko
except ModuleNotFoundError:
    print("Paramiko is needed to build an SSH connection and execute print command.")
    download_paramiko = input("Paramiko module not found, download now? --")
    if download_paramiko.lower() == "y":
        os.system("pip3 install paramiko")
        import paramiko
    else:
        print("Exiting...")
        sys.exit()


with open("usrname.txt", "r+") as usrname_file:
    entered_usrname = usrname_file.read()
    if entered_usrname == "":
        def create_print_dir():
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("remote.cip.ifi.lmu.de", username=entered_usrname, password=pw)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Desktop; mkdir Print_Works")
            ssh.close()
        entered_usrname = input("It seems you are using the program for the first time. Enter your CIP username: ")
        usrname_file.write(entered_usrname)
        create_print_dir()
        print("Print_Works directory created on the CIP computer")


def gobi_pr():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username=entered_usrname, password=pw)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Desktop/Print_Works; ./gobi_pr_all.sh")
    ssh.close()

def klhr_pr():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username=entered_usrname, password=pw)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Desktop/Print_Works; ./klhr_pr_all.sh")
    ssh.close()

def sbrn_pr():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username=entered_usrname, password=pw)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Desktop/Print_Works; ./sbrn_pr_all.sh")
    ssh.close()

def atkt_pr():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username=entered_usrname, password=pw)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Desktop/Print_Works; ./atkt_pr_all.sh")
    ssh.close()

def rm_prted_files(rm_local):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("remote.cip.ifi.lmu.de", username=entered_usrname, password=pw)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cd Desktop/Print_Works; rm *.pdf")
    ssh.close()
    if rm_local:
        os.system("rm *.pdf") # manually enable

pw = getpass.getpass("Password: ")
# copy files to Print_Works folder
scp_command = "scp *.pdf " + entered_usrname + "@remote.cip.ifi.lmu.de:~/Desktop/Print_Works"
os.system(scp_command)

invalid_printer = True
while invalid_printer:
    print("\t1. Gobi")
    print("\t2. Kalahari")
    print("\t3. Sibirien")
    print("\t4. Antarktis")
    print("\t0. Change username")
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
    elif printer == "0":
        new_usrname = input("Enter a new username: ")
        with open("usrname.txt", "w") as usrname_file:
            usrname_file.write(new_usrname)
    else:
        continue

print_success = input("Print successful?(Y/N) --")
if print_success.lower() == "y":
    rm_prted_files(True)
else:
    rm_prted_files(False)

# 1 check paramiko
# 2 check username

# 1 cp files to cip
# 2 paramiko login
# 3 execute shell script
# 4 rm local prtd files if success

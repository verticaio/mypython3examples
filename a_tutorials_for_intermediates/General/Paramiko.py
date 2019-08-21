from paramiko import SSHClient
client = SSHClient()
client.load_system_host_keys()
client.connect('10.153.0.46', username="root", password="pass")
stdin, stdout, stderr = client.exec_command('touch paramiko')

print(stdin,stdout, stderr)
import subprocess

cmd = ['git','--version']
proc = subprocess.Popen(cmd, stdout = subprocess.PIPE)
ver_str = proc.stdout.read().strip()
proc.stdout.close()
proc.wait()
print ver_str

ver_str = ver_str[len('git version '):].strip()
print ver_str


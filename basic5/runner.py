import subprocess

s = subprocess.run('behave ./features/tests/login.feature --no-capture',shell=True, check=True)
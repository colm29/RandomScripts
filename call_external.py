import subprocess
try:
    completed = subprocess.run('false',
                            capture_output=True,
                            text=True,
                            check=True)
    """ completed = subprocess.run(['ls','-l'],
                                capture_output=True,
                                text=True) """
    # completed = subprocess.run(['python3','something.py'],
    #                            capture_output=True,
    #                            text=True)
    print('args', completed.args)
    print('returncode', completed.returncode)
    print('stderr', completed.stderr)
    print('stdout', completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
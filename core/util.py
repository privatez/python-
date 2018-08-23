import subprocess
from platform import system as system_name


def ping(host: str, count: int = 1):
    param = '-n' if system_name().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]

    return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode('utf8')

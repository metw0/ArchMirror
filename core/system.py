import subprocess
from core.config import blacklist

def get_local_packages():
    try:
        raw_list = subprocess.run(['pacman', '-Qteq'], capture_output=True, text=True, check=True)
        return raw_list.stdout.splitlines()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []

def filter_packages(packages):
    return [pkg for pkg in packages if pkg not in blacklist]
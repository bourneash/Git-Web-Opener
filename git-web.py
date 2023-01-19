import subprocess

def get_remote_url():
    remote_url = subprocess.run(['git', 'config', '--get', 'remote.origin.url'], capture_output=True, text=True).stdout.strip()
    return remote_url

def open_remote_url(remote_url):
    if 'github' in remote_url:
        remote_url = remote_url.replace(':', '/').replace('git@', 'https://').replace('.git', '')
    elif 'gitlab' in remote_url:
        remote_url = remote_url.replace(':', '/').replace('git@', 'https://').replace('.git', '')
    else:
        print('Unsupported git service provider')
        return
    subprocess.run(['open', remote_url])

remote_url = get_remote_url()
open_remote_url(remote_url)

import pathlib
print('Welcome to the PyLib Installer!')
print('First, choose the folder to install PyLib.')
folder = input('folder>> ')
pathlib.Path(folder+'/libs/').mkdir(parents=True, exist_ok=True)
with open(folder+'/pl.py', 'w') as f:
    f.write(f'''import requests as r
import sys

def nstall(package):
    fd = '{folder}/libs/'
    url = 'https://github.com/Munder2/PyLib/raw/refs/heads/main/libs/'+package
    resp = r.get(url)
    print('Getting the package . . .')
    if resp.status_code == 200:
        print('Success!\\nDownloading the package . . .')
        with open(fd+package, 'wb') as f:
            f.write(resp.content)
        print('Success!')
    else:
        print('Failed to get the package.\\nTry looking for errors in the enterred package name.'); sys.exit(1)

if __name__ == '__main__':
    try:
        if sys.argv[1] == '-d':
            install(sys.argv[2])
        else:
            print('Usage: pl -d <package>'); sys.exit(1)
    except:
        print('Usage: pl -d <package>'); sys.exit(1)''')

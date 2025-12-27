import tomli
import argparse
import os

def restore_backup(file_path):
    with open(file_path, 'rb') as f:
        raw_data = tomli.load(f)

    packages_list = raw_data['packages']
    clean_data = ' '.join(packages_list)

    return clean_data

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', required=True)
    args = parser.parse_args()

    packages_string = restore_backup(args.path)
    command = f"sudo pacman -S --needed {packages_string}"

    print('Config successfully read')

    install_answer = input('Install read packages ? (y/n)').lower()
    if install_answer == 'y':
        exit_code = os.system(command)

        if exit_code == 0:
            print('Packages successfully installed')
        else:
            print(f'Installation failed with code: {exit_code}')
    elif install_answer not in ['y', 'n']:
        print('Answer error, try again')
    else:
        print('Ok...')
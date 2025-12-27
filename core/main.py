import os
import tomli_w
import argparse
from datetime import datetime
from core.system import get_local_packages, filter_packages


def create_backup(output_path, custom_name):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    raw = get_local_packages()
    pkgs = filter_packages(raw)

    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
    user = os.getlogin()

    manifest_data = {
        "meta": {
            'user': user,
            'date': date_str
        },
        'packages': pkgs
    }

    filename = custom_name if custom_name else f'manifest_{date_str}.toml'
    full_path = os.path.join(output_path, filename)

    with open(full_path, 'wb') as f:
        tomli_w.dump(manifest_data, f)
    print(f"Success ! Backup saved to: {full_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default='data')
    parser.add_argument('-n', '--name')
    args = parser.parse_args()

    create_backup(output_path=args.output, custom_name=args.name)
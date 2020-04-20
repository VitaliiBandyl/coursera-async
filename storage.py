import os
import json
import argparse
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--key", default='')
parser.add_argument("--val", default='')
args = parser.parse_args()

STORAGE = 'storage.data'
storage_path = os.path.join(tempfile.gettempdir(), STORAGE)
if args.key and args.val:
    if not os.path.exists(storage_path):
        args.val = [args.val]
        data = json.dumps({args.key: args.val})
        with open(storage_path, 'w') as f:
            f.write(data)
    else:
        with open(storage_path, 'r') as f:
            f = json.loads(f.read())
            if args.key in f:
                f[args.key].append(args.val)
            else:
                f[args.key] = [args.val]
            data = json.dumps(f)
        with open(storage_path, 'w') as f:
            f.write(data)
elif args.key:
    try:
        if os.path.exists(storage_path):
            with open(storage_path, 'r') as f:
                f = f.read()
                f = json.loads(f)
            print(*f[args.key], sep=', ')
    except:
        pass

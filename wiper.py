import os
import shutil

dir = 'data/'
for file in os.listdir(dir):
    path = os.path.join(dir, file)
    try:
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
    except Exception as e:
        print(f'Reason:{path}-{e}')
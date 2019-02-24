"""
Discription: A Python Progress Meter
Author: Nianzu Ethan Zheng
Date: 2018-1-21
Copyright
"""

import os
import pickle
import shutil
import pandas as pd


def make_dir(root, folder_name):
    path = os.path.join(root, folder_name)
    if not os.path.exists(path):
        os.makedirs(path)
        print(path)
        # os.chdir(path)            # change to the path
        return path
    print("Folder has existed!")
    return path


def delete_empty_dir(dir):
    if os.path.exists(dir):
        if os.path.isdir(dir):
            for d in os.listdir(dir):
                path = os.path.join(dir, d)
                if os.path.isdir(path):
                    delete_empty_dir(path)
        if not os.listdir(dir):
            os.rmdir(dir)
            print("remove the empty dir: {}".format(dir))
    else:
        print("Please start your performance!")


def check_dir(path, is_restart=False):
    name = os.path.split(path)[1]
    if not os.path.exists(path):
        os.makedirs(path)
        print('Create a new folder named {}'.format(name))
    elif is_restart:
        shutil.rmtree(path)
        os.makedirs(path)
        print('The folder named {} is restarted'.format(name))
    print('The folder named {} has existed.'.format(name))

def pickle_load(path_name, use_pd=False):
    with open(path_name, 'rb') as f:
        value, name = pickle.load(f)
    if use_pd:
        value = pd.DataFrame(value, columns=name)
    print("pickle named {} has been loaded...".format(name))
    return value, name


def pickle_save(value, name, path_name):
    with open(path_name, 'wb') as f:
        pickle.dump(value, f, protocol=pickle.HIGHEST_PROTOCOL)
    return print("data named {} has been saved...".format(name))

if __name__ == '__main__':
    check_dir('../Test')

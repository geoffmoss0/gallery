import os
from addict import Dict

def get_dir_tree_dict():
    path = os.path.normpath("images/root")
    file_tree = Dict()
    for root, dirs, files in os.walk(path, topdown=True):
        path = root.split('/')
        path.pop(0)
        file_tree_fd = file_tree
        for part in path:
            file_tree_fd = file_tree_fd[part]
        file_tree_fd['.'] = files

    return file_tree

def convert_bytes_to_utf8(dic):
    for key in dic:
        if isinstance(key, bytes):
            k = key.decode('utf-8')
            v = dic[key]
            del dic[key]
            dic[k] = v
        if isinstance(dic[key], bytes):
            v = dic[key].decode('utf-8')
            dic[key] = v
    return dic


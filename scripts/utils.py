def read_file(path):
    with open(path) as fin:
        return fin.read()


def write_file(path, content, is_binary=False):
    mode = "w"
    if is_binary:
        mode = "wb+"
    with open(path, mode) as fout:
        fout.write(content)

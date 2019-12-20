import torch
def get_version():
    return torch.__version__


if __name__ == '__main__':
    print(get_version())
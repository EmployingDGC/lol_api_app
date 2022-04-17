if __name__ == "__main__":
    import sys
    import os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))


import includes.tools as t


def main():
    print(t.get_yaml_configs())


if __name__ == "__main__":
    main()

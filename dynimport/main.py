def retrieve(name, loc=None):
    import importlib
    if loc in [None, "system", "user", "pypi"]:
        # TODO: Check if package exists first
        lib = importlib.import_module(name)
        print(f"Found '{name}' at {loc}, imported successfully!")
        return lib
    else:
        raise Exception(f"Couldn't retrieve {name}")


def install(name, loc=None):
    print(f"Installing {name} from {loc}")
    if loc in [None, "pypi"]:
        pipinstall(name)
        retrieve(name, loc)
    else:
        raise Exception(f"Couldn't install {name}, unknown location {loc}")


def pipinstall(package, loc=None):
    import subprocess
    import sys
    subprocess.call([sys.executable, "-m", "pip", "install", "--user", package])


def dimport(_id):
    _id_s = _id.split("@")
    if len(_id_s) > 1:
        name, loc = _id_s
    else:
        name = _id_s[0]

    if loc:
        # TODO: If location is given, check up the locator used
        pass

    try:
        return retrieve(name, loc)
    except Exception as e:
        print(f"Couldn't import {name}: {e}")
        install(name, loc)


def main():
    dimport("lib@system")
    dimport("takethetime@pypi")


if __name__ == "__main__":
    main()

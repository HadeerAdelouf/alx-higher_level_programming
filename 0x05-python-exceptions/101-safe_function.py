#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        X = fct(*args)
        return X
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None

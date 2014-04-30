#!/usr/bin/env python

import os
import sys
import time
import subprocess
import tempfile

def unpack_tiff(filename):

    print filename

    unpack_dir = tempfile.mkdtemp()

    unpack_pattern = os.path.join(unpack_dir, 'stack-%d.tif')

    subprocess.call(['convert', filename, unpack_pattern])

    return unpack_dir

def write_watchfile(filename, stack_dir):

    watch_str = "open_image_stack(0, '%s')\n" % stack_dir

    with open(filename, "w") as f:
        f.write(watch_str)

def invoke_volviewer(watch_filename):
    volviewer = "/common/software/VolViewer/VolViewer"

    invocation = "set_watchfile('%s')" % watch_filename

    subprocess.Popen([volviewer, invocation])

def main():

    filename = sys.argv[1]
    unpack_dir = unpack_tiff(filename)

    fh, watch_fn = tempfile.mkstemp(suffix='.txt')

    print watch_fn

    invoke_volviewer(watch_fn)

    time.sleep(3)
    
    write_watchfile(watch_fn, unpack_dir)




if __name__ == "__main__":
    main()




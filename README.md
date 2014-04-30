# VVBridge

VolViewer-Fiji bridge.

Provides a mechanism to allow opening of confocal microscopy images stored in
OMERO via the Fiji client.

# Mechanism of operation

* Fiji copies the image (as an OME-TIF) to temporary storage space and passes
vvbridge the location of the file as a parameter.

* vvbridge uses convert to unpack the multipage tif into multiple single tifs.

* vvbridge then invokes VolViewer with a command to watch a specific file.

* vvbridge waits until VolViewer is ready and then writes the location of the stack to the watch file, causing VolViewer to open it.

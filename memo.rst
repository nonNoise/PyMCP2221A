======================================================================================
Memo.
======================================================================================


How to build hidlib ?
---------------------------------------------------------------------------------------

Download cython-hidapi archive:

    $ git clone https://github.com/trezor/cython-hidapi.git

    $ cd cython-hidapi

Initialize hidapi submodule:

    $ git submodule update --init

Build cython-hidapi extension module:

    $ python setup.py build

To use hidraw API instead of libusb add --without-libusb option:

    $ python setup.py build --without-libusb


How did run at Raspberry Pi?
---------------------------------------------------------------------------------------

git clone https://github.com/nonNoise/PyMCP2221A.git

python

    from PyMCP2221A import PyMCP2221A

    
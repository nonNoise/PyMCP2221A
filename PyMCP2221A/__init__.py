import platform
plat = platform.platform()
if  ("armv7l" or "armv6l")  in plat :
    from binary import hid
else:
    import hid

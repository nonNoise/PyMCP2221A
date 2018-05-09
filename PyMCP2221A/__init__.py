import platform
plat = platform.platform()
if  ("armv7l" or "armv6l")  in plat :
    from raspberrypi import hid
else:
    import hid

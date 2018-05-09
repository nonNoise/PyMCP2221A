import platform
plat = platform.platform()
if  ("armv7l")  in plat :
    from lib_linux_armv7l_2_7 import hid
else:
    import hid
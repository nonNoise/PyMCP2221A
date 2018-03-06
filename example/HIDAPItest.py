import hid
# Check all  usb device
for d in hid.enumerate(0x04D8, 0x00DD):
    keys = d.keys()
    #keys.sort()
    for key in keys:
        print ("%s : %s" % (key, d[key]))

    print ("")

print(hid.enumerate(0x04D8, 0x00DD)[0]["path"])
mcp2221a = hid.device()
#mcp2221a.open(VID,PID)
mcp2221a.open_path(hid.enumerate(0x04D8, 0x00DD)[0]["path"])

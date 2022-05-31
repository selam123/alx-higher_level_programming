#!/usr/bin/python3
# except q and e
for k in range(97, 123, 1):
    if k == 113 or k == 101:
        pass
    else:
        print('{}'.format(chr(k)), end="")

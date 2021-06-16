def Hello_World(i=0):
    try:
        __import__(__import__("sys")._getframe().f_code.co_name.replace(chr(95), chr(32))[::-1][i] + str(Hello_World(i=i+1)))
    except Exception as e:
        __import__("sys").stdout.write(str(e).split("'")[-2].split(str(None))[0] if str(e)[0] not in "sl" else "")

Hello_World()
import asyncio
import sys
from acmd import Cmd

class FooCmd(Cmd):

    prompt = '(test)'

    def do_hello(self, arg):
        print('hello:{}'.format(arg))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    foo = FooCmd()

    foo.cmdloop(loop=loop)

    try:
        loop.run_forever()  # our cmd will run automatically from this moment
    except KeyboardInterrupt:
        loop.stop()
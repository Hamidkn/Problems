import argparse
from synchronize import sync

if __name__=='__main__':

    parser = argparse.ArgumentParser('Synchronization')

    parser.add_argument("-s", "--source", help="define source path.")
    parser.add_argument("-d", "--replica", help="define destination path.")
    parser.add_argument("-l", "--log", help="log file.")
    parser.add_argument("-a", "--action", help="define an action(r for remove, c for copy).", default='r')
    parser.add_argument("-n", "--n", help="Number of interval.", default=1)

    args = parser.parse_args()
    source = args.source
    replica = args.replica
    log = args.log
    action = args.action
    n = int(args.n)

    synchronize = sync(source, replica, log, action)

    for i in range(n):
        synchronize.look_into()
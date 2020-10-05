#Imports
import argparse
from datetime import datetime
# Import local scripts
import read_write_serial


class color():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    N = '\033[0m'

#Arguments   
argparser = argparse.ArgumentParser(description='SMLParser is an Python based SML(OBIS) Parser')
requiredNamed = argparser.add_argument_group('required arguments')
requiredNamed.add_argument('-sp', '--serialport', help='Serial Port')
argparser.add_argument('-lf', '--log-file', help='Defines the log file')


args = argparser.parse_args()
if not args.serialport:
    print("{}[!]{} You need to define the Serialport! {}-sp [SerialPort]{}".format(color.RED, color.N, color.YELLOW, color.N))
    quit()
#Print Serial-Port
print("{}[i]{} Serial Port is: {}{}{}".format(color.GREEN, color.N, color.YELLOW, args.serialport, color.N))

if args.log_file:
    print("{}[i]{} Log file-path is: {}{}{}".format(color.GREEN, color.N, color.YELLOW, args.log_file, color.N))

#Print Date and time
now = datetime.now()
now_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("{}[i]{} Started at: {}{}{}".format(color.GREEN, color.N, color.YELLOW, now_date_time, color.N))

#Testing
print(read_write_serial.readSerial(args.serialport, 100))
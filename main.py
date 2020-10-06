# Imports
import argparse
from datetime import datetime

# Import local scripts
import read_write_serial
import print_logging

# Define
print_log = print_logging.print_logging


class color:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    N = "\033[0m"


# Arguments
argparser = argparse.ArgumentParser(
    description="SMLParser is an Python based SML(OBIS) Parser"
)
requiredNamed = argparser.add_argument_group("required arguments")
requiredNamed.add_argument("-sp", "--serialport", help="Serial Port")
argparser.add_argument("-lf", "--log-file", help="Defines the log file")
argparser.add_argument(
    "-v",
    "--log-level",
    help="Loglevel 0=Off 1= Error 2=Info 3=Debug 4=Everything - Default 2",
)

args = argparser.parse_args()
# Loglevel 0=Off 1= Error 2=Info 3=Debug 4=Everything - Default 2
if args.log_level:
    if int(args.log_level) >= 1:
        print(
            "{}[i]{} Loglevel is: {}{}{}".format(
                color.GREEN, color.N, color.YELLOW, args.log_level, color.N
            )
        )
    loglevel = args.log_level
else:
    loglevel = 2

if not args.serialport:
    if int(loglevel) >= 1:
        print_log(
            "{}[!]{} You need to define the Serialport! {}-sp [SerialPort]{}".format(
                color.RED, color.N, color.YELLOW, color.N
            ),
            loglevel,
            args,
        )
    quit()
# Print Serial-Port
print_log(
    "{}[i]{} Serial Port is: {}{}{}".format(
        color.GREEN, color.N, color.YELLOW, args.serialport, color.N
    ),
    loglevel,
    args,
)


if args.log_file:
    print_log(
        "{}[i]{} Log file-path is: {}{}{}".format(
            color.GREEN, color.N, color.YELLOW, args.log_file, color.N
        ),
        loglevel,
        args,
    )

# Print Date and time
now = datetime.now()
now_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print_log(
    "{}[i]{} Started at: {}{}{}".format(
        color.GREEN, color.N, color.YELLOW, now_date_time, color.N
    ),
    loglevel,
    args,
)

# Testing
# print(read_write_serial.readSerial(args.serialport, 100))

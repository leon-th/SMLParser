import re

def log(text, loglevel, args):
    with open(args.log_file, "a") as log_file:
        log_file.write("\n")
        #Remove Ascii Escape(Colors)
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        result = ansi_escape.sub('', text)
        log_file.write(result)

def print_logging(text, loglevel, args):
    print(text)
    if args.log_file:
        log(text, loglevel, args)
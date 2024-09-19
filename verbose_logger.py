verbose_log = ""

log = {}

commands = {}

def clear_log():
    global verbose_log
    global  log
    verbose_log = ""
    for key in log:
        log[key] = ""


def create_logger(test_case):
    test_case = test_case.lower()
    if test_case not in log:
        log[test_case] = ""

    def append_msg(message):
        log[test_case] += f"\n{message}"

    return append_msg

def view_log(cases=None):
    if cases is None or cases == ['']:
        cases = input("Enter the countries you would like to view separated by semi-colons (ex: cuba; us virgin islands\n")
        cases = cases.split(';')

    for c in cases:
        c = c.strip().lower()
        print_log(c)

def print_log(test_case):
    try:
        delimiter_length = 40 + len(test_case)
        header_length = (delimiter_length - len(test_case)) // 2
        header_wing = "=" * header_length
        header = header_wing + test_case.upper() + header_wing
        delimiter = "=" * delimiter_length
        print(f"\n{header}")
        print(log[test_case])
        print(f"\n{delimiter}")
    except KeyError:
        print(f"No associated log for {test_case}\n")



def control_flow(cmd_key, **kwargs):
    if cmd_key in commands:
        commands[cmd_key]()
    else:
        return


def register_command(func, cmd_key):
    commands[cmd_key] = func
verbose_log = ""

log = {}

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




# DEPRECATED
def append_log(message, test_case):
    test_case = test_case.lower()
    global verbose_log
    global log
    verbose_log += f"\n{message}"
    log[test_case] += f"\n{message}"

# Current Issue:
# I have to manually look through every log to find relevant test cases. If I'm confused why 'Inia' is more similar to 'Cuba' than 'India'...
# ...I don't care about the log for "US VIRGIN ISLANDS"
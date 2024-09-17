verbose_log = ""

def clear_log():
    global verbose_log
    verbose_log = ""


def append_log(message):
    global verbose_log
    verbose_log += f"\n{message}"

# Current Issue:
# I have to manually look through every log to find relevant test cases. If I'm confused why 'Inia' is more similar to 'Cuba' than 'India'...
# ...I don't care about the log for "US VIRGIN ISLANDS"
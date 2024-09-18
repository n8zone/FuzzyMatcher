from sys import stdout
from time import perf_counter
import verbose_logger
from verbose_logger import create_logger, clear_log, print_log, view_log
from countries import COUNTRIES, test_cases

STDOUT = create_logger("stdout")
MAX_LEN_DIFF = 4

# Reconsider using default arg for log, I'd prefer to keep algorithm functions and logger decoupled
def compare_strings(s1, s2, log=STDOUT):
    changes = 0
    checking_string = s1
    s1 = s1.lower()
    s2 = s2.lower()

    log(f"Testing {s1} against {s2}")

    s2_offset = 0 # guh
    for i in range(len(s1)):
        char_to_check = s1[i]

        try:
            compared_to = s2[i + s2_offset]
        except IndexError:
            new_changes = (len(s1) - len(s2))
            log(f"Reached the end of {s2}, adding {new_changes} new changes.")
            changes += new_changes
            break

        if char_to_check == compared_to:
            continue

        # Insertion handling
        if len(s1) > len(s2):
            next_char_exists = (i + 1) < len(s1)

            next_char_is_target = s1[i + 1] == compared_to if next_char_exists else False

            should_insert = next_char_exists and next_char_is_target

            # Here I simulate an insertion by telling the s2 pointer to lag
            if should_insert:
                s2_offset -= 1


        elif len(s2) > len(s1):
            prev_char_exists = (i - 1) >= 0
            prev_char_is_target = s1[i - 1] == compared_to if prev_char_exists else False

            should_delete = prev_char_exists and prev_char_is_target

            if should_delete:
                s2_offset += 1

        log(f"{compared_to} is not {char_to_check}, adding one change")
        changes += 1

    steps = i # lazy workaround for changing all instances of i for now
    return changes, steps


def get_most_similar(entry, known):
    known_copy = known.copy()
    filtered = list(filter(lambda s: abs(len(s) - len(entry)) < MAX_LEN_DIFF, known_copy))
    STDOUT(f"Filtered countries from {len(known)} entries to {len(filtered)} entries\n{filtered}")

    #               str, changes, steps
    most_similar = ("ok", 9999, 9999)

    matching = []
    for string in filtered:
        log = create_logger(string)
        changes, steps = compare_strings(s1=string, s2=entry, log=log)

        if changes < most_similar[1]:
            STDOUT(f"Changing most_similar from {most_similar} to {(string, changes)}.")
            most_similar = (string, changes, steps)
            matching = [most_similar]

        elif changes == most_similar[1]:
            STDOUT(f"Changing most_similar from {most_similar} to {(string, changes, steps)}.")
            matching_case = (string, changes, steps)

            matching = matching + [matching_case]
            STDOUT(f"{matching} <<<MATCHING")


        log(f"Result: {(string, changes, steps)}")

    matching_words = []
    for group in matching:
        matching_words.append(group[0])

    STDOUT(f"Matching words: {matching_words}")

    return matching_words





def main():
    case_number = 1
    for case in test_cases:
        trying = case[0]
        start = perf_counter()
        output = get_most_similar(trying, COUNTRIES)

        output_len = len(output)

        if output_len > 1:
            # handle that
            print(f"Found {output_len} matching words ({output})!")

            for i in range(output_len):
                print(f"{i+1}. {output[i]}")

            choice = -1

            while choice - 1 not in range(output_len):
                try:
                    choice = int(input("Please enter the digit corresponding to the correct word: "))
                except:
                    print("Please enter a valid integer within the range of the list")


            output = output[choice - 1]
        else:
            output = output[0]

        end = perf_counter()
        time_to_execute = (end - start) * 1000
        STDOUT(f"Time to execute: {time_to_execute}ms")
        print(f"\n=========CASE {case_number}============")
        print(f"Input: {trying}\nExpecting: {case[1]}\nActual: {output}")
        print(f"=========CASE {case_number}============\n")

        result = "success" if output == case[1] else "fail"

        if result == "success":
            verbose_logger.clear_log()
            case_number += 1
            continue

        next_instr = ""


        while next_instr != "n":



            if next_instr == "s":
                view_log(["stdout"])
                input()

            if next_instr == "vr":
                cases = [case[1], output]
                view_log(cases)
                input()
            elif next_instr != '' and next_instr[0].lower() == 'v':
                cases = next_instr[2::].split(';')
                print(cases)
                view_log(cases)
                print(
                    f"Changes to {output}: {compare_strings(trying, output)}\nChanges to expected: {compare_strings(case[1], trying)}")
                input()


            next_instr = input(
                "Enter 'vr' to view relevant logs\nEnter 'v' to view specific logs by country\nEnter 's' to view stdout\nEnter 'n' to continue to next case...")



        verbose_logger.clear_log()
        case_number += 1





if __name__ == '__main__':
    main()
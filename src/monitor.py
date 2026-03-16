import time
from log_parser import parse_logs
from attack_detector import detect_attacks
from report_generator import generate_report


def monitor_logs(logfile):

    print("Monitoring SSH logs...\n")

    last_size = 0

    while True:

        with open(logfile, "r") as file:

            file.seek(last_size)

            new_lines = file.readlines()

            if new_lines:

                events = parse_logs(logfile)

                attackers = detect_attacks(events)

                generate_report(attackers)

            last_size = file.tell()

        time.sleep(5)

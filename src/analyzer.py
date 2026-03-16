import sys
from log_parser import parse_logs
from attack_detector import detect_attacks
from report_generator import generate_report
from monitor import monitor_logs


def main():

    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <logfile> [--monitor]")
        return

    logfile = sys.argv[1]

    if len(sys.argv) > 2 and sys.argv[2] == "--monitor":
        monitor_logs(logfile)
        return

    events = parse_logs(logfile)

    attackers = detect_attacks(events)

    generate_report(attackers)


if __name__ == "__main__":
    main()

import argparse

parser = argparse.ArgumentParser(
    description="zVM Exporter for Prometheus. Metrics are exported to "
                "localhost.")

parser.add_argument(
    "-f", "--logfile",
    help="Output log file. If not provided, logs will not be output to "
            "file.")

parser.add_argument(
    "-p", "--port",
    help="Port on which to expose metrics. (defaults to 8009)",
    type=int,
    default='8009')

parser.add_argument(
    "--server",
    help="Address to the zVM SDK server. (port defaults to 8909)",
    required=True)

parser.add_argument(
    "--timeout",
    help="Timeout",
    type=int,
    default=3600)

parser.add_argument(
    "--token",
    help="Admin Token to authorize.",
    required=True)


parser.add_argument(
    "-v", "--version",
    action="version", version="%(prog)s " + __version__)

parser.add_argument(
    "--cert",
    help="SSL cert file. If not provided, SSL verification is disabled.",
    default=None)

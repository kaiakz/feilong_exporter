import argparse
from exporter import start_exporter
import configparser

def main():
    argparser = argparse.ArgumentParser(
        description="zVM Exporter for Prometheus. Metrics are exported to "
                    "localhost.")
    argparser.add_argument(
        "-f", "--logfile",
        help="Output log file. If not provided, logs will not be output to "
                "file.")
    argparser.add_argument(
        "-p", "--port",
        help="Port on which to expose metrics. (defaults to 8009)",
        type=int,
        action="store",
        default='8009')
    argparser.add_argument(
        "--server",
        help="Address to the zVM SDK server. (port defaults to 8909)",
        action="store",
        required=True)
    argparser.add_argument(
        "--timeout",
        help="Timeout",
        type=int,
        action="store",
        default=3600)
    argparser.add_argument(
        "--token",
        help="Path to admin token",
        action="store",
        required=True)

    args = argparser.parse_args()
    ip, port = args.server.split(':')
    if ip == None:
        print("Error server address")
    start_exporter(ip_addr=ip, port=int(port))

def load_servers(filename:str) -> dict:
    config = configparser.ConfigParser()
    config.read(filename, encoding='utf-8')
    servers = config.sections()
    
    
# Export them to Prometheus
if __name__ == "__main__":
    main()
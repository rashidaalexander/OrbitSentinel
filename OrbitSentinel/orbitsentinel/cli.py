
from __future__ import annotations
import argparse
from .engine import analyze
from .utils import to_json

def main() -> None:
    parser = argparse.ArgumentParser(prog="orbitsentinel")
    sub = parser.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("analyze")
    a.add_argument("path")
    r = sub.add_parser("report")
    r.add_argument("path")
    args = parser.parse_args()
    result = analyze(args.path)
    if args.cmd == "report":
        print("# OrbitSentinel Report\n")
        print(to_json(result))
    else:
        print(to_json(result))

if __name__ == "__main__":
    main()

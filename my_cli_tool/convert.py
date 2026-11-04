import csv
import json
from pathlib import Path


def run(args):
    if args.kind == "csv2json":
        rows = []
        with open(args.input, encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                rows.append(row)
        Path(args.output).write_text(
            json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"")
        print(f"CSV -> JSON：转了 {len(rows)} 行，输出 {args.output}")
    else:  # json2csv
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        if not isinstance(data, list) or not data:
            print("输入 JSON 必须是对象数组，且非空")
            return
        keys = list(data[0].keys())
        with open(args.output, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(data)
        print(f"JSON -> CSV：转了 {len(data)} 行，输出 {args.output}")

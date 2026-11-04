import urllib.request
from pathlib import Path


def run(args):
    req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    Path(args.out).write_bytes(data)
    print(f"已保存 {len(data)} 字节到 {args.out}")

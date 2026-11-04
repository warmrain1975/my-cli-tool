import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path


def run(args):
    params = {}
    for kv in args.params:
        if "=" in kv:
            k, v = kv.split("=", 1)
            params[k] = v

    url = args.url
    if params and args.method.upper() == "GET":
        sep = "&" if "?" in url else "?"
        url = url + sep + urllib.parse.urlencode(params)

    req = urllib.request.Request(url, method=args.method.upper())
    status = ""
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode("utf-8", errors="replace")
            status = str(r.status)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        status = f"HTTP {e.code}"

    print(f"状态: {status}")
    if args.out:
        Path(args.out).write_text(body, encoding="utf-8")
        print(f"响应已存到 {args.out}")
    else:
        print(body[:2000])

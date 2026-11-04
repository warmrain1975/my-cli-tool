import argparse
from . import rename, fetch, api, convert


def main():
    parser = argparse.ArgumentParser(prog="mycli", description="个人命令行小工具集（零第三方依赖）")
    sub = parser.add_subparsers(dest="command", required=True)

    # rename
    p = sub.add_parser("rename", help="批量改名：对目录下文件名做字符串替换")
    p.add_argument("directory", help="要处理的目录")
    p.add_argument("--pattern", required=True, help="要被替换掉的文字")
    p.add_argument("--replacement", default="", help="替换成什么（默认空串，即删除）")
    p.add_argument("--dry-run", action="store_true", help="只预览，不真改")
    p.set_defaults(func=rename.run)

    # fetch
    p = sub.add_parser("fetch", help="抓一个网页，存成本地 HTML 文件")
    p.add_argument("url", help="网页地址")
    p.add_argument("--out", required=True, help="保存到哪个文件")
    p.set_defaults(func=fetch.run)

    # api
    p = sub.add_parser("api", help="简单调一个 HTTP API")
    p.add_argument("url", help="接口地址")
    p.add_argument("--method", default="GET", help="GET 或 POST")
    p.add_argument("--params", nargs="*", default=[], help="查询参数，写成 key=value")
    p.add_argument("--out", help="把响应体存到文件")
    p.set_defaults(func=api.run)

    # convert
    p = sub.add_parser("convert", help="CSV <-> JSON 互转")
    p.add_argument("kind", choices=["csv2json", "json2csv"])
    p.add_argument("input", help="输入文件")
    p.add_argument("output", help="输出文件")
    p.set_defaults(func=convert.run)

    args = parser.parse_args()
    args.func(args)

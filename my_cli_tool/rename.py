from pathlib import Path


def run(args):
    d = Path(args.directory)
    if not d.is_dir():
        print(f"目录不存在: {d}")
        return
    count = 0
    for f in d.iterdir():
        if not f.is_file():
            continue
        if args.pattern not in f.name:
            continue
        new_name = f.name.replace(args.pattern, args.replacement)
        new_path = d / new_name
        if new_path.exists():
            print(f"跳过（目标已存在）: {f.name}")
            continue
        if args.dry_run:
            print(f"预览: {f.name}  ->  {new_name}")
        else:
            f.rename(new_path)
            print(f"改名: {f.name}  ->  {new_name}")
        count += 1
    print(f"共处理 {count} 个文件")

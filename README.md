# my-cli-tool

个人自用的命令行小工具集。纯 Python 标准库，零第三方依赖，Python 3.8+ 直接跑。

## 安装

不需要 pip install。clone 下来就能用：

```powershell
git clone https://github.com/warmrain1975/my-cli-tool.git
cd my-cli-tool
```

## 用法

统一入口：`python -m my_cli_tool <子命令> [参数]`

### 1. rename —— 批量改名

把某个目录下文件名里的 `旧文字` 全部换成 `新文字`。

```powershell
# 先预览，不动手
python -m my_cli_tool rename D:\照片 --pattern "副本_" --replacement "" --dry-run

# 确认没问题，真改
python -m my_cli_tool rename D:\照片 --pattern "副本_" --replacement ""
```

### 2. fetch —— 抓网页

把一个网页的原始 HTML 存到本地。

```powershell
python -m my_cli_tool fetch https://example.com --out page.html
```

### 3. api —— 调 HTTP 接口

```powershell
# GET，带参数
python -m my_cli_tool api "https://api.github.com/search/repositories" --params q=python language=python

# 响应存文件
python -m my_cli_tool api "https://httpbin.org/get" --out resp.json
```

### 4. convert —— CSV/JSON 互转

```powershell
# CSV 转 JSON（自动识别 Excel 导出的 UTF-8 BOM）
python -m my_cli_tool convert csv2json input.csv output.json

# JSON 转 CSV（要求 JSON 是对象数组）
python -m my_cli_tool convert json2csv input.json output.csv
```

## 目录结构

```
my_cli_tool/
├── __main__.py    # 入口
├── cli.py         # argparse 注册子命令
├── rename.py      # 批量改名
├── fetch.py       # 抓网页
├── api.py         # 调 API
└── convert.py     # CSV/JSON 互转
```

想加新功能：在 `my_cli_tool/` 下新建一个 `.py`，写个 `run(args)` 函数，再到 `cli.py` 里注册一个子命令就行。

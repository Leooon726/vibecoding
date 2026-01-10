#!/usr/bin/env python3
"""每隔1秒打印一次的简单脚本"""

import time

def main():
    count = 1
    while True:
        print(f"第 {count} 次打印 - 当前时间: {time.strftime('%H:%M:%S')}")
        count += 1
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n程序已停止")

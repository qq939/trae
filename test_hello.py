# 测试脚本：验证 hello.py 能正确打印 "hello world"
# 包含超时机制，防止脚本挂起
import subprocess
import sys
import os

# 超时时间（秒）
TIMEOUT_SECONDS = 10

def test_hello_world_output():
    """测试 hello.py 输出是否为 'hello world'"""
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hello.py")

    # 使用 subprocess 运行脚本，设置超时
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS
        )
    except subprocess.TimeoutExpired:
        print(f"FAIL: 脚本执行超时（超过 {TIMEOUT_SECONDS} 秒）")
        return False

    # 检查退出码
    if result.returncode != 0:
        print(f"FAIL: 脚本退出码非0，stderr: {result.stderr.strip()}")
        return False

    # 检查输出内容（忽略首尾空白）
    output = result.stdout.strip()
    if output == "hello world":
        print("PASS: 输出正确 -> 'hello world'")
        return True
    else:
        print(f"FAIL: 输出不匹配，实际输出: '{output}'，期望: 'hello world'")
        return False

if __name__ == "__main__":
    success = test_hello_world_output()
    sys.exit(0 if success else 1)

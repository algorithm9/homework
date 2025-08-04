#!/usr/bin/env python3
"""
测试MCP服务器的简单脚本
"""
import subprocess
import json
import sys

def test_mcp_server():
    """测试MCP服务器是否能正常响应"""
    try:
        # 启动MCP服务器进程
        process = subprocess.Popen(
            ['uv', 'run', 'weather.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd='/Users/lichengshan/weather'
        )
        
        # 发送初始化请求
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        }
        
        # 发送请求
        request_str = json.dumps(init_request) + '\n'
        process.stdin.write(request_str)
        process.stdin.flush()
        
        # 读取响应
        response = process.stdout.readline()
        if response:
            print("MCP服务器响应:", response.strip())
            return True
        else:
            print("MCP服务器无响应")
            return False
            
    except Exception as e:
        print(f"测试失败: {e}")
        return False
    finally:
        if 'process' in locals():
            process.terminate()

if __name__ == "__main__":
    print("测试MCP服务器...")
    success = test_mcp_server()
    sys.exit(0 if success else 1)

#!/usr/bin/env python3
"""
自动添加MCP服务器配置的脚本
"""
import json
import os
from pathlib import Path

def add_weather_mcp_config():
    # MCP设置文件路径
    mcp_settings_path = Path.home() / "Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json"
    
    # 要添加的weather服务器配置
    weather_config = {
        "weather": {
            "disabled": False,
            "timeout": 60,
            "type": "stdio",
            "command": "uv",
            "args": [
                "--directory",
                "/Users/lichengshan/weather",
                "run",
                "weather.py"
            ]
        }
    }
    
    try:
        # 读取现有配置
        if mcp_settings_path.exists():
            with open(mcp_settings_path, 'r', encoding='utf-8') as f:
                current_config = json.load(f)
        else:
            current_config = {"mcpServers": {}}
        
        # 确保mcpServers键存在
        if "mcpServers" not in current_config:
            current_config["mcpServers"] = {}
        
        # 添加weather配置
        current_config["mcpServers"].update(weather_config)
        
        # 写回文件
        with open(mcp_settings_path, 'w', encoding='utf-8') as f:
            json.dump(current_config, f, indent=2, ensure_ascii=False)
        
        print("✅ Weather MCP服务器配置已成功添加!")
        print(f"配置文件位置: {mcp_settings_path}")
        print("\n添加的配置:")
        print(json.dumps(weather_config, indent=2, ensure_ascii=False))
        
    except Exception as e:
        print(f"❌ 添加配置时出错: {e}")
        return False
    
    return True

if __name__ == "__main__":
    add_weather_mcp_config()

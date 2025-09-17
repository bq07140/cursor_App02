#!/usr/bin/env python3
"""
后端服务启动脚本
"""
import uvicorn
import os

if __name__ == "__main__":
    # 确保在正确的目录下运行
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print(f"当前工作目录: {os.getcwd()}")
    print("启动FastAPI服务...")
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["app"]
    )

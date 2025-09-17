# 待办事项管理系统

一个基于现代Web技术栈的全栈待办事项管理应用，采用前后端分离架构，支持任务的增删改查、状态管理和筛选功能。

## 🚀 技术栈

### 前端技术栈
- **框架**: React 18.2.0
- **构建工具**: Vite 5.0.8
- **HTTP客户端**: Axios 1.6.0
- **样式**: CSS3 (现代化响应式设计)

### 后端技术栈
- **框架**: FastAPI 0.115.0
- **ASGI服务器**: Uvicorn 0.32.0
- **ORM**: SQLAlchemy 2.0.36
- **数据验证**: Pydantic 2.9.2
- **数据库**: SQLite 3
- **Python版本**: 3.8+

## 📁 项目结构

```
cursor_App02/
├── backend/                 # 后端目录
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # FastAPI应用入口
│   │   ├── models.py       # 数据模型
│   │   ├── schemas.py      # Pydantic模式
│   │   ├── database.py     # 数据库配置
│   │   ├── crud.py         # CRUD操作
│   │   └── api/
│   │       └── todos.py    # 待办事项API路由
│   ├── requirements.txt    # Python依赖
│   ├── start_server.py     # 服务启动脚本
│   ├── test_main.py        # API测试
│   └── README.md          # 后端文档
├── frontend/              # 前端目录
│   ├── public/
│   │   └── vite.svg       # 图标文件
│   ├── src/
│   │   ├── components/    # React组件
│   │   │   ├── TodoForm.jsx
│   │   │   ├── TodoList.jsx
│   │   │   ├── TodoItem.jsx
│   │   │   ├── TodoFilter.jsx
│   │   │   └── TodoActions.jsx
│   │   ├── services/
│   │   │   └── api.js     # API服务
│   │   ├── styles/
│   │   │   ├── index.css  # 全局样式
│   │   │   └── App.css    # 应用样式
│   │   ├── App.jsx        # 根组件
│   │   └── main.jsx       # 应用入口
│   ├── package.json       # 前端依赖
│   ├── vite.config.js     # Vite配置
│   └── README.md          # 前端文档
├── start_backend.bat      # Windows后端启动脚本
├── start_frontend.bat     # Windows前端启动脚本
└── README.md              # 项目总览文档
```

## 🎯 功能特性

### 核心功能
- ✅ **添加待办事项** - 支持标题和描述输入
- ✅ **查看待办列表** - 美观的卡片式布局显示
- ✅ **标记完成** - 一键切换完成状态
- ✅ **删除事项** - 单个删除功能
- ✅ **筛选显示** - 全部/未完成/已完成三种筛选模式
- ✅ **批量操作** - 清除已完成事项/清除全部事项
- ✅ **进度显示** - 实时进度条和统计信息

### 用户体验
- 🎨 **现代UI设计** - 渐变背景、圆角、阴影等现代元素
- 📱 **响应式设计** - 完美适配移动端和桌面端
- ⚡ **流畅动画** - hover效果、过渡动画、加载状态
- 🔔 **友好提示** - 错误信息展示和操作确认
- 📊 **数据可视化** - 进度条和统计图表

## 🚀 快速开始

### 1. 环境要求

- Python 3.8+ 
- Node.js 16.0+
- npm 或 yarn

### 2. 后端启动

```bash
# 方式一：使用启动脚本 (Windows)
start_backend.bat

# 方式二：手动启动
cd backend
pip install -r requirements.txt
python start_server.py
```

后端服务将运行在 http://localhost:8000

### 3. 前端启动

```bash
# 方式一：使用启动脚本 (Windows)
start_frontend.bat

# 方式二：手动启动
cd frontend
npm install
npm run dev
```

前端应用将运行在 http://localhost:3000

### 4. 访问应用

打开浏览器访问 http://localhost:3000 即可使用待办事项管理系统。

## 🌐 API接口

### 基础信息
- **Base URL**: `http://localhost:8000`
- **Content-Type**: `application/json`

### 主要接口
- `GET /api/todos` - 获取待办事项列表
- `POST /api/todos` - 创建待办事项
- `PUT /api/todos/{id}` - 更新待办事项
- `PATCH /api/todos/{id}/toggle` - 切换完成状态
- `DELETE /api/todos/{id}` - 删除待办事项
- `DELETE /api/todos/completed` - 批量删除已完成
- `DELETE /api/todos/all` - 清空所有待办事项

详细API文档请访问：http://localhost:8000/docs

## 🗄️ 数据库设计

### todos表结构
```sql
CREATE TABLE todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## 🧪 测试

### 后端测试
```bash
cd backend
python -m pytest test_main.py -v
```

### 前端测试
```bash
cd frontend
npm run lint
```

## 📚 文档

- [后端文档](backend/README.md) - 详细的后端开发和API文档
- [前端文档](frontend/README.md) - 详细的前端开发和组件文档
- [技术架构](TECH_ARCHITECTURE.md) - 完整的技术架构设计文档

## 🎨 界面预览

### 主界面
- 现代化渐变背景设计
- 居中显示，最大宽度800px
- 卡片式布局，优雅的阴影效果

### 功能区域
- **添加表单** - 简洁的输入框和按钮
- **筛选标签** - 全部/未完成/已完成切换
- **待办列表** - 美观的列表项展示
- **操作按钮** - 完成、删除等操作按钮
- **进度显示** - 可视化进度条和统计

## 🔧 开发指南

### 后端开发
1. 修改数据模型: `backend/app/models.py`
2. 更新API接口: `backend/app/api/todos.py`
3. 添加业务逻辑: `backend/app/crud.py`
4. 运行测试: `python -m pytest test_main.py -v`

### 前端开发
1. 创建新组件: `frontend/src/components/`
2. 修改样式: `frontend/src/styles/`
3. 更新API调用: `frontend/src/services/api.js`
4. 测试功能: `npm run dev`

## 🚀 部署

### 开发环境
- 后端: `python start_server.py`
- 前端: `npm run dev`

### 生产环境
- 后端: Docker容器 + Nginx反向代理
- 前端: `npm run build` 后部署静态文件

## 🐛 常见问题

### Q: 后端服务启动失败
A: 检查Python版本和依赖安装，确保在backend目录下运行启动脚本。

### Q: 前端无法连接后端
A: 确认后端服务运行在8000端口，检查CORS配置。

### Q: 数据库错误
A: 删除`backend/todos.db`文件，重启后端服务自动重建数据库。

## 📝 更新日志

### v1.0.0 (2025-09-17)
- ✨ 初始版本发布
- ✅ 完整的前后端功能实现
- 🎨 现代化UI设计
- 📚 完善的文档和测试
- 🚀 便捷的启动脚本

## 🤝 贡献

欢迎提交Issues和Pull Requests来改进这个项目！

## 📄 许可证

本项目采用 MIT 许可证。

---

**开发完成！🎉 享受您的待办事项管理体验！**
# cursor_App02

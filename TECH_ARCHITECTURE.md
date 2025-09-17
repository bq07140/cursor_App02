# 待办事项应用技术架构文档

## 项目概述

这是一个基于现代Web技术栈的待办事项管理应用，采用前后端分离架构，支持任务的增删改查、状态管理和筛选功能。

## 技术栈

### 前端技术栈
- **框架**: React 18+
- **构建工具**: Vite
- **状态管理**: React Hooks (useState, useEffect)
- **HTTP客户端**: Axios
- **样式**: CSS3 (现代化响应式设计)
- **包管理器**: npm/yarn

### 后端技术栈
- **框架**: FastAPI 0.104.1
- **ASGI服务器**: Uvicorn 0.24.0
- **ORM**: SQLAlchemy 2.0.23
- **数据验证**: Pydantic 2.5.0
- **文件上传**: python-multipart 0.0.6
- **数据库**: SQLite 3
- **Python版本**: 3.8+

## 项目结构

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
│   ├── todos.db           # SQLite数据库文件
│   └── README.md          # 后端说明文档
├── frontend/              # 前端目录
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── TodoApp.jsx
│   │   │   ├── TodoForm.jsx
│   │   │   ├── TodoList.jsx
│   │   │   └── TodoItem.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── styles/
│   │   │   └── App.css
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── README.md          # 前端说明文档
└── req.md                 # 需求文档
```

## 数据库设计

### 表结构设计

#### todos表
```sql
CREATE TABLE todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 创建索引提升查询性能
CREATE INDEX idx_todos_completed ON todos(completed);
CREATE INDEX idx_todos_created_at ON todos(created_at);
```

### 字段说明
- `id`: 主键，自增整数
- `title`: 待办事项标题，必填，最大255字符
- `description`: 待办事项描述，可选
- `completed`: 完成状态，布尔值，默认false
- `created_at`: 创建时间，自动生成
- `updated_at`: 更新时间，自动更新

## API接口规范

### 基础信息
- **Base URL**: `http://localhost:8000`
- **Content-Type**: `application/json`
- **响应格式**: JSON

### 接口列表

#### 1. 获取所有待办事项
```http
GET /api/todos
```

**查询参数**:
- `status` (可选): `all` | `completed` | `pending` - 筛选条件

**响应示例**:
```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "title": "学习React",
            "description": "完成React基础教程",
            "completed": false,
            "created_at": "2025-09-16T10:00:00Z",
            "updated_at": "2025-09-16T10:00:00Z"
        }
    ],
    "total": 1
}
```

#### 2. 创建待办事项
```http
POST /api/todos
```

**请求体**:
```json
{
    "title": "新的待办事项",
    "description": "描述信息（可选）"
}
```

**响应示例**:
```json
{
    "success": true,
    "data": {
        "id": 2,
        "title": "新的待办事项",
        "description": "描述信息",
        "completed": false,
        "created_at": "2025-09-16T11:00:00Z",
        "updated_at": "2025-09-16T11:00:00Z"
    },
    "message": "待办事项创建成功"
}
```

#### 3. 更新待办事项
```http
PUT /api/todos/{todo_id}
```

**路径参数**:
- `todo_id`: 待办事项ID

**请求体**:
```json
{
    "title": "更新的标题",
    "description": "更新的描述",
    "completed": true
}
```

**响应示例**:
```json
{
    "success": true,
    "data": {
        "id": 1,
        "title": "更新的标题",
        "description": "更新的描述",
        "completed": true,
        "created_at": "2025-09-16T10:00:00Z",
        "updated_at": "2025-09-16T12:00:00Z"
    },
    "message": "待办事项更新成功"
}
```

#### 4. 删除待办事项
```http
DELETE /api/todos/{todo_id}
```

**路径参数**:
- `todo_id`: 待办事项ID

**响应示例**:
```json
{
    "success": true,
    "message": "待办事项删除成功"
}
```

#### 5. 标记完成/未完成
```http
PATCH /api/todos/{todo_id}/toggle
```

**路径参数**:
- `todo_id`: 待办事项ID

**响应示例**:
```json
{
    "success": true,
    "data": {
        "id": 1,
        "title": "学习React",
        "description": "完成React基础教程",
        "completed": true,
        "created_at": "2025-09-16T10:00:00Z",
        "updated_at": "2025-09-16T12:30:00Z"
    },
    "message": "状态切换成功"
}
```

#### 6. 批量删除已完成事项
```http
DELETE /api/todos/completed
```

**响应示例**:
```json
{
    "success": true,
    "message": "已删除 3 个已完成的待办事项",
    "deleted_count": 3
}
```

#### 7. 清空所有待办事项
```http
DELETE /api/todos/all
```

**响应示例**:
```json
{
    "success": true,
    "message": "所有待办事项已清空",
    "deleted_count": 5
}
```

### 错误响应格式
```json
{
    "success": false,
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "输入数据验证失败",
        "details": {
            "title": ["标题不能为空"]
        }
    }
}
```

### HTTP状态码
- `200`: 成功
- `201`: 创建成功
- `400`: 请求参数错误
- `404`: 资源不存在
- `422`: 数据验证失败
- `500`: 服务器内部错误

## 前端架构设计

### 组件结构
```
TodoApp (主容器)
├── TodoForm (添加表单)
├── TodoFilter (筛选组件)
├── TodoList (列表容器)
│   └── TodoItem (列表项)
└── TodoActions (批量操作)
```

### 状态管理
使用React Hooks管理应用状态：
- `todos`: 待办事项列表
- `filter`: 当前筛选条件
- `loading`: 加载状态
- `error`: 错误信息

### 样式设计要求
- **响应式设计**: 支持移动端和桌面端
- **主体居中**: 最大宽度800px
- **现代UI**: 圆角、阴影、渐变等现代元素
- **交互反馈**: hover效果、loading状态、错误提示
- **主题色彩**: 使用统一的色彩方案

## 开发规范

### 代码规范
- **Python**: 遵循PEP8规范
- **JavaScript**: 使用ESLint + Prettier
- **命名约定**: 驼峰命名法(camelCase)、下划线命名法(snake_case)
- **注释**: 关键函数和复杂逻辑需要注释

### Git规范
```
feat: 新功能
fix: 修复bug
docs: 文档更新
style: 代码格式调整
refactor: 代码重构
test: 测试相关
chore: 构建工具等
```

## 部署方案

### 开发环境
- 后端: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
- 前端: `npm run dev` (默认端口3000)

### 生产环境
- 后端: Docker容器 + Nginx反向代理
- 前端: 静态文件部署到CDN
- 数据库: SQLite文件持久化存储

## 性能优化

### 前端优化
- 组件懒加载
- 防抖处理用户输入
- 虚拟列表(大量数据时)
- 缓存API响应

### 后端优化
- 数据库索引优化
- 分页查询
- 响应压缩
- API缓存策略

## 安全考虑

### 数据验证
- 前后端双重验证
- SQL注入防护
- XSS攻击防护
- CSRF防护

### API安全
- 请求频率限制
- 输入长度限制
- 错误信息脱敏

## 测试策略

### 后端测试
- 单元测试: pytest
- API测试: FastAPI TestClient
- 数据库测试: SQLite内存数据库

### 前端测试
- 单元测试: Jest + React Testing Library
- 端到端测试: Cypress
- 组件测试: Storybook

## 监控与日志

### 日志记录
- API访问日志
- 错误日志
- 性能监控日志

### 监控指标
- 响应时间
- 错误率
- 并发用户数
- 数据库查询性能

---

**文档版本**: v1.0  
**创建日期**: 2025-09-16  
**最后更新**: 2025-09-16

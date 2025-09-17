# 待办事项管理系统 - 后端API

基于FastAPI的待办事项管理系统后端服务，提供RESTful API接口，支持待办事项的增删改查、状态管理和筛选功能。

## 🚀 技术栈

- **框架**: FastAPI 0.104.1
- **ASGI服务器**: Uvicorn 0.24.0
- **ORM**: SQLAlchemy 2.0.23
- **数据验证**: Pydantic 2.5.0
- **数据库**: SQLite 3
- **测试框架**: pytest 7.4.3
- **Python版本**: 3.8+

## 📁 项目结构

```
backend/
├── app/
│   ├── __init__.py          # 包初始化文件
│   ├── main.py              # FastAPI应用入口
│   ├── database.py          # 数据库配置
│   ├── models.py            # SQLAlchemy数据模型
│   ├── schemas.py           # Pydantic数据模式
│   ├── crud.py              # 数据库CRUD操作
│   └── api/
│       ├── __init__.py      # API包初始化
│       └── todos.py         # 待办事项API路由
├── requirements.txt         # Python依赖列表
├── test_main.py            # API测试文件
├── todos.db                # SQLite数据库文件(运行后生成)
├── test.db                 # 测试数据库文件(测试时生成)
└── README.md               # 项目说明文档
```

## 🛠 安装和运行

### 1. 环境要求

- Python 3.8 或更高版本
- pip (Python包管理器)

### 2. 安装依赖

```bash
cd backend
pip install -r requirements.txt
```

### 3. 启动开发服务器

```bash
# 启动开发服务器 (支持热重载)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 或者使用Python模块方式启动
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

服务启动后，可以通过以下地址访问：

- **API服务**: http://localhost:8000
- **交互式API文档**: http://localhost:8000/docs
- **ReDoc文档**: http://localhost:8000/redoc

### 4. 生产环境部署

```bash
# 生产环境启动 (无热重载)
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 🗄️ 数据库设计

### todos表结构

| 字段名 | 类型 | 约束 | 说明 |
|--------|------|------|------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | 主键ID |
| title | VARCHAR(255) | NOT NULL | 待办事项标题 |
| description | TEXT | NULL | 待办事项描述 |
| completed | BOOLEAN | DEFAULT FALSE | 完成状态 |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 更新时间 |

### 数据库初始化

数据库表会在应用首次启动时自动创建，无需手动执行SQL脚本。

## 📚 API接口文档

### 基础信息

- **Base URL**: `http://localhost:8000`
- **Content-Type**: `application/json`
- **响应格式**: JSON

### 接口列表

#### 1. 系统接口

##### 根路径
```http
GET /
```
返回API基本信息和版本。

##### 健康检查
```http
GET /health
```
检查API服务状态。

#### 2. 待办事项接口

##### 获取待办事项列表
```http
GET /api/todos?status={status}&skip={skip}&limit={limit}
```

**查询参数**:
- `status` (可选): `all` | `completed` | `pending` - 筛选条件
- `skip` (可选): 跳过的记录数，默认0
- `limit` (可选): 返回记录数限制，默认100，最大1000

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
            "created_at": "2025-09-17T10:00:00Z",
            "updated_at": "2025-09-17T10:00:00Z"
        }
    ],
    "total": 1
}
```

##### 创建待办事项
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

##### 获取单个待办事项
```http
GET /api/todos/{todo_id}
```

##### 更新待办事项
```http
PUT /api/todos/{todo_id}
```

**请求体**:
```json
{
    "title": "更新的标题",
    "description": "更新的描述",
    "completed": true
}
```

##### 切换完成状态
```http
PATCH /api/todos/{todo_id}/toggle
```

##### 删除单个待办事项
```http
DELETE /api/todos/{todo_id}
```

##### 批量删除已完成事项
```http
DELETE /api/todos/completed
```

##### 清空所有待办事项
```http
DELETE /api/todos/all
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

## 🧪 测试

### 运行测试

```bash
# 运行所有测试
python -m pytest test_main.py -v

# 运行特定测试类
python -m pytest test_main.py::TestTodoAPI -v

# 运行特定测试方法
python -m pytest test_main.py::TestTodoAPI::test_create_todo -v

# 生成测试覆盖率报告
python -m pytest test_main.py --cov=app --cov-report=html
```

### 测试覆盖范围

- ✅ 系统基础接口测试
- ✅ 待办事项CRUD操作测试
- ✅ 数据验证测试
- ✅ 错误处理测试
- ✅ 状态筛选测试
- ✅ 批量操作测试

## 🔧 开发指南

### 代码规范

- 遵循PEP8 Python编码规范
- 使用类型提示 (Type Hints)
- 函数和类需要添加文档字符串
- 变量和函数使用下划线命名法 (snake_case)
- 类名使用帕斯卡命名法 (PascalCase)

### 添加新的API端点

1. 在 `app/schemas.py` 中定义请求和响应模式
2. 在 `app/crud.py` 中添加数据库操作函数
3. 在 `app/api/todos.py` 中添加路由处理函数
4. 在 `test_main.py` 中添加相应的测试用例

### 数据库迁移

如需修改数据库结构：

1. 修改 `app/models.py` 中的模型定义
2. 删除现有的 `todos.db` 文件
3. 重启应用，数据库表会自动重新创建

> **注意**: 这会丢失所有现有数据。生产环境建议使用Alembic进行数据库迁移。

## 🔒 安全考虑

### 已实现的安全措施

- **输入验证**: 使用Pydantic进行数据验证
- **CORS配置**: 限制跨域请求来源
- **错误处理**: 统一错误响应格式
- **SQL注入防护**: 使用SQLAlchemy ORM

### 生产环境建议

- 添加API访问频率限制
- 实现用户认证和授权
- 使用HTTPS协议
- 配置日志记录和监控
- 使用环境变量管理配置

## 📊 性能优化

### 数据库优化

- 在 `completed` 和 `created_at` 字段上创建了索引
- 支持分页查询避免一次性加载大量数据
- 使用连接池管理数据库连接

### API优化

- 异步处理请求 (FastAPI原生支持)
- 响应数据压缩
- 合理的错误处理避免不必要的计算

## 🐛 常见问题

### Q: 启动时提示端口被占用
A: 修改启动命令中的端口号，或者关闭占用8000端口的其他进程。

### Q: 数据库文件权限错误
A: 确保应用有权限在当前目录创建和写入文件。

### Q: 测试失败
A: 确保所有依赖已正确安装，并且没有其他进程占用测试数据库。

### Q: CORS错误
A: 检查 `app/main.py` 中的CORS配置，确保前端地址在允许列表中。

## 📝 更新日志

### v1.0.0 (2025-09-17)
- ✨ 初始版本发布
- ✅ 实现完整的待办事项CRUD功能
- ✅ 支持状态筛选和批量操作
- ✅ 完整的API文档和测试覆盖

## 🤝 贡献指南

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 项目Issues: [GitHub Issues](https://github.com/your-repo/issues)
- 邮箱: your-email@example.com

---

**Happy Coding! 🎉**

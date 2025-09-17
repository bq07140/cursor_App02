# 待办事项管理系统 - 前端

基于React + Vite的现代化待办事项管理前端应用，提供直观美观的用户界面和流畅的用户体验。

## 🚀 技术栈

- **框架**: React 18.2.0
- **构建工具**: Vite 5.0.8
- **HTTP客户端**: Axios 1.6.0
- **样式**: CSS3 (现代化响应式设计)
- **开发工具**: ESLint + React插件

## 📁 项目结构

```
frontend/
├── public/
│   ├── vite.svg             # Vite图标
│   └── index.html           # HTML模板
├── src/
│   ├── components/          # React组件
│   │   ├── TodoApp.jsx      # 主应用组件
│   │   ├── TodoForm.jsx     # 添加表单组件
│   │   ├── TodoList.jsx     # 列表容器组件
│   │   ├── TodoItem.jsx     # 列表项组件
│   │   ├── TodoFilter.jsx   # 筛选组件
│   │   └── TodoActions.jsx  # 批量操作组件
│   ├── services/
│   │   └── api.js           # API服务封装
│   ├── styles/
│   │   ├── index.css        # 全局样式和CSS变量
│   │   └── App.css          # 应用主要样式
│   ├── App.jsx              # 根组件
│   └── main.jsx             # 应用入口
├── package.json             # 项目配置和依赖
├── vite.config.js           # Vite配置
└── README.md                # 项目说明文档
```

## 🛠 安装和运行

### 1. 环境要求

- Node.js 16.0 或更高版本
- npm 或 yarn 包管理器

### 2. 安装依赖

```bash
cd frontend
npm install
```

### 3. 启动开发服务器

```bash
# 启动开发服务器 (支持热重载)
npm run dev

# 应用将在 http://localhost:3000 启动
```

### 4. 构建生产版本

```bash
# 构建生产版本
npm run build

# 预览生产版本
npm run preview
```

### 5. 代码检查

```bash
# 运行ESLint检查
npm run lint
```

## 🎨 功能特性

### 核心功能

- ✅ **添加待办事项** - 支持标题和描述
- ✅ **查看待办列表** - 美观的卡片式布局
- ✅ **标记完成** - 一键切换完成状态
- ✅ **删除事项** - 单个删除功能
- ✅ **筛选显示** - 全部/未完成/已完成筛选
- ✅ **批量操作** - 清除已完成/清除全部
- ✅ **进度显示** - 可视化进度条和统计信息

### 用户体验

- 🎯 **响应式设计** - 完美适配移动端和桌面端
- 🎨 **现代UI设计** - 渐变背景、圆角、阴影等现代元素
- ⚡ **流畅动画** - hover效果、过渡动画、加载状态
- 🔔 **错误提示** - 友好的错误信息展示
- 📊 **实时统计** - 动态显示完成进度和数量统计

### 交互设计

- **直观操作** - 点击切换状态，悬停显示操作提示
- **键盘支持** - 表单提交支持回车键
- **确认对话框** - 重要操作前的确认提示
- **加载状态** - API请求时的加载指示器
- **空状态** - 无数据时的友好提示

## 🌐 API集成

### 后端接口

前端通过Axios与后端FastAPI服务通信，支持以下接口：

- `GET /api/todos` - 获取待办事项列表
- `POST /api/todos` - 创建新的待办事项
- `PUT /api/todos/{id}` - 更新待办事项
- `PATCH /api/todos/{id}/toggle` - 切换完成状态
- `DELETE /api/todos/{id}` - 删除单个待办事项
- `DELETE /api/todos/completed` - 批量删除已完成
- `DELETE /api/todos/all` - 清空所有待办事项

### 错误处理

- 网络请求错误自动重试
- 统一的错误信息展示
- 用户友好的错误提示
- 请求和响应日志记录

## 🎨 样式设计

### 设计系统

使用CSS自定义属性实现统一的设计系统：

```css
:root {
  /* 主题色彩 */
  --primary-color: #3b82f6;
  --success-color: #10b981;
  --danger-color: #ef4444;
  
  /* 间距系统 */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  
  /* 阴影效果 */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
}
```

### 响应式断点

- **桌面端** (>768px): 完整布局，最大宽度800px
- **平板端** (≤768px): 调整间距和布局
- **移动端** (≤480px): 垂直布局，优化触控体验

### 视觉特色

- **渐变背景** - 紫蓝色渐变主题
- **卡片设计** - 现代化卡片式布局
- **微交互** - 细致的hover和focus状态
- **进度可视化** - 彩色进度条和统计图表

## 🔧 配置说明

### Vite配置

```javascript
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})
```

### API配置

```javascript
const api = axios.create({
  baseURL: 'http://localhost:8000',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})
```

## 🚀 部署指南

### 开发环境

1. 确保后端服务运行在 http://localhost:8000
2. 启动前端开发服务器: `npm run dev`
3. 访问 http://localhost:3000

### 生产环境

1. 构建生产版本: `npm run build`
2. 部署 `dist` 目录到静态文件服务器
3. 配置反向代理将 `/api` 请求转发到后端服务

### Docker部署

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "preview"]
```

## 🔍 开发指南

### 组件开发规范

1. **函数式组件** - 使用React Hooks
2. **Props验证** - 添加适当的类型检查
3. **样式隔离** - 使用CSS类名约定
4. **可复用性** - 抽象通用组件逻辑

### 状态管理

使用React内置的useState和useEffect管理应用状态：

```javascript
const [todos, setTodos] = useState([])
const [filter, setFilter] = useState('all')
const [loading, setLoading] = useState(false)
const [error, setError] = useState(null)
```

### API调用模式

```javascript
const fetchTodos = async (status = 'all') => {
  try {
    setLoading(true)
    setError(null)
    const data = await todoAPI.getTodos(status)
    setTodos(data.data)
  } catch (err) {
    setError('获取待办事项失败')
    console.error('获取待办事项失败:', err)
  } finally {
    setLoading(false)
  }
}
```

## 🐛 常见问题

### Q: 前端无法连接到后端API
A: 检查后端服务是否运行在8000端口，确认CORS配置正确。

### Q: 样式没有生效
A: 确认CSS文件正确导入，检查浏览器开发者工具中的样式加载情况。

### Q: 热重载不工作
A: 重启开发服务器，检查文件监听权限。

### Q: 构建失败
A: 检查所有依赖是否正确安装，运行 `npm ci` 重新安装依赖。

## 📈 性能优化

### 已实现的优化

- **组件懒加载** - 按需加载组件
- **防抖处理** - 用户输入防抖
- **缓存策略** - API响应缓存
- **代码分割** - Vite自动代码分割

### 进一步优化建议

- 实现虚拟滚动(大量数据时)
- 添加Service Worker缓存
- 使用React.memo优化重渲染
- 图片懒加载和压缩

## 📝 更新日志

### v1.0.0 (2025-09-17)
- ✨ 初始版本发布
- ✅ 完整的待办事项管理功能
- 🎨 现代化响应式UI设计
- 🔧 完善的错误处理和用户体验
- 📚 完整的文档和部署指南

## 🤝 贡献指南

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](../LICENSE) 文件了解详情。

---

**Happy Coding! 🎉**

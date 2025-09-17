import axios from 'axios'

// 创建axios实例
const api = axios.create({
  baseURL: 'http://localhost:8000',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    console.log('API请求:', config.method?.toUpperCase(), config.url)
    return config
  },
  (error) => {
    console.error('请求错误:', error)
    return Promise.reject(error)
  }
)

// 响应拦截器
api.interceptors.response.use(
  (response) => {
    console.log('API响应:', response.status, response.config.url)
    return response.data
  },
  (error) => {
    console.error('响应错误:', error.response?.status, error.response?.data || error.message)
    
    // 统一错误处理
    const errorMessage = error.response?.data?.error?.message || 
                        error.response?.data?.detail || 
                        error.message || 
                        '网络请求失败'
    
    return Promise.reject(new Error(errorMessage))
  }
)

// 待办事项API
export const todoAPI = {
  // 获取待办事项列表
  getTodos: async (status = 'all', skip = 0, limit = 100) => {
    const params = { skip, limit }
    if (status && status !== 'all') {
      params.status = status
    }
    return await api.get('/api/todos', { params })
  },

  // 创建待办事项
  createTodo: async (todo) => {
    return await api.post('/api/todos', todo)
  },

  // 获取单个待办事项
  getTodo: async (id) => {
    return await api.get(`/api/todos/${id}`)
  },

  // 更新待办事项
  updateTodo: async (id, todo) => {
    return await api.put(`/api/todos/${id}`, todo)
  },

  // 切换完成状态
  toggleTodo: async (id) => {
    return await api.patch(`/api/todos/${id}/toggle`)
  },

  // 删除待办事项
  deleteTodo: async (id) => {
    return await api.delete(`/api/todos/${id}`)
  },

  // 批量删除已完成的待办事项
  deleteCompleted: async () => {
    return await api.delete('/api/todos/completed')
  },

  // 清空所有待办事项
  deleteAll: async () => {
    return await api.delete('/api/todos/all')
  },
}

// 系统API
export const systemAPI = {
  // 健康检查
  healthCheck: async () => {
    return await api.get('/health')
  },

  // 获取系统信息
  getSystemInfo: async () => {
    return await api.get('/')
  },
}

export default api

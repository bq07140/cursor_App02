import React, { useState, useEffect } from 'react'
import TodoForm from './components/TodoForm'
import TodoList from './components/TodoList'
import TodoFilter from './components/TodoFilter'
import TodoActions from './components/TodoActions'
import { todoAPI } from './services/api'
import './styles/App.css'

function App() {
  const [todos, setTodos] = useState([])
  const [filter, setFilter] = useState('all')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  // 获取待办事项列表
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

  // 添加待办事项
  const addTodo = async (title, description) => {
    try {
      setError(null)
      const data = await todoAPI.createTodo({ title, description })
      setTodos(prev => [data.data, ...prev])
    } catch (err) {
      setError('添加待办事项失败')
      console.error('添加待办事项失败:', err)
    }
  }

  // 切换完成状态
  const toggleTodo = async (id) => {
    try {
      setError(null)
      const data = await todoAPI.toggleTodo(id)
      setTodos(prev => prev.map(todo => 
        todo.id === id ? data.data : todo
      ))
    } catch (err) {
      setError('更新待办事项失败')
      console.error('更新待办事项失败:', err)
    }
  }

  // 删除待办事项
  const deleteTodo = async (id) => {
    try {
      setError(null)
      await todoAPI.deleteTodo(id)
      setTodos(prev => prev.filter(todo => todo.id !== id))
    } catch (err) {
      setError('删除待办事项失败')
      console.error('删除待办事项失败:', err)
    }
  }

  // 清除已完成的待办事项
  const clearCompleted = async () => {
    try {
      setError(null)
      await todoAPI.deleteCompleted()
      setTodos(prev => prev.filter(todo => !todo.completed))
    } catch (err) {
      setError('清除已完成事项失败')
      console.error('清除已完成事项失败:', err)
    }
  }

  // 清除所有待办事项
  const clearAll = async () => {
    if (window.confirm('确定要清除所有待办事项吗？')) {
      try {
        setError(null)
        await todoAPI.deleteAll()
        setTodos([])
      } catch (err) {
        setError('清除所有事项失败')
        console.error('清除所有事项失败:', err)
      }
    }
  }

  // 筛选待办事项
  const filteredTodos = todos.filter(todo => {
    if (filter === 'completed') return todo.completed
    if (filter === 'pending') return !todo.completed
    return true
  })

  // 统计信息
  const stats = {
    total: todos.length,
    completed: todos.filter(todo => todo.completed).length,
    pending: todos.filter(todo => !todo.completed).length
  }

  // 初始加载
  useEffect(() => {
    fetchTodos()
  }, [])

  // 筛选变化时重新获取数据
  useEffect(() => {
    fetchTodos(filter)
  }, [filter])

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1>待办事项管理</h1>
          <p>高效管理您的日常任务</p>
        </header>

        {error && (
          <div className="error-message">
            {error}
            <button onClick={() => setError(null)}>×</button>
          </div>
        )}

        <main className="main">
          <TodoForm onAddTodo={addTodo} />
          
          <div className="todos-section">
            <div className="todos-header">
              <TodoFilter 
                filter={filter} 
                onFilterChange={setFilter}
                stats={stats}
              />
            </div>

            {loading ? (
              <div className="loading">加载中...</div>
            ) : (
              <TodoList 
                todos={filteredTodos}
                onToggle={toggleTodo}
                onDelete={deleteTodo}
              />
            )}

            {todos.length > 0 && (
              <TodoActions 
                onClearCompleted={clearCompleted}
                onClearAll={clearAll}
                stats={stats}
              />
            )}
          </div>
        </main>

        <footer className="footer">
          <p>&copy; 2025 待办事项管理系统</p>
        </footer>
      </div>
    </div>
  )
}

export default App

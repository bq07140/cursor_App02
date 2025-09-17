import React from 'react'

function TodoItem({ todo, onToggle, onDelete }) {
  const formatDate = (dateString) => {
    const date = new Date(dateString)
    return date.toLocaleDateString('zh-CN', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  return (
    <li className={`todo-item ${todo.completed ? 'completed' : ''}`}>
      <div className="todo-content">
        <div className="todo-main">
          <button
            className={`toggle-btn ${todo.completed ? 'completed' : ''}`}
            onClick={() => onToggle(todo.id)}
            title={todo.completed ? '标记为未完成' : '标记为完成'}
          >
            {todo.completed ? '✓' : '○'}
          </button>
          
          <div className="todo-text">
            <h3 className="todo-title">{todo.title}</h3>
            {todo.description && (
              <p className="todo-description">{todo.description}</p>
            )}
            <div className="todo-meta">
              <span className="todo-date">
                创建于 {formatDate(todo.created_at)}
              </span>
              {todo.completed && (
                <span className="completed-badge">已完成</span>
              )}
            </div>
          </div>
        </div>
        
        <div className="todo-actions">
          <button
            className="delete-btn"
            onClick={() => onDelete(todo.id)}
            title="删除待办事项"
          >
            🗑️
          </button>
        </div>
      </div>
    </li>
  )
}

export default TodoItem

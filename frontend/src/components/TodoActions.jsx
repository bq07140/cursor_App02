import React from 'react'

function TodoActions({ onClearCompleted, onClearAll, stats }) {
  return (
    <div className="todo-actions">
      <div className="actions-left">
        <span className="progress-text">
          进度: {stats.total > 0 ? Math.round((stats.completed / stats.total) * 100) : 0}%
        </span>
        <div className="progress-bar">
          <div 
            className="progress-fill"
            style={{ 
              width: `${stats.total > 0 ? (stats.completed / stats.total) * 100 : 0}%` 
            }}
          />
        </div>
      </div>
      
      <div className="actions-right">
        {stats.completed > 0 && (
          <button 
            className="action-btn secondary"
            onClick={onClearCompleted}
          >
            清除已完成 ({stats.completed})
          </button>
        )}
        
        {stats.total > 0 && (
          <button 
            className="action-btn danger"
            onClick={onClearAll}
          >
            清除全部
          </button>
        )}
      </div>
    </div>
  )
}

export default TodoActions

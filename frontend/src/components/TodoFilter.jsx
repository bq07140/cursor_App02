import React from 'react'

function TodoFilter({ filter, onFilterChange, stats }) {
  const filters = [
    { key: 'all', label: '全部', count: stats.total },
    { key: 'pending', label: '未完成', count: stats.pending },
    { key: 'completed', label: '已完成', count: stats.completed }
  ]

  return (
    <div className="todo-filter">
      <div className="filter-tabs">
        {filters.map(({ key, label, count }) => (
          <button
            key={key}
            className={`filter-tab ${filter === key ? 'active' : ''}`}
            onClick={() => onFilterChange(key)}
          >
            {label}
            <span className="count">({count})</span>
          </button>
        ))}
      </div>
      
      <div className="stats-summary">
        <span className="stats-text">
          共 {stats.total} 项，已完成 {stats.completed} 项
        </span>
      </div>
    </div>
  )
}

export default TodoFilter

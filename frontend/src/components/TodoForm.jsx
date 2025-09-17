import React, { useState } from 'react'

function TodoForm({ onAddTodo }) {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    
    if (!title.trim()) {
      alert('请输入待办事项标题')
      return
    }

    onAddTodo(title.trim(), description.trim())
    setTitle('')
    setDescription('')
  }

  return (
    <form className="todo-form" onSubmit={handleSubmit}>
      <div className="form-group">
        <input
          type="text"
          placeholder="输入新的待办事项..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="todo-input"
          maxLength={255}
        />
        <button type="submit" className="add-btn">
          添加
        </button>
      </div>
      <div className="form-group">
        <textarea
          placeholder="描述 (可选)"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="todo-description"
          rows={2}
          maxLength={500}
        />
      </div>
    </form>
  )
}

export default TodoForm

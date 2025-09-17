from sqlalchemy.orm import Session
from sqlalchemy import desc
from . import models, schemas
from typing import List, Optional

def get_todos(
    db: Session, 
    status: Optional[str] = None,
    skip: int = 0, 
    limit: int = 100
) -> List[models.Todo]:
    """获取待办事项列表"""
    query = db.query(models.Todo)
    
    # 根据状态筛选
    if status == "completed":
        query = query.filter(models.Todo.completed == True)
    elif status == "pending":
        query = query.filter(models.Todo.completed == False)
    # status == "all" 或 None 时不添加筛选条件
    
    return query.order_by(desc(models.Todo.created_at)).offset(skip).limit(limit).all()

def get_todos_count(db: Session, status: Optional[str] = None) -> int:
    """获取待办事项总数"""
    query = db.query(models.Todo)
    
    if status == "completed":
        query = query.filter(models.Todo.completed == True)
    elif status == "pending":
        query = query.filter(models.Todo.completed == False)
    
    return query.count()

def get_todo(db: Session, todo_id: int) -> Optional[models.Todo]:
    """根据ID获取单个待办事项"""
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def create_todo(db: Session, todo: schemas.TodoCreate) -> models.Todo:
    """创建新的待办事项"""
    db_todo = models.Todo(
        title=todo.title,
        description=todo.description,
        completed=False
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo_update: schemas.TodoUpdate) -> Optional[models.Todo]:
    """更新待办事项"""
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None
    
    # 只更新提供的字段
    update_data = todo_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)
    
    db.commit()
    db.refresh(db_todo)
    return db_todo

def toggle_todo(db: Session, todo_id: int) -> Optional[models.Todo]:
    """切换待办事项完成状态"""
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None
    
    db_todo.completed = not db_todo.completed
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int) -> bool:
    """删除单个待办事项"""
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return False
    
    db.delete(db_todo)
    db.commit()
    return True

def delete_completed_todos(db: Session) -> int:
    """删除所有已完成的待办事项"""
    deleted_count = db.query(models.Todo).filter(models.Todo.completed == True).count()
    db.query(models.Todo).filter(models.Todo.completed == True).delete()
    db.commit()
    return deleted_count

def delete_all_todos(db: Session) -> int:
    """删除所有待办事项"""
    deleted_count = db.query(models.Todo).count()
    db.query(models.Todo).delete()
    db.commit()
    return deleted_count

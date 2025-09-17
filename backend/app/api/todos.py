from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/todos", tags=["todos"])

@router.get("/", response_model=schemas.TodoListResponse)
async def get_todos(
    status: Optional[str] = Query(None, pattern="^(all|completed|pending)$", description="筛选条件: all, completed, pending"),
    skip: int = Query(0, ge=0, description="跳过的记录数"),
    limit: int = Query(100, ge=1, le=1000, description="返回的记录数限制"),
    db: Session = Depends(get_db)
):
    """获取待办事项列表"""
    try:
        todos = crud.get_todos(db, status=status, skip=skip, limit=limit)
        total = crud.get_todos_count(db, status=status)
        
        return schemas.TodoListResponse(
            success=True,
            data=todos,
            total=total
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取待办事项失败: {str(e)}")

@router.post("/", response_model=schemas.SingleTodoResponse, status_code=201)
async def create_todo(
    todo: schemas.TodoCreate,
    db: Session = Depends(get_db)
):
    """创建新的待办事项"""
    try:
        db_todo = crud.create_todo(db=db, todo=todo)
        return schemas.SingleTodoResponse(
            success=True,
            data=db_todo,
            message="待办事项创建成功"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建待办事项失败: {str(e)}")

@router.get("/{todo_id}", response_model=schemas.SingleTodoResponse)
async def get_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    """获取单个待办事项"""
    db_todo = crud.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="待办事项不存在")
    
    return schemas.SingleTodoResponse(
        success=True,
        data=db_todo
    )

@router.put("/{todo_id}", response_model=schemas.SingleTodoResponse)
async def update_todo(
    todo_id: int,
    todo_update: schemas.TodoUpdate,
    db: Session = Depends(get_db)
):
    """更新待办事项"""
    try:
        db_todo = crud.update_todo(db, todo_id=todo_id, todo_update=todo_update)
        if db_todo is None:
            raise HTTPException(status_code=404, detail="待办事项不存在")
        
        return schemas.SingleTodoResponse(
            success=True,
            data=db_todo,
            message="待办事项更新成功"
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新待办事项失败: {str(e)}")

@router.patch("/{todo_id}/toggle", response_model=schemas.SingleTodoResponse)
async def toggle_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    """切换待办事项完成状态"""
    try:
        db_todo = crud.toggle_todo(db, todo_id=todo_id)
        if db_todo is None:
            raise HTTPException(status_code=404, detail="待办事项不存在")
        
        status_text = "已完成" if db_todo.completed else "未完成"
        return schemas.SingleTodoResponse(
            success=True,
            data=db_todo,
            message=f"状态已切换为{status_text}"
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"切换状态失败: {str(e)}")

@router.delete("/completed", response_model=schemas.DeleteResponse)
async def delete_completed_todos(
    db: Session = Depends(get_db)
):
    """批量删除已完成的待办事项"""
    try:
        deleted_count = crud.delete_completed_todos(db)
        return schemas.DeleteResponse(
            success=True,
            message=f"已删除 {deleted_count} 个已完成的待办事项",
            deleted_count=deleted_count
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除已完成待办事项失败: {str(e)}")

@router.delete("/all", response_model=schemas.DeleteResponse)
async def delete_all_todos(
    db: Session = Depends(get_db)
):
    """清空所有待办事项"""
    try:
        deleted_count = crud.delete_all_todos(db)
        return schemas.DeleteResponse(
            success=True,
            message=f"所有待办事项已清空",
            deleted_count=deleted_count
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"清空待办事项失败: {str(e)}")

@router.delete("/{todo_id}", response_model=schemas.APIResponse)
async def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    """删除单个待办事项"""
    try:
        success = crud.delete_todo(db, todo_id=todo_id)
        if not success:
            raise HTTPException(status_code=404, detail="待办事项不存在")
        
        return schemas.APIResponse(
            success=True,
            message="待办事项删除成功"
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除待办事项失败: {str(e)}")

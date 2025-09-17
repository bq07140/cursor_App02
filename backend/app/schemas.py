from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# 基础Todo模式
class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="待办事项标题")
    description: Optional[str] = Field(None, description="待办事项描述")

# 创建Todo请求模式
class TodoCreate(TodoBase):
    pass

# 更新Todo请求模式
class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255, description="待办事项标题")
    description: Optional[str] = Field(None, description="待办事项描述")
    completed: Optional[bool] = Field(None, description="完成状态")

# Todo响应模式
class TodoResponse(TodoBase):
    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

# API响应模式
class APIResponse(BaseModel):
    success: bool
    message: Optional[str] = None

class TodoListResponse(APIResponse):
    data: List[TodoResponse]
    total: int

class SingleTodoResponse(APIResponse):
    data: TodoResponse

class DeleteResponse(APIResponse):
    deleted_count: Optional[int] = None

# 错误响应模式
class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Optional[dict] = None

class ErrorResponse(BaseModel):
    success: bool = False
    error: ErrorDetail

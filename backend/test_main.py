import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import get_db, Base
from app.models import Todo
import json

# 创建测试数据库
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建测试数据库表
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

class TestTodoAPI:
    """待办事项API测试类"""
    
    def setup_method(self):
        """每个测试方法执行前的设置"""
        # 清空测试数据库
        db = TestingSessionLocal()
        db.query(Todo).delete()
        db.commit()
        db.close()
    
    def test_root_endpoint(self):
        """测试根路径"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        assert "待办事项管理API" in data["message"]
    
    def test_health_check(self):
        """测试健康检查"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        assert data["status"] == "healthy"
    
    def test_create_todo(self):
        """测试创建待办事项"""
        todo_data = {
            "title": "测试待办事项",
            "description": "这是一个测试描述"
        }
        response = client.post("/api/todos/", json=todo_data)
        assert response.status_code == 201
        data = response.json()
        assert data["success"] == True
        assert data["data"]["title"] == todo_data["title"]
        assert data["data"]["description"] == todo_data["description"]
        assert data["data"]["completed"] == False
        assert "id" in data["data"]
    
    def test_create_todo_without_description(self):
        """测试创建不带描述的待办事项"""
        todo_data = {
            "title": "只有标题的待办事项"
        }
        response = client.post("/api/todos/", json=todo_data)
        assert response.status_code == 201
        data = response.json()
        assert data["success"] == True
        assert data["data"]["title"] == todo_data["title"]
        assert data["data"]["description"] is None
    
    def test_create_todo_invalid_data(self):
        """测试创建待办事项时传入无效数据"""
        # 空标题
        response = client.post("/api/todos/", json={"title": ""})
        assert response.status_code == 422
        
        # 缺少标题
        response = client.post("/api/todos/", json={"description": "只有描述"})
        assert response.status_code == 422
    
    def test_get_todos_empty(self):
        """测试获取空的待办事项列表"""
        response = client.get("/api/todos/")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        assert data["data"] == []
        assert data["total"] == 0
    
    def test_get_todos_with_data(self):
        """测试获取有数据的待办事项列表"""
        # 先创建几个待办事项
        todos = [
            {"title": "待办事项1", "description": "描述1"},
            {"title": "待办事项2", "description": "描述2"},
            {"title": "待办事项3"}
        ]
        
        created_todos = []
        for todo in todos:
            response = client.post("/api/todos/", json=todo)
            created_todos.append(response.json()["data"])
        
        # 获取所有待办事项
        response = client.get("/api/todos/")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        assert len(data["data"]) == 3
        assert data["total"] == 3
    
    def test_get_todo_by_id(self):
        """测试根据ID获取待办事项"""
        # 先创建一个待办事项
        todo_data = {"title": "测试获取单个待办事项"}
        create_response = client.post("/api/todos/", json=todo_data)
        created_todo = create_response.json()["data"]
        
        # 根据ID获取
        response = client.get(f"/api/todos/{created_todo['id']}")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        assert data["data"]["id"] == created_todo["id"]
        assert data["data"]["title"] == todo_data["title"]
    
    def test_get_todo_not_found(self):
        """测试获取不存在的待办事项"""
        response = client.get("/api/todos/999")
        assert response.status_code == 404
        data = response.json()
        assert data["success"] == False
    
    def test_update_todo(self):
        """测试更新待办事项"""
        # 先创建一个待办事项
        todo_data = {"title": "原始标题", "description": "原始描述"}
        create_response = client.post("/api/todos/", json=todo_data)
        created_todo = create_response.json()["data"]
        
        # 更新待办事项
        update_data = {
            "title": "更新后的标题",
            "description": "更新后的描述",
            "completed": True
        }
        response = client.put(f"/api/todos/{created_todo['id']}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        assert data["data"]["title"] == update_data["title"]
        assert data["data"]["description"] == update_data["description"]
        assert data["data"]["completed"] == True
    
    def test_update_todo_partial(self):
        """测试部分更新待办事项"""
        # 先创建一个待办事项
        todo_data = {"title": "原始标题", "description": "原始描述"}
        create_response = client.post("/api/todos/", json=todo_data)
        created_todo = create_response.json()["data"]
        
        # 只更新标题
        update_data = {"title": "只更新标题"}
        response = client.put(f"/api/todos/{created_todo['id']}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        assert data["data"]["title"] == update_data["title"]
        assert data["data"]["description"] == todo_data["description"]  # 描述应该保持不变
    
    def test_toggle_todo(self):
        """测试切换待办事项状态"""
        # 先创建一个待办事项
        todo_data = {"title": "测试切换状态"}
        create_response = client.post("/api/todos/", json=todo_data)
        created_todo = create_response.json()["data"]
        assert created_todo["completed"] == False
        
        # 切换为完成状态
        response = client.patch(f"/api/todos/{created_todo['id']}/toggle")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        assert data["data"]["completed"] == True
        
        # 再次切换为未完成状态
        response = client.patch(f"/api/todos/{created_todo['id']}/toggle")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        assert data["data"]["completed"] == False
    
    def test_delete_todo(self):
        """测试删除待办事项"""
        # 先创建一个待办事项
        todo_data = {"title": "要被删除的待办事项"}
        create_response = client.post("/api/todos/", json=todo_data)
        created_todo = create_response.json()["data"]
        
        # 删除待办事项
        response = client.delete(f"/api/todos/{created_todo['id']}")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        
        # 验证已被删除
        response = client.get(f"/api/todos/{created_todo['id']}")
        assert response.status_code == 404
    
    def test_filter_todos_by_status(self):
        """测试按状态筛选待办事项"""
        # 创建几个待办事项，一些完成，一些未完成
        todos = [
            {"title": "未完成1"},
            {"title": "未完成2"},
            {"title": "已完成1"},
            {"title": "已完成2"}
        ]
        
        created_todos = []
        for todo in todos:
            response = client.post("/api/todos/", json=todo)
            created_todos.append(response.json()["data"])
        
        # 将后两个标记为完成
        for i in [2, 3]:
            client.patch(f"/api/todos/{created_todos[i]['id']}/toggle")
        
        # 测试获取所有待办事项
        response = client.get("/api/todos/?status=all")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 4
        
        # 测试获取未完成的待办事项
        response = client.get("/api/todos/?status=pending")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 2
        assert all(not todo["completed"] for todo in data["data"])
        
        # 测试获取已完成的待办事项
        response = client.get("/api/todos/?status=completed")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 2
        assert all(todo["completed"] for todo in data["data"])
    
    def test_delete_completed_todos(self):
        """测试批量删除已完成的待办事项"""
        # 创建几个待办事项
        todos = [
            {"title": "未完成1"},
            {"title": "已完成1"},
            {"title": "已完成2"}
        ]
        
        created_todos = []
        for todo in todos:
            response = client.post("/api/todos/", json=todo)
            created_todos.append(response.json()["data"])
        
        # 将后两个标记为完成
        for i in [1, 2]:
            client.patch(f"/api/todos/{created_todos[i]['id']}/toggle")
        
        # 删除已完成的待办事项
        response = client.delete("/api/todos/completed")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        assert data["deleted_count"] == 2
        
        # 验证只剩下未完成的
        response = client.get("/api/todos/")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 1
        assert not data["data"][0]["completed"]
    
    def test_delete_all_todos(self):
        """测试清空所有待办事项"""
        # 创建几个待办事项
        todos = [
            {"title": "待办事项1"},
            {"title": "待办事项2"},
            {"title": "待办事项3"}
        ]
        
        for todo in todos:
            client.post("/api/todos/", json=todo)
        
        # 清空所有待办事项
        response = client.delete("/api/todos/all")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
        assert data["deleted_count"] == 3
        
        # 验证已清空
        response = client.get("/api/todos/")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 0
        assert data["data"] == []

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

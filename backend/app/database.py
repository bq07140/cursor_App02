from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# 数据库配置
DATABASE_URL = "sqlite:///./todos.db"

# 创建数据库引擎
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False},  # SQLite特定配置
    echo=False  # 设置为True可以看到SQL语句
)

# 创建SessionLocal类
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建Base类
Base = declarative_base()

# 数据库依赖
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

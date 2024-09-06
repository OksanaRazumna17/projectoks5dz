from pydantic import BaseModel
from typing import Optional


# Базовая схема для категории
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


# Схема для создания категории
class CategoryCreate(CategoryBase):
    pass


# Схема для ответа, которая будет содержать ID категории
class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True  # Включает поддержку работы с объектами ORM


# Базовая схема для вопроса
class QuestionBase(BaseModel):
    title: str
    body: str
    category_id: int


# Схема для создания вопроса
class QuestionCreate(QuestionBase):
    pass


# Схема для ответа, которая будет включать категорию
class QuestionResponse(QuestionBase):
    id: int
    category: CategoryResponse

    class Config:
        orm_mode = True  # Включает поддержку работы с объектами ORM

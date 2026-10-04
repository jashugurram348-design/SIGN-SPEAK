# models.py

from dataclasses import dataclass
from typing import Optional


# =========================================================
# SIGN MODEL
# =========================================================

@dataclass
class Sign:
    id: Optional[int] = None
    name: str = ""
    category: str = ""
    description: str = ""
    image: str = ""
    created_at: Optional[str] = None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "image": self.image,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            name=data.get("name", ""),
            category=data.get("category", ""),
            description=data.get("description", ""),
            image=data.get("image", ""),
            created_at=data.get("created_at")
        )


# =========================================================
# TRANSLATION HISTORY MODEL
# =========================================================

@dataclass
class TranslationHistory:
    id: Optional[int] = None
    input_text: str = ""
    translated_text: str = ""
    created_at: Optional[str] = None

    def to_dict(self):
        return {
            "id": self.id,
            "input_text": self.input_text,
            "translated_text": self.translated_text,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            input_text=data.get("input_text", ""),
            translated_text=data.get("translated_text", ""),
            created_at=data.get("created_at")
        )


# =========================================================
# LEARNING PROGRESS MODEL
# =========================================================

@dataclass
class LearningProgress:
    id: Optional[int] = None
    lesson_name: str = ""
    completed: bool = False
    completed_at: Optional[str] = None

    def to_dict(self):
        return {
            "id": self.id,
            "lesson_name": self.lesson_name,
            "completed": self.completed,
            "completed_at": self.completed_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            lesson_name=data.get("lesson_name", ""),
            completed=bool(data.get("completed", False)),
            completed_at=data.get("completed_at")
        )


# =========================================================
# API RESPONSE MODEL
# =========================================================

@dataclass
class APIResponse:
    success: bool
    message: str = ""
    data: Optional[object] = None

    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data
        }
from enum import Enum

from pydantic import BaseModel, Field, field_validator


class Label(str, Enum):
    HATE = "Hate"
    SAFE = "Safe"


class HateAnalysis(BaseModel):
    label: Label = Field(..., description="Either 'Hate' or 'Safe'")
    confidence: float = Field(..., description="Confidence score between 0 and 1")
    reason: str = Field(..., description="Brief explanation of the classification")

    @field_validator("label", mode="before")
    @classmethod
    def validate_label(cls, v):
        if isinstance(v, str):
            v = v.strip().capitalize()
        return v

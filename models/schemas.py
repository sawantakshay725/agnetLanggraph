from pydantic import BaseModel

class DemandRequest(BaseModel):
    product_id: int
    period: str

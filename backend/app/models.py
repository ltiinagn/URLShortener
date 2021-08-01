from pydantic import BaseModel

class URLData(BaseModel):
	url: str
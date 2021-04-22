from pydantic import BaseModel

class AudioDB(BaseModel):
    audioFileType: str
    audioFileMetadata: dict
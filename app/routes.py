from fastapi import APIRouter
from pydantic import BaseModel
from .services.rotate_service import rotateImages

router = APIRouter()
class RotateRequest(BaseModel):
    folder_path: str
    size: str | None = None  # or Optional[str]

@router.post("/api/rotate")
async def rotate_images(request: RotateRequest):
    print(f"Received request to rotate images in folder: {request.folder_path} with size: {request.size}")
    size = tuple(map(int, request.size.split('x'))) if request.size else None
    if not request or not request.folder_path:
        return {"error": "Input folder is required"}
    result_path = await rotateImages(request.folder_path, size)
    return {"message": "Images processed", "output_path": result_path}

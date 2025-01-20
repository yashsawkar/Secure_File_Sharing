from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import File, User
from app.schemas import FileOut

router = APIRouter()

@router.post("/upload-file", response_model=FileOut)
def upload_file(
    file: UploadFile = File(...), current_user=Depends(get_current_user), db: Session = Depends(get_db)
):
    if current_user.role != "ops_user":
        raise HTTPException(status_code=403, detail="Not authorized to upload files")
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.presentationml.presentation", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    db_file = File(filename=file.filename, owner_id=current_user.id)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file
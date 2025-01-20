from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, File
from app.utils.encryption import generate_encrypted_url

router = APIRouter()

@router.get("/list-files")
def list_files(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.role != "client_user":
        raise HTTPException(status_code=403, detail="Not authorized to list files")
    return db.query(File).all()

@router.get("/download-file/{file_id}")
def download_file(file_id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    file = db.query(File).filter(File.id == file_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    if current_user.role != "client_user":
        raise HTTPException(status_code=403, detail="Not authorized to download this file")
    return {"download-link": generate_encrypted_url(file_id), "message": "success"}
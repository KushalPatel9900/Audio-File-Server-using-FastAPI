from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/")
def Add_audio_file(request: schemas.AudioDB, db : Session = Depends(get_db)):

    if request.audioFileType == "Song":
        new_audio = models.Song(Name=request.audioFileMetadata["Name"], Duration = request.audioFileMetadata["Duration"])
        db.add(new_audio)
        db.commit()
        db.refresh(new_audio)
        return new_audio

    elif request.audioFileType == "Podcast":
        new_audio = models.Podcast(Name=request.audioFileMetadata["Name"], 
                                   Duration = request.audioFileMetadata["Duration"],
                                   Host = request.audioFileMetadata["Host"],
                                   Participants = request.audioFileMetadata["Participants"])
        db.add(new_audio)
        db.commit()
        db.refresh(new_audio)
        return new_audio

    elif request.audioFileType == "Audiobook":
        new_audio = models.AudioBook(Title=request.audioFileMetadata["Title"], 
                                    Author = request.audioFileMetadata["Author"],
                                    Narrator = request.audioFileMetadata["Narrator"],
                                    Duration=request.audioFileMetadata["Duration"])
        db.add(new_audio)
        db.commit()
        db.refresh(new_audio)
        return new_audio

@app.get('/{audioFileType}')
def get_all_audio(audioFileType, db: Session = Depends(get_db)):
    audio = None
    if audioFileType == "Song":
        audio = db.query(models.Song).all()
        
    
    elif audioFileType == "Podcast":
        audio = db.query(models.Podcast).all()
        
    
    elif audioFileType == "Audiobook":
        audio = db.query(models.AudioBook).all()
        
    if not (audioFileType=="Song" or audioFileType=="Podcast" or audioFileType=="Audiobook"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No such audioFileType found!")
    
    return audio

@app.get('/{audioFileType}/{audioFileID}')
def get_by_id(audioFileType,audioFileID, db: Session = Depends(get_db)):
    audio = None
    if audioFileType == "Song":
        audio = db.query(models.Song).filter(models.Song.ID == audioFileID).first()
        
    
    elif audioFileType == "Podcast":
        audio = db.query(models.Podcast).filter(models.Podcast.ID == audioFileID).first()
        
    
    elif audioFileType == "Audiobook":
        audio = db.query(models.AudioBook).filter(models.AudioBook.ID == audioFileID).first()
    
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No such audioFileType found!")
    if not audio:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No such entry found!")
    
    return audio
    
@app.delete('/{audioFileType}/{audioFileID}')
def delete_by_ID(audioFileType, audioFileID, db: Session = Depends(get_db)):
    if audioFileType == "Song":
        audio = db.query(models.Song).filter(models.Song.ID == audioFileID).delete(synchronize_session=False)
        

    elif audioFileType == "Podcast":
        audio = db.query(models.Podcast).filter(models.Podcast.ID == audioFileID).delete(synchronize_session=False)
        

    elif audioFileType == "Audiobook":
        audio = db.query(models.AudioBook).filter(models.AudioBook.ID == audioFileID).delete(synchronize_session=False)

    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No such audioFileType found!")

    if audio==0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No such entry found!")

    db.commit() #Commiting to the Database
    return {"detail": f"{audioFileType} with audioFileID-{audioFileID} deleted!"}
        
@app.put("/{audioFileType}/{audioFileID}")
def update_by_id(audioFileType, audioFileID, request: schemas.AudioDB, db : Session = Depends(get_db)):
    if audioFileType == "Song":
        audio = db.query(models.Song).filter(models.Song.ID == audioFileID).update({"Name": request.audioFileMetadata["Name"], 
                                                                            "Duration": request.audioFileMetadata["Duration"]}, 
                                                                            synchronize_session=False)

    elif audioFileType == "Podcast":
        audio = db.query(models.Podcast).filter(models.Podcast.ID == audioFileID).update({"Name": request.audioFileMetadata["Name"], 
                                                                            "Duration": request.audioFileMetadata["Duration"],
                                                                            "Host": request.audioFileMetadata["Host"],
                                                                            "Participants" : request.audioFileMetadata["Participants"]}, 
                                                                            synchronize_session=False)

    elif audioFileType == "Audiobook":
        audio = db.query(models.AudioBook).filter(models.AudioBook.ID == audioFileID).update({"Title": request.audioFileMetadata["Title"], 
                                                                            "Author": request.audioFileMetadata["Author"],
                                                                            "Narrator": request.audioFileMetadata["Narrator"],
                                                                            "Duration" : request.audioFileMetadata["Duration"]}, 
                                                                            synchronize_session=False)

    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No such audioFileType found!")

    if audio==0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No such entry found!")

    db.commit() #Commiting to the Database
    return {"detail": f"{audioFileType} with audioFileID-{audioFileID} updated!"}
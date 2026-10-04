from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:


    @staticmethod
    def create_user(user_valid_data, db: Session ):
        try:
            db.add(user_valid_data)
            db.commit()
            db.refresh(user_valid_data)
            return {'message': 'successfully inserted data'}

        except  Exception as ex:
            return {'error': str(ex)}


    @staticmethod
    def _validate_is_duplicate_email(email, db: Session):
        return db.query(User).filter(User.email == email).first()



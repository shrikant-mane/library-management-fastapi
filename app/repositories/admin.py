from sqlalchemy.orm import Session
from app.models.admin import Admin
from app.schemas.admin import CreateAdmin
from app.models.admin import Admin


class AdminRepository:

    @staticmethod
    def get_all_admin(db: Session ):
        admin_list = db.query(Admin).all()
        return admin_list


    @staticmethod
    def get_admin_by_id(admin_id: int, db: Session):
        admin_data = db.query(Admin).filter(admin_id==Admin.id).first()
        return admin_data


    @staticmethod
    def create_admin(admin_data, db: Session ):
        try:
            db.add(admin_data)
            db.commit()
            db.refresh(admin_data)
            return {'message': 'successfully inserted data'}

        except Exception as ex:
            return {'error': str(ex)}


    @staticmethod
    def update_admin_email(admin_id, admin_email, db: Session):
        try:
            admin = db.query(Admin).filter(admin_id==Admin.id).first()
            if not admin:
                return None
            admin.email = admin_email
            db.add(admin)
            db.commit()
            db.refresh(admin)
            return admin
        except Exception as ex:
            raise ex


    @staticmethod
    def delete_admin(admin_id: int, db:Session):
        admin = db.query(Admin).filter(admin_id==Admin.id).first()
        if not admin:
            return None
        db.delete(admin)
        db.commit()
        return admin



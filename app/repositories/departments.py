# contain database interaction
from sqlalchemy.orm import Session
from app.models.departments import Department
from app.schemas.departments import CreateDepartment

class Department_Repository:
    @staticmethod
    def get_all_department(db: Session ):
        department_list = db.query(Department).all()
        return department_list


    @staticmethod
    def get_department(department_id: int, db: Session):
        department_data = db.query(Department).filter(Department.id == department_id).first()
        return department_data


    @staticmethod
    def create_department(department_data : CreateDepartment , db : Session):
        try:
            department = Department(
                id=department_data.id,
                name=department_data.name,
                email=department_data.email,
                head_of_department=department_data.head_of_department
            )
            db.add(department)
            db.commit()
            db.refresh(department)
            return {'message': 'successfully inserted data'}
        except Exception as ex:
            return {'error': str(ex)}


    @staticmethod
    def update_department_email(department_id: int, department_email:str, db: Session):
        try:
            department = db.query(Department).filter(Department.id == department_id).first()
            if not department:
                return None
            department.email = department_email
            db.add(department)
            db.commit()
            db.refresh(department)
            return department
        except Exception as ex:
            raise ex


    @staticmethod
    def delete_department(department_id: int, db: Session):
        department = db.query(Department).filter(Department.id == department_id).first()
        if not department:
            return None
        db.delete(department)
        db.commit()
        return department



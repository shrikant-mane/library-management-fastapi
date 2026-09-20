from app.main import app
from fastapi.testclient import TestClient
from app.tests.setup.test_database import override_get_db
from app.core.database import get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# # app = FastAPI()
#
# @app.get('/test_env')
# def test_get_env():
#     try:
#         return {'TEST_DATABASE_URL': settings.TEST_DATABASE_URL}
#     except Exception as ex:
#         raise ex
#
# @app.get('/database')
# def test_database_connection_check(db: Session = Depends(test_get_db)):
#     try:
#         db.execute(text('select 1'))
#         return {'status': 'test database connection successfull'}
#
#     except Exception as ex:
#         return {
#             'status': 'test database connection failed',
#             'error': str(ex)
#         }
#

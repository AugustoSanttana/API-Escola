from sqlalchemy import text
from sqlalchemy.engine import create_engine

engine = create_engine(url="postgresql://postgres:Az1310750412@127.0.0.1:5432/escola", enable_from_linting=False, echo=False)
 
class DatabaseManager:
    
    engine = engine
 
    def _init_(self) -> None:
        pass

    def execute_sql_str(self, sql: str, query=False):
        with self.engine.connect() as conn:
            with conn.begin():
                result = conn.execute(text(sql))
                if query:
                    return result.fetchall()
                return None

    def select_one(self, sql: str):
        with self.engine.begin() as conn:
            result = conn.execute(text(sql))
            return result.fetchone()
    
    def select_all(self, sql: str):
        with self.engine.begin() as conn:
            result = conn.execute(text(sql))
            return result.fetchall()
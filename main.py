from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

date = datetime.today()
print(date)

if __name__ == '__main__':
    calculate_salary()
    get_employees()

from DBcreater import *
from DBmanager import *
from hh import *
from utils import *


parser = HH()
company_id = parser.get_request_company()
vacancies_list_hh = parser.get_request_vacantcies(company_id)
parser.insert_vacancies(vacancies_list_hh)

vacancies_list_hh = load_json_file('vacantes.json')

db_work = DBcreater()
db_work.createDB()
db_work.create_table_hh_companys()
db_work.create_table_hh_vacancies()
db_work.insert_table_hh_company(vacancies_list_hh)
db_work.insert_table_hh_vacancies(vacancies_list_hh)

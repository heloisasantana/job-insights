from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    salaries_list = []
    max_salary = 0
    for row in data:
        if row["max_salary"] and row["max_salary"] != 'invalid':
            salaries_list.append(int(row["max_salary"]))
            max_salary = max(salaries_list)
    return max_salary


def get_min_salary(path: str) -> int:
    data = read(path)
    salaries_list = []
    min_salary = 0
    for row in data:
        if row["min_salary"] and row["min_salary"] != 'invalid':
            salaries_list.append(int(row["min_salary"]))
            min_salary = min(salaries_list)
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if int(job["max_salary"]) < int(job["min_salary"]):
            raise ValueError('max_salary must be bigger than the min_salary')
        if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
            return True
        return False
    except (TypeError, KeyError) as error:
        raise ValueError(error)


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_by_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_by_salary.append(job)
        except ValueError as error:
            print(error)
    return filtered_by_salary

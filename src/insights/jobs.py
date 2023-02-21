import csv

from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        data = csv.DictReader(file)
        jobs_list = []
        for row in data:
            jobs_list.append(row)
    return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    types_list = []
    for row in data:
        if row["job_type"] not in types_list:
            types_list.append(row["job_type"])
    return types_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError

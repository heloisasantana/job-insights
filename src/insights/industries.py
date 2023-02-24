from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    industries_list = []
    for row in data:
        if row["industry"] not in industries_list and row["industry"] != '':
            industries_list.append(row["industry"])
    return industries_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industry_list = []
    for row in jobs:
        if row["industry"] == industry:
            industry_list.append(row)
    return industry_list

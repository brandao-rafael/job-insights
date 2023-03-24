from typing import List, Dict
from src.insights.jobs import read

# from jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    all_jobs = read(path)
    industries = []
    for job in all_jobs:
        if job["industry"] not in industries:
            if job["industry"] != "":
                industries.append(job["industry"])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    job_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            job_by_industry.append(job)
    return job_by_industry

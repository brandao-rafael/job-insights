from typing import Union, List, Dict

from src.insights.jobs import read

# from jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    all_jobs = read(path)
    salary = 0
    for job in all_jobs:
        if job["max_salary"].isdigit():
            if int(job["max_salary"]) > salary:
                salary = int(job["max_salary"])
    return salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    all_jobs = read(path)
    salary = get_max_salary(path)
    for job in all_jobs:
        if job["min_salary"].isdigit():
            if int(job["min_salary"]) < salary:
                salary = int(job["min_salary"])
    return salary


def validate_salary(salary):
    """validate salary"""
    if salary is None or not isinstance(salary, (str, int)):
        raise ValueError("salary must be a number")

    if str(salary).isdigit() and isinstance(salary, str):
        salary = int(salary)

    if int(salary) < 0 or salary < 0:
        return False

    if not str(salary).isdigit():
        raise ValueError("salary must be a number")

    return True


def validate_job(job):
    """validate job"""
    if (
        job.get("min_salary", None) is None
        or job.get("max_salary", None) is None
        or not str(job["min_salary"]).isdigit()
        or not str(job["max_salary"]).isdigit()
        or int(job["min_salary"]) > int(job["max_salary"])
    ):
        raise ValueError("Some fields are invalid")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    if str(salary).isdigit() and isinstance(salary, str):
        salary = int(salary)

    if salary is None:
        raise ValueError("salary must be a number")

    validate_salary(salary)
    validate_job(job)

    if isinstance(salary, int):
        return int(job["min_salary"]) <= salary <= int(job["max_salary"])

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_per_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_per_range.append(job)
        except ValueError:
            pass
    return jobs_per_range

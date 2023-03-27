import pytest
from src.pre_built.sorting import sort_by


@pytest.fixture
def by_max_salary():
    return [
        {"date_posted": "2022-07-20", "max_salary": 56000, "min_salary": 1500},
        {"date_posted": "2022-04-21", "max_salary": 22000, "min_salary": 1000},
        {"date_posted": "2021-12-28", "max_salary": 13000, "min_salary": 1600},
        {"date_posted": "2023-02-20", "max_salary": 6000, "min_salary": 1800},
    ]


@pytest.fixture
def by_min_salary():
    return [
        {"date_posted": "2022-04-21", "max_salary": 22000, "min_salary": 1000},
        {"date_posted": "2022-07-20", "max_salary": 56000, "min_salary": 1500},
        {"date_posted": "2021-12-28", "max_salary": 13000, "min_salary": 1600},
        {"date_posted": "2023-02-20", "max_salary": 6000, "min_salary": 1800},
    ]


@pytest.fixture
def by_date_posted():
    "2022-04-21" "2022-04-22"
    return [
        {
            "date_posted": "2023-02-20",
            "max_salary": 6000,
            "min_salary": 1800,
        },
        {
            "date_posted": "2022-07-20",
            "max_salary": 56000,
            "min_salary": 1500,
        },
        {
            "date_posted": "2022-04-21",
            "max_salary": 22000,
            "min_salary": 1000,
        },
        {
            "date_posted": "2021-12-28",
            "max_salary": 13000,
            "min_salary": 1600,
        },
    ]


def test_sort_by_criteria(by_max_salary, by_min_salary, by_date_posted):
    jobs_to_sort = [
        {"date_posted": "2021-12-28", "max_salary": 13000, "min_salary": 1600},
        {"date_posted": "2022-04-21", "max_salary": 22000, "min_salary": 1000},
        {"date_posted": "2022-07-20", "max_salary": 56000, "min_salary": 1500},
        {"date_posted": "2023-02-20", "max_salary": 6000, "min_salary": 1800},
    ]
    print("AAAAAAAAAAAAAAAAAAAA", sort_by(jobs_to_sort, "max_salary"))
    sort_by(jobs_to_sort, "max_salary")
    assert jobs_to_sort == by_max_salary

    sort_by(jobs_to_sort, "min_salary")
    assert jobs_to_sort == by_min_salary

    sort_by(jobs_to_sort, "date_posted")
    assert jobs_to_sort == by_date_posted

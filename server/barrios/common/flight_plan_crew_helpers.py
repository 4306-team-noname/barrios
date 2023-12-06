from data.models import IssFlightPlanCrew, IssFlightPlanCrewNationalityLookup
from django.db.models import Sum
import datetime as dt


def get_total_crew_by_date(date: dt.date) -> int:
    total_crew_num = IssFlightPlanCrew.objects.filter(datedim=date).aggregate(
        total=Sum("crew_count")
    )["total"]
    return total_crew_num


def get_usos_crew_by_date(date: dt.date) -> int:
    usos_nat_values = IssFlightPlanCrewNationalityLookup.objects.filter(
        is_usos_crew=True
    ).values("nationality")
    usos_nationalities = [n["nationality"].strip() for n in usos_nat_values]
    all_crew = IssFlightPlanCrew.objects.filter(datedim=date)
    usos_sum = 0
    for crew in all_crew:
        if crew.nationality_category in usos_nationalities:
            usos_sum += crew.crew_count
    return usos_sum


def get_rsos_crew_by_date(date: dt.date) -> int:
    rsos_nat_values = IssFlightPlanCrewNationalityLookup.objects.filter(
        is_rsa_crew=True
    ).values("nationality")
    rsos_nationalities = [n["nationality"].strip() for n in rsos_nat_values]
    all_crew = IssFlightPlanCrew.objects.filter(datedim=date)
    rsos_sum = 0
    for crew in all_crew:
        if crew.nationality_category in rsos_nationalities:
            rsos_sum += crew.crew_count
    return rsos_sum


def get_commercial_crew_by_date(date: dt.date) -> int:
    all_crew = IssFlightPlanCrew.objects.filter(datedim=date)
    commercial_sum = 0
    for crew in all_crew:
        if crew.nationality_category == "Commercial":
            commercial_sum += crew.crew_count
    return commercial_sum


def get_other_crew_by_date(date: dt.date) -> int:
    usos_nat_values = IssFlightPlanCrewNationalityLookup.objects.filter(
        is_usos_crew=True
    ).values("nationality")
    usos_nationalities = [n["nationality"].strip() for n in usos_nat_values]
    rsos_nat_values = IssFlightPlanCrewNationalityLookup.objects.filter(
        is_rsa_crew=True
    ).values("nationality")
    rsos_nationalities = [n["nationality"].strip() for n in rsos_nat_values]
    all_crew = IssFlightPlanCrew.objects.filter(datedim=date)

    other_sum = 0
    for crew in all_crew:
        if (
            crew.nationality_category not in usos_nationalities
            and crew.nationality_category not in rsos_nationalities
            and crew.nationality_category != "Commercial"
        ):
            other_sum += crew.crew_count
    return other_sum

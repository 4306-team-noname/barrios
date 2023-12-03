import pandas as pd
from pandas import DataFrame
import datetime as dt
import math


#wants the csv flight plan
def get_dock_days(flight_plan: DataFrame):
    #query to only use dates where the event is dock and convert it to a list
    dock_days_list = flight_plan[flight_plan['event'] == 'Dock']['datedim'].to_list()

    #convert list of date strings into a list of datetime objects
    dates_list = [dt.datetime.strptime(date, '%m/%d/%Y').date() for date in dock_days_list]

    #returns a list of the days difference between each date
    return pd.Series(dates_list).diff().dt.days.iloc[1:].astype(int).tolist(), dock_days_list, (len(dock_days_list) -1)


#wants the csv flight_plan_crew
def get_crew_list(crewF: DataFrame, dock_days_list) -> list[int]:
    crew_per_dock = []

    for i, date in enumerate(dock_days_list):
        crewNum = crewF[crewF['datedim'] == date]['crew_count'].tolist()
        Amount = sum(crewNum)
        crew_per_dock.append(Amount)

    #returns a list of the number of crew members on board during each dock
    return crew_per_dock


#wants the csv rates_definition, and a consumable
def rates(rater, consumable):
    #sum of generated
    sum_generated = sum(rater[(rater['affected_consumable'] == consumable) & (rater['type'] == 'generation')]['rate'].to_list())

    #grabs the usage rates of consumable
    usage_list = rater[(rater['affected_consumable'] == consumable) & (rater['type'] == 'usage')]['rate'].to_list()

    #if units contains 'crew'
    crew_check = rater[(rater['affected_consumable'] == consumable) & (rater['type'] == 'usage')]['units'].tolist()

    sum_usage_list = []
    sum_usage_crew_list = []

    for i, j in enumerate(crew_check):
        if j.find('Crew') != -1:
            sum_usage_crew_list.append(usage_list[i])
        else:
            sum_usage_list.append(usage_list[i])

    sum_usage = sum(sum_usage_list)
    sum_usage_crew = sum(sum_usage_crew_list)

    return sum_usage, sum_usage_crew, sum_generated


#idk yet
def consumable_ascension(flight_plan: DataFrame, rater: DataFrame, consumable):
    df, dock_days_list, num_days = get_dock_days(flight_plan)
    
    sum_usage, sum_usage_crew, sum_generated = rates(rater, consumable)
    #create a list of base rates 
    listofrates = [sum_usage] * (num_days)
    listofrates_crew = []
    consumable_to_send = []
    current_sum = 0
    res_list = []

    for i in range(0, len(listofrates)):
        listofrates_crew.append(get_crew_list(df, dock_days_list)[i] * sum_usage_crew)

    for i in range(0, len(listofrates)):
        res_list.append(((listofrates[i] + listofrates_crew[i]) - sum_generated) * num_days[i])


    #rounding
    for i, value in enumerate(res_list):
        current_sum+=value
        consumable_to_send.append(math.trunc(current_sum))
        current_sum = current_sum - math.trunc(current_sum)

    #returns a list of the amount of consumables to send
    return consumable_to_send
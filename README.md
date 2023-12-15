> [!IMPORTANT]
> Please read the [development guidelines](#development-guidelines)!

# Barrios - 4306 - Software Engineering
Barrios Technologies project for Angelo State CS 4306 - Software Engineering

## Team Members
- [Jeff Caldwell](https://github.com/nemo-omen) - jcaldwell2@angelo.edu
- [Carlos Cardenas](https://github.com/arcxcc) - ccardenas11@angelo.edu
- [Josue Lozano](https://github.com/jlozano23) - jlozano18@angelo.edu
- [Jeremy Miles](https://github.com/jeremymiles) - jmiles10@angelo.edu
- [Jonathan Morgan](https://github.com/jmorgan28-01) - jmorgan28@angelo.edu

## Client Contacts
- Ginger Kerrick, Chief Strategy Officer - ginger.kerrick@barrios.com
- Devin Vyain, Data Solutions Lab Supervisor - devin.a.vyain@nasa.gov

## Project Mentor
[Mason Kindle](https://www.angelo.edu/live/profiles/13285-mason-kindle),  Graduate Assistant  - mkindle@angelo.edu

## Project Requirements
**Focus**

> Remember the following prompts for analysis, and center all of the effort around deriving insights into these prompts:
> Questions:
> 1. What is the percent difference between historical consumable usage rate assumptions and actual calculated usage rates in mission time frames between resupply?

__Answer__: Overall historical usage on the space station for the time period covered by client data was 1.04% less than assumed usage rates.

![Overall Usage](https://github.com/4306-team-noname/barrios/blob/8b0a4d748c6a11940b3ead6af81f7ee0126e0a12/assets/Final/OverallUsage.png)

> 2. What resupply quantities are necessary, considering planned resupply vehicle traffic from the ISS Flight Plan, planned On-Orbit Crew counts, and historical usage rates to sustain minimum supply thresholds, plus a 10% safety factor, through the next two years?

__Answer__: Usage quantities can be found in the table below.

| event_date | vehicle_name | ACY Inserts | Air      | Filter Inserts | KTO | Nitrogen | Oxygen  | Pretreat Tanks | Urine Receptacle | US Food BOBs | Water       |
| ---------- | ------------ | ----------- | -------- | -------------- | --- | -------- | ------- | -------------- | ---------------- | ------------ | ----------- |
| 2024-01-10 | Ax-3         | 63          | 282 lbs  | 0              | 1   | 3 lbs    | 52 lbs  | 0              | 0                | 1            | 177 Liters  |
| 2024-01-17 | DCC-1        | 172         | 484 lbs  | 1              | 5   | 6 lbs    | 177 lbs | 1              | 1                | 3            | 560 Liters  |
| 2024-01-29 | NG-20        | 155         | 686 lbs  | 1              | 4   | 8 lbs    | 127 lbs | 0              | 1                | 4            | 431 Liters  |
| 2024-02-15 | 87Progress   | 27          | 121 lbs  | 0              | 1   | 1 lbs    | 23 lbs  | 0              | 0                | 0            | 76 Liters   |
| 2024-02-18 | Crew-8       | 136         | 605 lbs  | 1              | 4   | 8 lbs    | 112 lbs | 1              | 1                | 3            | 380 Liters  |
| 2024-03-04 | SpX-30       | 346         | 1534 lbs | 2              | 9   | 18 lbs   | 283 lbs | 1              | 2                | 7            | 962 Liters  |
| 2024-04-11 | Boe-CFT      | 182         | 807 lbs  | 1              | 5   | 10 lbs   | 150 lbs | 1              | 1                | 4            | 507 Liters  |
| 2024-05-01 | HTV-X1       | 82          | 363 lbs  | 0              | 2   | 4 lbs    | 67 lbs  | 0              | 0                | 2            | 228 Liters  |
| 2024-05-10 | Ax-4         | 191         | 847 lbs  | 1              | 6   | 10 lbs   | 157 lbs | 1              | 1                | 4            | 532 Liters  |
| 2024-05-31 | 88Progress   | 273         | 1211 lbs | 2              | 7   | 15 lbs   | 224 lbs | 1              | 2                | 5            | 760 Liters  |
| 2024-06-30 | SpX-31       | 319         | 1412 lbs | 2              | 9   | 17 lbs   | 261 lbs | 2              | 2                | 7            | 886 Liters  |
| 2024-08-04 | USCV-9       | 136         | 605 lbs  | 1              | 4   | 7 lbs    | 112 lbs | 0              | 1                | 3            | 380 Liters  |
| 2024-08-19 | 89Progress   | 55          | 242 lbs  | 0              | 1   | 3 lbs    | 45 lbs  | 1              | 0                | 1            | 152 Liters  |
| 2024-08-25 | NG-21        | 191         | 848 lbs  | 1              | 5   | 10 lbs   | 157 lbs | 0              | 1                | 4            | 532 Liters  |
| 2024-09-15 | DCC-2        | 611         | 1896 lbs | 4              | 17  | 23 lbs   | 609 lbs | 3              | 4                | 13           | 1943 Liters |
| 2024-11-01 | PAM-5        | 291         | 1291 lbs | 1              | 8   | 16 lbs   | 239 lbs | 1              | 1                | 6            | 811 Liters  |
| 2024-12-03 | HTV-X2       | 36          | 162 lbs  | 1              | 1   | 1 lbs    | 30 lbs  | 0              | 1                | 0            | 101 Liters  |
| 2024-12-07 | 90Progress   | 210         | 928 lbs  | 1              | 6   | 12 lbs   | 172 lbs | 1              | 1                | 5            | 583 Liters  |
| 2024-12-30 | SPM          | 9           | 40 lbs   | 0              | 0   | 0 lbs    | 7 lbs   | 0              | 0                | 0            | 25 Liters   |
| 2024-12-31 | SpX-32       | 291         | 1291 lbs | 2              | 8   | 16 lbs   | 239 lbs | 2              | 2                | 6            | 811 Liters  |
| 2025-02-01 | NG-22        | 45          | 202 lbs  | 0              | 2   | 2 lbs    | 37 lbs  | 0              | 0                | 1            | 126 Liters  |
| 2025-02-06 | USCV-10      | 164         | 726 lbs  | 1              | 4   | 9 lbs    | 135 lbs | 1              | 1                | 3            | 456 Liters  |
| 2025-02-24 | 91Progress   | 728         | 3228 lbs | 4              | 20  | 39 lbs   | 597 lbs | 3              | 4                | 15           | 2027 Liters |
| 2025-05-15 | PAM-6        | 9           | 41 lbs   | 0              | 0   | 0 lbs    | 8 lbs   | 0              | 0                | 1            | 25 Liters   |
| 2025-05-16 | DCC-3        | 415         | 1170 lbs | 2              | 12  | 14 lbs   | 428 lbs | 1              | 2                | 8            | 1354 Liters |
| 2025-06-14 | 92Progress   | 437         | 1937 lbs | 3              | 12  | 23 lbs   | 359 lbs | 2              | 3                | 9            | 1216 Liters |
| 2025-08-01 | NG-23        | 27          | 121 lbs  | 0              | 0   | 2 lbs    | 22 lbs  | 0              | 0                | 1            | 76 Liters   |
| 2025-08-04 | USCV-11      | 255         | 1130 lbs | 2              | 7   | 13 lbs   | 209 lbs | 2              | 2                | 5            | 709 Liters  |
| 2025-09-01 | 93Progress   | 273         | 1210 lbs | 1              | 8   | 15 lbs   | 224 lbs | 1              | 1                | 6            | 760 Liters  |
| 2025-10-01 | CRS 2-24     | 282         | 1251 lbs | 2              | 8   | 15 lbs   | 232 lbs | 1              | 2                | 6            | 785 Liters  |
| 2025-11-01 | NG-24        | 228         | 1009 lbs | 1              | 6   | 12 lbs   | 187 lbs | 1              | 1                | 4            | 634 Liters  |
| 2025-11-26 | PAM-7        | 218         | 968 lbs  | 1              | 6   | 12 lbs   | 179 lbs | 1              | 1                | 5            | 607 Liters  |


> 3. What resupply quantities meet the requirements of question \#2 while minimizing launch vehicle quantity? (e.g., launching 10,000 granola bars would ensure the minimum thresholds are not violated, but is not a realistic or optimal strategy for balancing launch mass requirements with supply requirements)

__Answer__: Resupply quantities listed in the table above meet the minimum launch vehicle quantity based on the schedule represented in the `iss_flight_plan` data.

> 4. What month in the next two years of the Flight Plan timeline is most likely to incur a violation of minimum supply thresholds?

__Answer__: The time period most likely to incur a violation of minimum resupply thresholds is the period between launches in February, 2025 and May 2025.

![Resupply Failure Period](https://github.com/4306-team-noname/barrios/blob/ff0721e778ddb1218bb342f1a5b04885b2aba6b7/assets/Final/MostLikelyFailurePeriod.png)

> 5. Which consumables item(s) are most likely to incur a violation of minimum supply thresholds in the next two years of the future Flight Plan timeline?

__Answer__: Water is the most likely consumable to incur a violation of minimum resupply thresholds.

![Water Failure](https://github.com/4306-team-noname/barrios/blob/ff0721e778ddb1218bb342f1a5b04885b2aba6b7/assets/Final/MostLikelyFailureConsumable.png)

## Documentation
[Project Wiki](https://github.com/4306-team-noname/barrios/wiki)

## Installation
Installation instructions are on the [Installation Instructions](https://github.com/4306-team-noname/barrios/wiki/01-%E2%80%90-Installation) page.

## User Manual
A user manual can be found on the [User Manual](https://github.com/4306-team-noname/barrios/wiki/02-%E2%80%90-User-Manual) page.

## Project Iterations
- [Iteration 1: Requirements](https://github.com/4306-team-noname/barrios/wiki/Iteration-1:-Requirements)
- [Iteration 2: Design](https://github.com/4306-team-noname/barrios/wiki/Iteration-2:-Design)
- [Iteration 3: RAD and First Implementation](https://github.com/4306-team-noname/barrios/wiki/Iteration-3:-RAD-and-First-Implementation)
- [Iteration 4: Design](https://github.com/4306-team-noname/barrios/wiki/Iteration-4:-Design)
- [Iteration 5: Final Design Document](https://github.com/4306-team-noname/barrios/wiki/Iteration-5:-Final-Design-Document)

## Project Presentation
A slideshow presentation describing the project and its implementation can be viewed through the [presentation pdf](https://github.com/4306-team-noname/barrios/blob/82d9cd14ffeae308f3123e21589db65dd1983a41/assets/Final/Presentation_Team%20Noname.pdf).
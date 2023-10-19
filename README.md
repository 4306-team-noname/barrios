> [!IMPORTANT]
> Please read the [development guidelines](#development-guidelines)!

# Barrios - 4306 - Software Engineering
Barrios Technologies project for Angelo State CS 4306 - Software Engineering

## Team Members
- [Carlos Cardenas](https://github.com/arcxcc) - ccardenas11@angelo.edu
- [Jonathan Morgan](https://github.com/jmorgan28-01) - jmorgan28@angelo.edu
- [Jeremy Miles](https://github.com/jeremymiles) - jmiles10@angelo.edu
- [Josue Lozano](https://github.com/jlozano23) - jlozano18@angelo.edu
- [Jeff Caldwell](https://github.com/nemo-omen) - jcaldwell2@angelo.edu

## Weekly meeting times

### Team Meetings

Wednesday and Saturday, 7:30 p.m.

## Client Meetings

TBD

## Client Contacts
- Ginger Kerrick, Chief Strategy Officer - ginger.kerrick@barrios.com
- Devin Vyain, Data Solutions Lab Supervisor - devin.a.vyain@nasa.gov

## Project Mentor
[Mason Kindle](https://www.angelo.edu/live/profiles/13285-mason-kindle),  Graduate Assistant  - mkindle@angelo.edu

## Project Requirements
**Focus**

> Remember the following prompts for analysis, and center all of the effort around deriving insights into these prompts:
> Questions:
> 1. __Analysis__ (?)
> What is the percent difference between historical consumable usage rate assumptions and actual calculated usage rates in mission time frames between resupply?
> 2. __Optimization__
> What resupply quantities are necessary, considering planned resupply vehicle traffic from the ISS Flight Plan, planned On-Orbit Crew counts, and historical usage rates to sustain minimum supply thresholds, plus a 10% safety factor, through the next two years?
> 3. __Optimization__
> What resupply quantities meet the requirements of question \#2 while minimizing launch vehicle quantity? (e.g., launching 10,000 granola bars would ensure the minimum thresholds are not violated, but is not a realistic or optimal strategy for balancing launch mass requirements with supply requirements)
> 4. __Predictive modeling__
> What month in the next two years of the Flight Plan timeline is most likely to incur a violation of minimum supply thresholds?
> 5. __Predictive modeling__
> Which consumables item(s) are most likely to incur a violation of minimum supply thresholds in the next two years of the future Flight Plan timeline?

## Documentation
[Project Wiki](https://github.com/4306-team-noname/barrios/wiki)

## Project Tracking
[Github Projects](https://github.com/orgs/4306-team-noname/projects/1)

## Client Documentation
See markdown files in [client_docs](./client_docs) for the provided project summary and data dictionaries.

## Data
[Barrios data on Google Drive](https://drive.google.com/drive/u/0/folders/1QjZAWA7KyjAwYDQU2jbEDuHuvXdkoxZB)

## Resources
See the [resources](docs/resources.md) for a set of tools to use for data exploration, analysis, and manipulation.

## Development Guidelines
See the [guidelines](docs/guidelines.md) guidance on how to work with Git and GitHub.

## Running the development application

### Prerequisites
You need to have `docker` and `docker-compose` installed on your computer for everything to work properly. Both can probably be obtained by installing `Docker Desktop`.

#### Start Docker images
Start `docker-compose` from the root directory of the application (i.e. `barrios/`).

```bash
docker-compose up
```
This will pull the necessary docker images and set them up so you have a PostgreSQL server and a PGAdmin server running.

#### Set up the database through PGAdmin
1. __Connect to the database server with PGAdmin__
   1. 1. In a browser, navigate to `localhost:5050` (or `http://127.0.0.1:50`, if you're feeling verbose). This will open a setup page for PGAdmin. It will ask you to set a master password. Set it to whatever you want.
   2. In `Quick Links` on the front page, click `Add New Server`.
   3. On the tab labeled `General`, set the `Name` to `postgres`.
   4. In the `Connection` tab, set the `Host name/address` to `postgres` the username to `postgres`, and the password to `changeme`. You can toggle `Save password` if you want.
   5. Click `Save`
2. __Set up the database user__
   1. This will add the `postgres` server you loaded from the docker container. In the left sidebar, click `Servers`, then `postgres` to expand the menu.
   2. Right-click on `Login/Group Roles`, then choose `Create > Login/Group Role...`
   3. In the `General` tab, set the name to `barrios`.
   4.  In the `Definition` tab, set the password to `barrios123`
   5.  In the `Privileges` tab, turn on `Can log in?`
   6.  Click `Save`
3.  __Add the database__
    1.  In the left sidebar, under `postgres`, right-click on `Databases` and select `Create > Database...`
    2.  In the `General` tab, set the `Database` to `barrios`, and the `Owner` to `barrios`
    3.  Click `Save`

#### Populate the database tables
1. Back in the terminal, navigate to the `src` directory in the `barrios` project folder, then run a migration:
   ```bash
    cd src
    emmett migrations up
   ```

### Start the server
If there were no problems with the last command, you're good to go. Just start the development server (while still in the `barrios/src` directory) with:

```bash
emmett develop
```

Have fun!
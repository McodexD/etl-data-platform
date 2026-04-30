# Project Reflection: ETL Data Platform

## Agile Workflow (VG Criteria)
This project was conducted using an agile methodology. I defined the work using **User Stories** and tracked progress using a **GitHub Project Board**. Development was done in a separate **feature branch**, and changes were integrated into the main branch via **Pull Requests**.

## How it could have been more agile
To make this even more agile, I could have:
1. **Defined smaller Sprints**: Instead of one large push, I could have set 2-day goals to get feedback earlier.
2. **Automated Testing**: Adding unit tests for the 'Transform' phase would allow for faster, more confident iterations.
3. **Continuous Deployment**: Setting up a GitHub Action to automatically deploy the FastAPI code would shorten the delivery cycle.

## Technical Choice
I chose **Pandas** for the transformation phase because it is highly efficient at generating the statistical results required by the F11 criteria. **FastAPI** was used to satisfy the requirement of exposing the data flow to the user.
---
layout: posts
title:  "Real Estate Launch"
date:   2024-08-10
tags: PBI
author_profile: true
author: Chris Brockett
categories: work
highlight_home: true
tagline: "PBI Dax"
header:
  overlay_image: /assets/images/sand.jpg
  teaser: /assets/images/sand.jpg
  
  caption: "Photo credit: Chris Brockett"
description: A mix of Sql and Excel
---

## Goal
This project was to look at Zillow data and provide recommendations on how to launch a real estate company.  All data used for this project came from Zillow.  This one is a bit different from other projects that I have built as I tailored it for a presentation with the thought of converting it to a tracking tool if the company went live.

<iframe src="/assets/pdf/realestate.pdf" width="900" height="400"></iframe>

## Project
I began by analyzing the data to identify trends based on area. While graphing the data, I noticed a drastic change from 2020 to 2023. The Covid lockdowns drove a spike in sales due to increased remote work, but this also led to a subsequent downturn, making it a challenging environment to launch a real estate business.

## Recommendation
There were three options to consider: a nationwide launch, a limited scope launch, or no launch at all. Given the 30% decrease in home sales since 2020, launching nationwide carries a high degree of risk. My recommendation is to launch in a single location, such as Los Angeles. Los Angeles still has a strong average number of homes sold per month and a lower mean number of days to close. This approach allows the company to establish its culture, define its market presence, and then expand into other markets.

The last couple of pages outline potential future offerings and data sets that could help the company grow and dive deeper into the business.

## Dax
Used 2 dax calculations to determine the difference between 2023 and 2020.  Set it up to ensure that if they changed the date filter it wouldnt break the results

2023 price = CALCULATE([AVG Sale Price],FILTER(all('Calendar Cust'),'Calendar Cust'[Year] = 2023 ))

Calendar function - tied to min /max date off of data project so that if data was updated the calendar updated as well.  Also broke out the date so that I could filter properly and the months would not filter in wrong order.

Calendar Cust = 
ADDCOLUMNS (
    CALENDAR (MIN('Client Analyst Data Project - Sales Count'[Month]), max('Client Analyst Data Project - Sales Count'[Month])),
    "Calendar Date", [Date],
    "Year", YEAR ( [Date] ),
    "Calendar Month", FORMAT ( [Date], "MMM" ) & " " & right(format([Date], "yyyy"),2) ,
    "Calendar Week", "CY " & right(format([Date], "yyyy"),2) & " - " &FORMAT ( [Date], "MMM" ) & " WK " &weeknum([Date]),
    "Month Number", VALUE(YEAR ( [Date] ) & format(MONTH([Date]),"00")),
    "Month Sort",MONTH([Date]),
    "Month Name", FORMAT ( [Date], "MMMM" ),
    "Day", DAY ( [Date] ),
    "Day of Week Number", WEEKDAY ( [Date] ),
    "Day of Week Name", FORMAT ( [Date], "dddd" )
)
## Learning
- It was interesting to see the real estate data and the impact to the market due to Covid
- How to create a calendar function.  So use to having calendars within the databases that I could use.
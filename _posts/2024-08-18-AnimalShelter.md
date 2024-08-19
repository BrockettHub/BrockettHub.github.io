---
layout: posts
title:  "Animal Shelter"
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
description: A mix of excel and PBI
---
## Executive Summary
We are successfully maintaining our no-kill shelter status by staying above the 90% threshold, currently achieving a 93.9% live release rate. While this is commendable, it marks an 8% decrease from the previous year.

The primary factor contributing to this decline is the incidence of rabies within the "other" classification of animals. To address this issue, it is recommended to:

- We should stop accepting bats and raccoons. Currently, these animals have a combined successful release rate of only 10%. By preventing them from being taken in, we can increase our overall success rate for this year to 96%.
- Check with state laws to see if these animals should count within the no kill percentage.
- Targeted Health Interventions: Implement focused health and safety measures for the identified animals to reduce rabies cases.

By addressing these areas, we can work towards improving our live release rate and ensure the ongoing success of our no-kill shelter.

<iframe src="/assets/pdf/Animal no kill.pdf" width="900" height="400"></iframe>

## Project
Since I have been volunteering with an animal shelter, this data was fun to peek at to understand more about how shelters work.

## Data Cleaning
This particular data set threw some unique challenges.  I expected some duplication within the data as some animals could come through the system multiple times.  To check I performed a ranking function within power query to see if that would remove duplications based on animal id and date.  There were still duplications but since it was only 90 records out of 160 k, I just had power query remove duplicates.

## Dax
To compare this year vs last year crafted 2 dax measures and set them up so if they changed filters it wouldnt change the value.  Here is one of them.
Current Year = CALCULATE([Cases], filter(all(Austin_Animal_Center_Outcomes_20240818),year(Austin_Animal_Center_Outcomes_20240818[DateTime])=year(today())&& Austin_Animal_Center_Outcomes_20240818[Outcome Type] = "Euthanasia" )) / CALCULATE([Cases], filter(all(Austin_Animal_Center_Outcomes_20240818),year(Austin_Animal_Center_Outcomes_20240818[DateTime])=year(today())))

## Learning
How to do ranking within power query
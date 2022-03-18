## University Project under Natural Language Processing Subject (BITI3413)

Link to [News Classification](https://biti3413-nlp-newsclassify.herokuapp.com/)
Note: Opening this link may take up to 1 minute to load

A web application were developed using Heroku. The AI which responsible in classifying the news were integrated to Heroku.
The web app fetch the article from the given link. Then, the article was tokenise into words to get the word frequency using Bag of Words (BOW). The AI classifies the news by reading the pattern number of words.

## Model
We use Neural Network to classify the news. In input layer, there are 147 nodes and each nodes represent the word.

Word | Sum of TF IDF
--- | ---  
health
business
car
family
people
technology
travel
company
time
country
science
religious
data
government
game
team
work
religion
sport
world
state
system
child
service
entertainment
way
player
league
case
research
vehicle
digital
change
community
political
public
industry
care
group
party
home
test
holiday
school
life
support
student
plan
customer
member
market
global
social
event
experience
minister
university
number
program
information
politics
level
development
content
issue
future
leader
show
city
national
online
international
education
across
risk
model
ai
opportunity
report
parent
percent
mental
study
news
sports
area
employee
policy
video
church
product
process
result
price
law
climate
story
local
cost
scientist
space
project
medical
republic
human
platform
premier
job
decision
president
feel
growth
play
film
share
free
role
sector
safety
office
supply
healthcare
power
sale
brand
control
organization
rate
patient
idea
value
rule
energy
club
election
ministry
economy
goal
investment
demand
consumer
money
strategy
food
society
measure
director
Table above shows the 147 words used as node for input layer. The sum of TF IDF are the total value of TF IDF from each thousands of scraped articles.

## Results
<p align="center">
  <img width="517" height="400" src="https://user-images.githubusercontent.com/55189926/158936358-4d931049-4021-48ba-aeb1-ed6a95efd93d.png">
  <img width="478" height="400" src="https://user-images.githubusercontent.com/55189926/158936370-c71ece58-ddf9-4f5a-ab8e-65aeb1fd5a30.png">
  <br>
  Result 1 (Page to <a href="https://www.unlv.edu/news/release/astronomers-closer-unlocking-origin-mysterious-fast-radio-bursts">Article</a>)
  <br>
</p>

<p align="center">
  <img width="503" height="390" src="https://user-images.githubusercontent.com/55189926/158937328-6b3a1c71-f887-4e4b-9bd1-d53042b79031.png">
  <img width="493" height="390" src="https://user-images.githubusercontent.com/55189926/158937835-c6d9684f-45eb-4d3b-8975-09918eadcee8.png">
  <br>
  Result 2 (Page to <a href="https://www.malaymail.com/news/malaysia/2022/03/16/celcom-digi-maxis-and-u-mobile-welcome-govt-decision-to-rollout-5g-via-sing/2047827">Article</a>)
</p>

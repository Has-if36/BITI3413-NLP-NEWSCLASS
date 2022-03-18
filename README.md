## University Project under Natural Language Processing Subject (BITI3413)

Link to [News Classification](https://biti3413-nlp-newsclassify.herokuapp.com/)
Note: Opening this link may take up to 1 minute to load

A web application were developed using Heroku. The AI which responsible in classifying the news were integrated to Heroku.
The web app fetch the article from the given link. Then, the article was tokenise into words to get the word frequency using Bag of Words (BOW). The AI classifies the news by reading the pattern number of words.

## Model
We use Neural Network to classify the news. In input layer, there are 147 nodes and each nodes represent the word.

Word | Sum of TF IDF
--- | ---  
health			| 41.6533237
business		| 38.61746642
car				| 34.23202733
family			| 30.46119777
people			| 28.17926318
technology		| 27.35149981
travel			| 25.00928354
company			| 24.20728763
time			| 22.3715341
country			| 20.97434797
science			| 20.77201082
religious		| 20.61842605
data			| 20.24902703
government		| 19.34505328
game			| 18.6838436
team			| 18.40271764
work			| 17.58363177
religion		| 17.24608716
sport			| 17.10946304
world			| 17.10181797
state			| 16.95911084
system			| 16.50585173
child			| 16.46207316
service			| 16.33497502
entertainment	| 16.04002719
way				| 15.95330127
player			| 15.93718143
league			| 15.5544716
case			| 15.36784611
research		| 15.25450805
vehicle			| 15.17379989
digital			| 14.40210379
change			| 14.38752062
community		| 14.38094741
political		| 14.3434005
public			| 14.24519699
industry		| 13.96607222
care			| 13.55281198
group			| 13.44963881
party			| 13.40881577
home			| 13.37936071
test			| 13.27930774
holiday			| 13.26491019
school			| 12.66078053
life			| 12.50129079
support			| 12.30904417
student			| 12.25145751
plan			| 12.12053761
customer		| 12.00568717
member			| 11.81219047
market			| 11.76804372
global			| 11.67965675
social			| 11.66538553
event			| 11.64581729
experience		| 11.61844199
minister		| 11.28101249
university		| 11.23539087
number			| 11.21867066
program			| 11.18955657
information		| 11.12466522
politics		| 10.70329016
level			| 10.69308764
development		| 10.62008584
content			| 10.55540449
issue			| 10.54764995
future			| 10.51840039
leader			| 10.51159032
show			| 10.5061875
city			| 10.43624103
national		| 10.41283714
online			| 10.24005849
international	| 10.13097604
education		| 10.11096361
across			| 10.08096942
risk			| 10.06675989
model			| 9.972340776
ai				| 9.931241871
opportunity		| 9.881564684
report			| 9.849350424
parent			| 9.841288643
percent			| 9.827359326
mental			| 9.724779523
study			| 9.719974673
news			| 9.68304396
sports			| 9.649790426
area			| 9.51825061
employee		| 9.4959338
policy			| 9.487552872
video			| 9.440121893
church			| 9.436940575
product			| 9.428884367
process			| 9.39040686
result			| 9.334774238
price			| 9.304248001
law				| 9.260885433
climate			| 9.167669087
story			| 9.032192251
local			| 9.027344456
cost			| 9.01436005
scientist		| 8.862163859
space			| 8.828530191
project			| 8.788232113
medical			| 8.758672574
republic		| 8.719653682
human			| 8.685659441
platform		| 8.618741183
premier			| 8.602349769
job				| 8.572289349
decision		| 8.444496722
president		| 8.404323172
feel			| 8.363726554
growth			| 8.354904459
play			| 8.342200321
film			| 8.320734255
share			| 8.270504997
free			| 8.2503904
role			| 8.192606791
sector			| 8.186839126
safety			| 8.08468343
office			| 8.042315815
supply			| 8.022996647
healthcare		| 7.997445267
power			| 7.96541427
sale			| 7.947031772
brand			| 7.843004326
control			| 7.765204949
organization	| 7.694313615
rate			| 7.689793811
patient			| 7.681432879
idea			| 7.669635576
value			| 7.650902498
rule			| 7.534836295
energy			| 7.530643808
club			| 7.459510787
election		| 7.425900799
ministry		| 7.350946872
economy			| 7.326925221
goal			| 7.275322461
investment		| 7.269394197
demand			| 7.268122866
consumer		| 7.252617857
money			| 7.238944767
strategy		| 7.168477706
food			| 7.148693334
society			| 7.146264275
measure			| 7.118912537
director		| 7.081201491

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

# **findMatariki by Team NSB**

### **Preface**

Matariki is the Māori name of the Pleides star cluster. The predawn rising of Matariki in the mid-winter sky marks the changing of the seasons and the beginning of the Maori New Year. Traditionally, this was used to determine the coming season's crop; a warmer season, and therefore a more productive crop yield, was indicated by how bright the stars were. 

Today, Matariki serves as a celebration of whanaungatanga (kinship), a time for whanau (families) to "reflect on the past year, celebrate the present, and plan for the year ahead". With the passing of [The Matariki Public Holiday Bill](https://www.parliament.nz/en/pb/bills-and-laws/bills-proposed-laws/document/BILL_115986/te-pire-m%C5%8D-te-hararei-t%C5%ABmatanui-o-te-k%C4%81hui-o-matarikite), Aotearoa celebrated its first official public holiday this year on Friday, the 24th of June. 

As part of our school Hackathon, we have programmed a user-friendly python script using [NASA's JPL Horizons API](https://ssd-api.jpl.nasa.gov/doc/horizons.html) that outputs the date of the public holiday with any reasonable year as an input. 

We believe this script also has real-world practical use for whanau on a national level. Therefore, we have concocted a [concept design](https://docs.google.com/presentation/d/19V19oQvpHnYjP2_FcM1_xw8tZIVGi9tB801cl1HUxh0/edit#slide=id.p) for a Chrome extension as a possible future implementation. Rangatahi (younger generation) could use this extension to find out when the Matariki public holiday will be on a recent year; they could then get into contact with their tūpuna (grandparents) to get together. Not only would this celebrate the purpose of Matariki, this could also form the basis of a culture change by bridging the growing gap between tuakana-teina (relationship between youth and elderly), by enabling our youth to take the first step for connection.

## **Installation**

To install the required libraries, go to the root path of the repo and run the following:
```
pip install -r requirements.txt
```

## **Usage**
```
In the root directory, run:
```
python findMatariki.py
```

Then enter the year and the Matariki date for that year will be returned.


## **Methodology**
 ### On the surface
 The program will prompt you to enter a **REASONABLE** year as the input. Press enter after writing down the year you would like to predict. Then, the program will return the date of Matariki in YYYY-MM-DD format for that year. 
 The year chosen has to be a number, and it must be a number between 1000 to 9999 inclusive (the justification behind this is in Merits).
 ### Digging deeper

## **Merits**
  - Specifications
  Our script finds the correct Matariki date for the next 50 years (2022-2052), as outlined in [this document](https://www.mbie.govt.nz/assets/matariki-dates-2022-to-2052-matariki-advisory-group.pdf). Not only this, we are also able to predict the Matariki date for a long range of years, both in the future and in the past. Since NASA's JPL Horizons API has moon phase data available from years 1000 to 9999 inclusive, this means our script can predict when Matariki was as far as 1022 years ago, as well as when it will be 7977 years in the future, and anywhere in between. We have displayed the predictions in a YYYY-MM-DD format for convenience.
  - Readability
  We have added docstrings to our script (findMatariki.py) so that anyone, with a coding background or not, can follow along. These comments guide the reader systematically from top to bottom, documenting every function, class, and module. Here is an example:
Furthermore, under our Alternative Solutions, we also added detailed string comments explaining how these solutions work. To illustrate:
  - Reusability
  Every function defined is structured on its own, so that they can be reusable in other programs. We ensured this was the case when we were starting as we knew a possible development on this script could be to use it as a [Chrome extension](https://docs.google.com/presentation/d/19V19oQvpHnYjP2_FcM1_xw8tZIVGi9tB801cl1HUxh0/edit#slide=id.p).
  - Documentation
  Refer to "Methodology" and "Alternative Solutions".
  - Efficiency
  
  - Teamwork
 Our group was the first to make a repo and push commits, and both members have written >1/2n code.
  - Creativity & Difficulty
 Refer to "Alternative Solutions". We used both lunation/api based calculations

## **Alternative Solutions**
other solutions are not as accurate

## **Contributors**
@Sttaseen - findMatariki
@xGhqul - testing, commenting

# **findMatariki by Team NSB**
### **Preface**

Matariki is the Māori name of the Pleides star cluster. The predawn rising of Matariki in the mid-winter sky indicates the changing of the seasons and the beginning of the Māori New Year. Traditionally, this was used to deduce the coming season's crop; a warmer season, and therefore a more productive crop yield, was indicated by how bright the stars were. 


<p align="center">
  <img width="436" height="436" src="https://user-images.githubusercontent.com/67076071/181239364-db4690c8-5d69-4059-92c1-19e911d018df.png">
</p>


Today, Matariki serves as a celebration of whanaungatanga (kinship), a time for whanau (families) to "reflect on the past year, celebrate the present, and plan for the year ahead". With the passing of [The Matariki Public Holiday Bill](https://www.parliament.nz/en/pb/bills-and-laws/bills-proposed-laws/document/BILL_115986/te-pire-m%C5%8D-te-hararei-t%C5%ABmatanui-o-te-k%C4%81hui-o-matarikite), Aotearoa celebrated its first official public holiday this year on Friday, the 24th of June. 

As part of our school Hackathon, we have programmed this user-friendly python script using [NASA's JPL Horizons API](https://ssd-api.jpl.nasa.gov/doc/horizons.html) to predict the date of the public holiday with any reasonable year as an input. 

We believe this script also has real-world practical use for whanau on a national level. Therefore, we have concocted a [concept design](https://docs.google.com/presentation/d/19V19oQvpHnYjP2_FcM1_xw8tZIVGi9tB801cl1HUxh0/edit#slide=id.p) for a Chrome extension as a possible future implementation. Rangatahi (younger generation) could use this extension to find out when the Matariki public holiday will be on a recent year; they could then get into contact with their tūpuna (grandparents) to get together. Not only would this celebrate the purpose of Matariki, this could also form the basis of a culture change by bridging the growing gap between tuakana-teina (relationship between youth and elderly), by enabling our youth to take the first step for connection.

## **Installation**

To install the required libraries, go to the repository folder. Then run the following in your command prompt:
```
pip install -r requirements.txt
```

## **Usage**

In the root directory, run:
```
python findMatariki.py
```
The program will prompt you to enter a year as an input. Enter the year and the Matariki date for that year will be returned.

[Here](https://www.youtube.com/watch?v=6a-HgocFTS0&feature=youtu.be) is a short video demonstrating how to use the program.

## **Methodology**
Since the Matariki dates were [determined](https://www.mbie.govt.nz/assets/matariki-dates-2022-to-2052-matariki-advisory-group.pdf) by using the knowledge that the Matariki becomes visible during the Tangaroa period of a Maori lunar month, we used lunar cycles to find this Tangaroa period.

- Use NASA's Horizon API to get the Sun-to-Phase (STO) phase angles of the moon.
- Determine the local maximas of these STO values using ```argrelextrema``` from the```SciPy.Signal``` library. These gives us the times for the new moons of different months. 
- Use the fact that Tangaroa always occurs after the 19th of June and that the Tangaroa period always starts on the 23rd day of a lunar month to find the first day of the Tangaroa period after the 19th of June.
- Use ```Matariki.closestFriday()``` to determine closest Friday to the start of the Tangaroa period which is also the Matariki day for that year.

## **Specifications**
Our script finds the correct Matariki date for the next 50 years (2022-2052), as outlined in [this document](https://www.mbie.govt.nz/assets/matariki-dates-2022-to-2052-matariki-advisory-group.pdf). Not only this, we are also able to predict the Matariki date for a long range of years, both in the future and in the past. Since NASA's JPL Horizons API has moon phase data available from years 1000 to 9999 inclusive, this means our script can predict when Matariki was as far as 1022 years ago, as well as when it will be 7977 years in the future, and anywhere in between. We have displayed the predictions in a YYYY-MM-DD format for convenience.

We have added docstrings to our script (findMatariki.py) so that anyone, with a coding background or not, can follow along. These comments guide the reader systematically from top to bottom, documenting every function, class, and module. Here is an example:

![code](https://i.imgur.com/r6ngXUI.jpg)

Every function defined is structured on its own, so that they can be reusable in other programs. We ensured this was the case when we were starting as we knew a possible development on this script could be to use it as a [Chrome extension](https://docs.google.com/presentation/d/19V19oQvpHnYjP2_FcM1_xw8tZIVGi9tB801cl1HUxh0/edit#slide=id.p).

## **Contributors**
[@Sttaseen](https://github.com/sttaseen)

[@xGhqul](https://github.com/xGhqul)

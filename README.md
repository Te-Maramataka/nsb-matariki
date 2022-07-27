# **TEAM NSB**

### **Preface**
Matariki is the Māori name of the Pleides star cluster. The predawn rising of Matariki in the mid-winter sky marks the changing of the seasons and the beginning of the Maori New Year. Traditionally, this was used to determine the coming season's crop; a warmer season, and therefore a more productive crop yield, was indicated by how bright the stars were. Today, Matariki serves as a celebration of whanaungatanga (kinship), a time for whanau (family) to "reflect on the past year, celebrate the present, and plan for the year ahead". With the passing of [The Matariki Public Holiday Bill](https://www.parliament.nz/en/pb/bills-and-laws/bills-proposed-laws/document/BILL_115986/te-pire-m%C5%8D-te-hararei-t%C5%ABmatanui-o-te-k%C4%81hui-o-matarikite), Aotearoa celebrated its first official public holiday this year on Friday, the 24th of June. Using NASA's JPL Horizons API, we have programmed a user-friendly python script that outputs the date of the public holiday with any reasonable year as input. As well as being a submission for our school Hackathon, we believe this script would have practical use for any families 

## **Installation**

## **Usage**

## **Our Strategy**

## **Documentation**
other solutions are not as accurate

## **Merits**
  - Specifications
  Our script finds the correct Matariki date for the next 50 years (2022-2052), as outlined in [this document](https://www.mbie.govt.nz/assets/matariki-dates-2022-to-2052-matariki-advisory-group.pdf). Not only this, we are also able to predict the Matariki date for a long range of years, both in the future and in the past. Since NASA's JPL Horizons API has moon phase data available from years 1000 to 9999 inclusive, this means our script can predict when Matariki was as far as 1022 years ago, as well as when it will be 7977 years in the future, and anywhere in between. We have displayed the predictions in a YYYY-MM-DD format for convenience.
  - Readability
  We have added docstrings to our script (findMatariki.py) so that anyone, with a coding background or not, can follow along. These comments guide the reader systematically from top to bottom, documenting every function, class, and module. Here is an example:
Furthermore, under our Alternative Solutions, we added detailed string comments explaining how these solutions work. To illustrate:
  - Reusability
  Every function defined is structured on its own, so that they can be reusable in other programs. We ensured this was the case when we were starting as we knew a possible development on this script could be to use it as a Chrome extension.
  - Documentation
  Refer to "Our Strategy" and "Alternative Solutions".
  - Efficiency
  
  - Teamwork
 Our group was the first to make a repo and push commits, and both members have written >1/2n code.
  - Creativity & Difficulty
 Refer to "Alternative Solutions". We used both lunation/api based calculations

## **Alternative Solutions**

![Multaja'](images/head.png)

### Motivation
We no longer live in a world where refugee migration doesn’t touch us. As citizens in this global village, we are linked. Some members of our team have followed reports of refugee displacement on the news, and some of our team have seen it with their own eyes. This weekend (Oct 19-21), we felt particularly compelled by the challenge to collect and analyze satellite imagery to learn about land occupied by displaced populations. 

### The Challenge
Design an approach that uses NASA Earth observations data to characterize land cover & land use conditions at informal settlements.

#### Seal_Team_404
* Abhi Banerjee
* Kevin Africa
* Chris Bowers
* Grace Shea
* Jared Anderson

**Space Apps Challenge Hackathon** - Seattle, WA - October 19-21, 2018
- "Best Use of Data" Winner (1st place Data Science)
- Finalist in Seattle, moving on toward's Global Competition!

<p align="center">
  <img src="images/space_apps.png" width="350" title="NASA SpaceApps 2018 - Seattle ">
</p>

### Our Project
Multaja', the Arabic word for 'refuge', 'shelter' & 'sanctuary', is the name of our project. Utilize an ensemble of various machine learning techniques including K-means clustering, open vision and time series forecasting to quantify & predict number of structures and infer populations at a refugee camp. Governments, NGOs and other aid agencies can now allocate resources more accurately with less down-time.

Our solution is:

* Scalable to other settlements
* Sensitive to the local geography, climate & geo-political situation
* Can be adapted to be easily understandable for residents, humanitarians, policy makers, scientists, and others who are committed to the welfare of vulnerable populations

### Scope
Rukban, Syria - At the northeastern corner Jordan, at the joint border of Syria and Iraq, there is a refugee camp in dire need of aid. It is often referred to as the most desperate settlement of Syrian refugees. Due to its remoteness, but also due to the Jordanian government’s desire to restrict refugee access.

### Modeling
Satellite imagery was taken from the Sentinel-2 dataset. For the initial analysis the image below was used:

![Rukban](images/rukban.png)

K-means clusering, by detecting man-made structures, provides a good estimation of population density

![Rukban](images/rukban_clustered.png)

Applying a binary filter

![Rukban](images/rukban_binary.png)

Several Blob Detection Algorithms are applied as well. By using a count of the detected blobs and the density of the clustering, we can estimate population density and the change of population density over time.

![Rukban](images/rukban_blobs.png)

### Links
- Presentation Slides: https://bit.ly/2EDTzAt
- GitHub: https://github.com/drunkONdata/Multaja
- SpaceApps Project Page: https://bit.ly/2RolXbh
- Video of Presentation in Seattle: https://youtu.be/6BhrshuaHlU <br>(**NOTE**: Project was renamed to Multaja' from Ma'waa)

### Future Work
* Engage NGOs and aid workers for greater nuanced understanding of metrics and KPIs that matter to their planning and policy making
* Create dashboard that automatically updates population forecasts with updated satellite imagery data
* Aggregate high resolution satellite imagery for various conflict zones to be analyzed by the Multaja' machine learning platform to mitigate data scarcity and build robust time series forecast
* Model validation with labeled data
* Incorporating imaging from different spectra for machine learning platform
* Develop app that governments and NGOs can use to allocate resources and develop response plans

### Additional Background
In Northeastern corner Jordan, at the joint border of Syria and Iraq, there is a refugee camp in dire need of aid. This camp is in Rukban. It is often referred to as the most desperate settlement of Syrian refugees. This is not only due to its remoteness, but also due to the Jordanian government’s desire to restrict refugee access to Jordan from this area due to security concerns. 

The refugee population in Rukban have fled Islamic State controlled territories such as Raqqa, and the Jordanian government believes that ISIS has infiltrated these refugees. The United Nations and the Jordanian government have been at odds on this issue. Several terrorist attacks have taken place over the past two years, resulting in the deaths of Syrian refugees and Jordanian Soldiers.

On the Syrian side, the Syrian government has blocked all avenues of aid to this camp.  On the Jordanian side, humanitarian aid has halted due to the increased danger for Jordanian Soldiers and NGO workers.

As of this month, UNICEF estimates that 45,000 people live at the camp and have reported the death of two children due to starvation. The UN announced last week that preparations are underway for the first aid convoy in 9 months to reach Rukban in the next few days.

### MIT License
Copyright (c) 2018 Multaja'

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
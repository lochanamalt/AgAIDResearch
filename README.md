# AgAID Research Project

### Washington State University

---

**Mentor: Sindhuja Sankaran**

**Research Grad Student Resources**
* Lochana Marasingha
* Chamaporn Paiboonvorachat

By: **Trevor Buchanan**

---

### Units and labels:
 - Temperatures: Celsius
 - Yield: Bushels/Acre
 - Soil temperature depth: Inches
 - Plant height: Inches
 - Plot area: Square feet
 - IoT: Internet of Things

## Project progress summary:
* 06/10/2024 - Familiarization with data and begin to parse
* 06/11/2024 - Continue to parse data and begin create visualizations for it
* 06/12/2024 - Expand and refine visualizations and interpolate between missing 
data with multiple techniques depending on the data type (e.i. vi and temperature 
have very different trajectory paths, so the same interpolation cannot be used 
for both. Furthermore, some information can be filled from other IoT units at the 
site, and other online resources such as weather data)
* 06/13/2024 - Refactor and begin to use time series learning models


## Notes:
* Spring wheat crop was planted on the 25th of April
* Vegetation index (vi) formula names: cigreen0, cigreen, evi2, gndvi0, gndvi, ndvi, rdvi, savi, sr
* The vi used will only be the 'mean' value for each data point
* Labels in full data and ground truth data: variety_index <-> variety <-> ENTRY | replication_variety <-> BLOC
* The soil temperature measurement used is the 8-inch average
* Winter varieties:
1. Rosalyn
2. Otto
3. Puma
4. Purl
5. Jasper
6. Inspire
7. Piranha CL+
8. Jameson
* Spring varieties:
1. Glee
2. Kelse 
3. Alum
4. Chet
5. Louise
6. Ryan
7. Seahawk
8. Whit
9. Dayn
10. Tekoa
11. Net CL+
12. Jedd

### Missing Data Points Notes For Winter Wheat:
(Dates with * marker are within 2 weeks of heading date)

**Block: 1, Entry: 1 data points length: 68**
* Heading date: 2022-06-19
	* 2022-05-20
	* 2022-05-27
	* 2022-05-29
	* 2022-06-04
	* 2022-06-05
	* *2022-06-07
	* *2022-06-08
	* *2022-06-09
	* *2022-06-11
	* *2022-06-13
	* *2022-07-01
	* 2022-07-07
	* 2022-07-08

**Block: 1, Entry: 2 data points length: 68**
* Heading date: 2022-06-23
	* 2022-05-20
	* 2022-05-27
	* 2022-05-29
	* 2022-06-04
	* 2022-06-05
	* 2022-06-07
	* 2022-06-08
	* 2022-06-09
	* *2022-06-11
	* *2022-06-13
	* *2022-07-01
	* 2022-07-07
	* 2022-07-08

**Block: 1, Entry: 3 data points length: 68**
* Heading date: 2022-06-20
	* 2022-05-20
	* 2022-05-27
	* 2022-05-29
	* 2022-06-04
	* 2022-06-05
	* *2022-06-07
	* *2022-06-08
	* *2022-06-09
	* *2022-06-11
	* *2022-06-13
	* *2022-07-01
	* 2022-07-07
	* 2022-07-08

**Block: 1, Entry: 4 data points length: 68**
* Heading date: 2022-06-20
	* 2022-05-20
	* 2022-05-27
	* 2022-05-29
	* 2022-06-04
	* 2022-06-05
	* *2022-06-07
	* *2022-06-08
	* *2022-06-09
	* *2022-06-11
	* *2022-06-13
	* *2022-07-01
	* 2022-07-07
	* 2022-07-08

**Block: 1, Entry: 5 data points length: 73**
* Heading date: 2022-06-21
	* 2022-05-27
	* 2022-05-29
	* *2022-06-11
	* *2022-06-13
	* 2022-07-22
	* 2022-07-26
	* 2022-07-29

**Block: 1, Entry: 6 data points length: 73**
* Heading date: 2022-06-22
	* 2022-05-27
	* 2022-05-29
	* *2022-06-11
	* *2022-06-13
	* 2022-07-22
	* 2022-07-26
	* 2022-07-29

**Block: 1, Entry: 7 data points length: 73**
* Heading date: 2022-06-18
	* 2022-05-27
	* 2022-05-29
	* *2022-06-11
	* *2022-06-13
	* 2022-07-22
	* 2022-07-26
	* 2022-07-29

**Block: 1, Entry: 8 data points length: 73**
* Heading date: 2022-06-21
	* 2022-05-27
	* 2022-05-29
	* *2022-06-11
	* *2022-06-13
	* 2022-07-22
	* 2022-07-26
	* 2022-07-29

**Block: 2, Entry: 4 data points length: 73**
* Heading date: 2022-06-20
	* 2022-05-25
	* 2022-05-28
	* 2022-05-29
	* 2022-05-30
	* 2022-05-31
	* 2022-06-01
	* *2022-06-11
	* *2022-06-13

**Block: 2, Entry: 5 data points length: 73**
* Heading date: 2022-06-22
	* 2022-05-25
	* 2022-05-28
	* 2022-05-29
	* 2022-05-30
	* 2022-05-31
	* 2022-06-01
	* *2022-06-11
	* *2022-06-13

**Block: 2, Entry: 8 data points length: 73**
* Heading date: 2022-06-22
	* 2022-05-25
	* 2022-05-28
	* 2022-05-29
	* 2022-05-30
	* 2022-05-31
	* 2022-06-01
	* *2022-06-11
	* *2022-06-13

**Block: 2, Entry: 7 data points length: 73**
* Heading date: 2022-06-19
	* 2022-05-25
	* 2022-05-28
	* 2022-05-29
	* 2022-05-30
	* 2022-05-31
	* 2022-06-01
	* *2022-06-11
	* *2022-06-13

**Block: 2, Entry: 2 data points length: 76**
* Heading date: 2022-06-24
	* 2022-05-29
	* *2022-06-11
	* 2022-07-26
	* 2022-07-27
	* 2022-07-28

**Block: 2, Entry: 3 data points length: 76**
* Heading date: 2022-06-18
	* 2022-05-29
	* *2022-06-11
	* 2022-07-26
	* 2022-07-27
	* 2022-07-28

**Block: 2, Entry: 1 data points length: 76**
* Heading date: 2022-06-22
	* 2022-05-29
	* *2022-06-11
	* 2022-07-26
	* 2022-07-27
	* 2022-07-28

**Block: 2, Entry: 6 data points length: 76**
* Heading date: 2022-06-22
	* 2022-05-29
	* *2022-06-11
	* 2022-07-26
	* 2022-07-27
	* 2022-07-28

**Block: 3, Entry: 5 data points length: 68**
* Heading date: 2022-06-21
	* 2022-05-25
	* 2022-05-29
	* 2022-06-04
	* 2022-06-05
	* 2022-06-06
	* 2022-06-07
	* *2022-06-08
	* *2022-06-09
	* *2022-06-10
	* *2022-06-11
	* *2022-06-12
	* *2022-06-13

**Block: 3, Entry: 3 data points length: 68**
* Heading date: 2022-06-20
	* 2022-05-25
	* 2022-05-29
	* 2022-06-04
	* 2022-06-05
	* 2022-06-06
	* *2022-06-07
	* *2022-06-08
	* *2022-06-09
	* *2022-06-10
	* *2022-06-11
	* *2022-06-12
	* *2022-06-13

**Block: 3, Entry: 7 data points length: 68**
* Heading date: 2022-06-20
	* 2022-05-25
	* 2022-05-29
	* 2022-06-04
	* 2022-06-05
	* 2022-06-06
	* *2022-06-07
	* *2022-06-08
	* *2022-06-09
	* *2022-06-10
	* *2022-06-11
	* *2022-06-12
	* *2022-06-13

**Block: 3, Entry: 1 data points length: 68**
* Heading date: 2022-06-22
	* 2022-05-25
	* 2022-05-29
	* 2022-06-04
	* 2022-06-05
	* 2022-06-06
	* 2022-06-07
	* 2022-06-08
	* *2022-06-09
	* *2022-06-10
	* *2022-06-11
	* *2022-06-12
	* *2022-06-13

**Missing all data points for plot Block: 3, Entry: 2**

**Missing all data points for plot Block: 3, Entry: 4**

**Missing all data points for plot Block: 3, Entry: 8**

**Missing all data points for plot Block: 3, Entry: 6**


### Missing Data Points Notes For Sping Wheat:
(Dates with * marker are within 2 weeks of heading date)

**Block: 1, Entry: 9 data points length: 49**
* Heading date: 2022-06-25
	* *2022-06-13
	* *2022-06-14
	* *2022-06-15
	* *2022-06-16
	* *2022-06-17
	* *2022-06-18
	* *2022-06-19
	* *2022-06-20
	* *2022-06-21
	* *2022-06-22
	* *2022-06-23
	* *2022-06-24
	* 2022-07-20

**Block: 1, Entry: 7 data points length: 49**
* Heading date: 2022-06-29
	* 2022-06-13
	* 2022-06-14
	* 2022-06-15
	* *2022-06-16
	* *2022-06-17
	* *2022-06-18
	* *2022-06-19
	* *2022-06-20
	* *2022-06-21
	* *2022-06-22
	* *2022-06-23
	* *2022-06-24
	* 2022-07-20

**Block: 1, Entry: 11 data points length: 49**
* Heading date: 2022-06-30
	* 2022-06-13
	* 2022-06-14
	* 2022-06-15
	* 2022-06-16
	* *2022-06-17
	* *2022-06-18
	* *2022-06-19
	* *2022-06-20
	* *2022-06-21
	* *2022-06-22
	* *2022-06-23
	* *2022-06-24
	* 2022-07-20

**Block: 1, Entry: 3 data points length: 57**
* Heading date: 2022-06-29
	* 2022-06-11
	* 2022-06-13
	* 2022-06-14
	* 2022-08-01

**Block: 1, Entry: 4 data points length: 57**
* Heading date: 2022-06-28
	* 2022-06-11
	* 2022-06-13
	* 2022-06-14
	* 2022-08-01

**Block: 1, Entry: 6 data points length: 57**
* Heading date: 2022-06-25
	* 2022-06-11
	* *2022-06-13
	* *2022-06-14
	* 2022-08-01

**Block: 1, Entry: 8 data points length: 44**
* Heading date: 2022-06-25
	* 2022-06-11
	* *2022-06-13
	* *2022-06-14
	* *2022-06-15
	* 2022-07-21
	* 2022-07-22

**Block: 1, Entry: 12 data points length: 44**
* Heading date: 2022-06-25
	* 2022-06-11
	* *2022-06-13
	* *2022-06-14
	* *2022-06-15
	* 2022-07-21
	* 2022-07-22

**Block: 1, Entry: 2 data points length: 44**
* Heading date: 2022-06-26
	* 2022-06-11
	* *2022-06-13
	* *2022-06-14
	* *2022-06-15
	* 2022-07-21
	* 2022-07-22

**Block: 1, Entry: 5 data points length: 55**
* Heading date: 2022-06-30
	* 2022-06-13
	* 2022-06-15
	* 2022-06-16
	* *2022-06-17
	* *2022-06-25
	* *2022-07-08
	* 2022-07-31

**Block: 1, Entry: 10 data points length: 55**
* Heading date: 2022-07-01
	* 2022-06-13
	* 2022-06-15
	* 2022-06-16
	* 2022-06-17
	* *2022-06-25
	* *2022-07-08
	* 2022-07-31

**Block: 1, Entry: 1 data points length: 55**
* Heading date: 2022-06-24
	* *2022-06-13
	* *2022-06-15
	* *2022-06-16
	* *2022-06-17
	* *2022-06-25
	* 2022-07-08
	* 2022-07-31

**Block: 2, Entry: 11 data points length: 56**
* Heading date: 2022-06-30
	* 2022-06-13
	* 2022-06-14
	* 2022-06-15
	* 2022-06-16
	* *2022-06-17
	* 2022-08-02

**Block: 2, Entry: 7 data points length: 56**
* Heading date: 2022-07-01
	* 2022-06-13
	* 2022-06-14
	* 2022-06-15
	* 2022-06-16
	* 2022-06-17
	* 2022-08-02

**Block: 2, Entry: 4 data points length: 56**
* Heading date: 2022-06-28
	* 2022-06-13
	* 2022-06-14
	* *2022-06-15
	* *2022-06-16
	* *2022-06-17
	* 2022-08-02

**Block: 2, Entry: 9 data points length: 57**
* Heading date: 2022-06-25
	* *2022-06-13
	* *2022-06-14
	* *2022-06-15

**Block: 2, Entry: 6 data points length: 57**
* Heading date: 2022-06-24
	* *2022-06-13
	* *2022-06-14
	* *2022-06-15

**Block: 2, Entry: 8 data points length: 57**
* Heading date: 2022-06-25
	* *2022-06-13
	* *2022-06-14
	* *2022-06-15

**Missing all data points for plot Block: 2, Entry: 12**

**Missing all data points for plot Block: 2, Entry: 5**

**Missing all data points for plot Block: 2, Entry: 3**

**Block: 2, Entry: 10 data points length: 57**
* Heading date: 2022-06-30
	* 2022-06-10
	* 2022-06-11
	* 2022-06-13
	* *2022-07-01
	* *2022-07-02

**Block: 2, Entry: 1 data points length: 57**
* Heading date: 2022-06-26
	* 2022-06-10
	* 2022-06-11
	* *2022-06-13
	* *2022-07-01
	* *2022-07-02

**Block: 2, Entry: 2 data points length: 57**
* Heading date: 2022-06-27
	* 2022-06-10
	* 2022-06-11
	* 2022-06-13
	* *2022-07-01
	* *2022-07-02

**Block: 3, Entry: 2 data points length: 59**
* Heading date: 2022-06-28
	* 2022-06-10
	* 2022-06-11
	* 2022-06-13

**Block: 3, Entry: 11 data points length: 59**
* Heading date: 2022-06-29
	* 2022-06-10
	* 2022-06-11
	* 2022-06-13

**Block: 3, Entry: 3 data points length: 59**
* Heading date: 2022-06-29
	* 2022-06-10
	* 2022-06-11
	* 2022-06-13

**Missing all data points for plot Block: 3, Entry: 12**

**Missing all data points for plot Block: 3, Entry: 9**

**Missing all data points for plot Block: 3, Entry: 4**

**Block: 3, Entry: 7 data points length: 59**
* Heading date: 2022-06-30
	* 2022-06-10
	* 2022-06-11
	* 2022-06-13

**Block: 3, Entry: 1 data points length: 59**
* Heading date: 2022-06-24
	* 2022-06-10
	* *2022-06-11
	* *2022-06-13

**Block: 3, Entry: 5 data points length: 59**
* Heading date: 2022-07-01
	* 2022-06-10
	* 2022-06-11
	* 2022-06-13

**Block: 3, Entry: 10 data points length: 43**
* Heading date: 2022-07-01
	* 2022-06-10
	* 2022-06-11
	* 2022-06-12
	* 2022-06-13
	* 2022-06-14
	* 2022-06-15
	* 2022-06-16
	* 2022-06-17
	* *2022-06-21

**Block: 3, Entry: 8 data points length: 43**
* Heading date: 2022-06-27
	* 2022-06-10
	* 2022-06-11
	* 2022-06-12
	* 2022-06-13
	* *2022-06-14
	* *2022-06-15
	* *2022-06-16
	* *2022-06-17
	* *2022-06-21

**Block: 3, Entry: 6 data points length: 43**
* Heading date: 2022-06-24
	* 2022-06-10
	* *2022-06-11
	* *2022-06-12
	* *2022-06-13
	* *2022-06-14
	* *2022-06-15
	* *2022-06-16
	* *2022-06-17
	* *2022-06-21

### Missing data interpolation techniques
The first technique used to fill the missing data was to pull the data from 
another plot of the same variety. If there was still missing data, then the next technique 
was to pull data from external weather sources nearby (to the site location). If there was still
missing data, then linear interpolation was used.


# References: 
* [1] J. Brownlee, “How to Develop LSTM Models for Time Series Forecasting,” Machine Learning Mastery, Nov. 13, 2018. https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/

* [2] J. Brownlee, “Gentle Introduction to Models for Sequence Prediction with RNNs,” Machine Learning Mastery, Jul. 16, 2017. https://machinelearningmastery.com/models-sequence-prediction-recurrent-neural-networks/
‌
* [3] C. Olah, “Understanding LSTM Networks,” Github.io, Aug. 27, 2015. https://colah.github.io/posts/2015-08-Understanding-LSTMs/

* [4] Liu, G., Zhong, K., Li, H., Chen, T., Wang Y., 2023b. A state of art review on time series forecasting with machine learning for environmental parameters in agricultural greenhouses. Inf. Process. Agric. https://doi.org/10.1016/j.inpa.2022.10.005.


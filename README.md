Border Crossing Report- Insight Code challenge solution:

I. Situation:
The Bureau of Transportation Statistics regularly makes available data on the number of vehicles, equipment, passengers and pedestrians crossing into the United States by land.
    Given:
    Dataset in directory Input: Border_Crossing_Entry_Data.csv


II. Target:
Solution in Python/ Scala/ Java
1. To calculate the total number of times vehicles, equipment, passengers and pedestrians cross the U.S.-Canadian and U.S.-Mexican borders each month.
2. To calculate the running monthly average of total number of crossings for that type of crossing and border.
3. Save output/ result into file "report.csv" in Repository Directory "Output"
4. Tests: "test_1" for testing output format and directory structure using "run_tests.sh"
(?)5. Solution/ code for scalability and full functionality for large datasets


III. Action:
Using Waterfall method, as the requirements are clearly defined and the solution can be completed in short schedule.
(Requirements analysis, System design, Coding/ Implementation, Testing and Deployment)

A. Requirement analysis:

1. Input Dataset

For this challenge, you will be given an input file, Border_Crossing_Entry_Data.csv, that will reside in the top-most input directory of your repository.

The file contains data of the form:

Port Name,State,Port Code,Border,Date,Measure,Value,Location
Derby Line,Vermont,209,US-Canada Border,03/01/2019 12:00:00 AM,Truck Containers Full,6483,POINT (-72.09944 45.005)
Norton,Vermont,211,US-Canada Border,03/01/2019 12:00:00 AM,Trains,19,POINT (-71.79528000000002 45.01)
Calexico,California,2503,US-Mexico Border,03/01/2019 12:00:00 AM,Pedestrians,346158,POINT (-115.49806000000001 32.67889)
Hidalgo,Texas,2305,US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,156891,POINT (-98.26278 26.1)
Frontier,Washington,3020,US-Canada Border,02/01/2019 12:00:00 AM,Truck Containers Empty,1319,POINT (-117.78134000000001 48.910160000000005)
Presidio,Texas,2403,US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,15272,POINT (-104.37167 29.56056)
Eagle Pass,Texas,2303,US-Mexico Border,01/01/2019 12:00:00 AM,Pedestrians,56810,POINT (-100.49917 28.70889)

See the notes from the Bureau of Transportation Statistics for more information on each field.

****
For the purposes of this challenge, you'll want to pay attention to the following fields:

    Border: Designates what border was crossed
    Date: Timestamp indicating month and year of crossing
    Measure: Indicates means, or type, of crossing being measured (e.g., vehicle, equipment, passenger or pedestrian)
    Value: Number of crossings
****

2. Expected Output

Using the input file, you must write a program to

**** Sum the total number of crossings (Value) of each type of vehicle or equipment, or passengers or pedestrians, that crossed the border that month, regardless of what port was used.
**** Calculate the running monthly average of total crossings, rounded to the nearest whole number, for that combination of Border and Measure, or means of crossing.

**** Your program must write the requested output data to a file named report.csv in the top-most output directory of your repository.

For example, given the above input file, the correct output file, report.csv would be:

Border,Date,Measure,Value,Average
US-Mexico Border,03/01/2019 12:00:00 AM,Pedestrians,346158,114487
US-Canada Border,03/01/2019 12:00:00 AM,Truck Containers Full,6483,0
US-Canada Border,03/01/2019 12:00:00 AM,Trains,19,0
US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,172163,56810
US-Canada Border,02/01/2019 12:00:00 AM,Truck Containers Empty,1319,0
US-Mexico Border,01/01/2019 12:00:00 AM,Pedestrians,56810,0

**** The lines should be sorted in descending order by

    Date
    Value (or number of crossings)
    Measure
    Border

The column, Average, is for the running monthly average of total crossings for that border and means of crossing in all previous months. In this example, to calculate the Average for the first line (i.e., running monthly average of total pedestrians crossing the US-Mexico Border in all of the months preceding March), you'd take the average sum of total number of US-Mexico pedestrian crossings in February 156,891 + 15,272 = 172,163 and January 56,810, and round it to the nearest whole number round(228,973/2) = 114,487


B. System Design: Using Python3(no external libraries)/ Scala/ Java.


C. Coding/ implementation:
* read datasets
* DataAnalysis
    * select features required
    * Format/ clean features
    * calculate features required
    * Format features and output dataset as per requirements
* write output in "report.csv" located in "output" directory


D. Testing:
Test_1 in Insight Test environment as well. Test scripts for testing values, formats and directory structure. Test for changing input datasets: in volume and datatypes.


E. Deployment: Submit the link for Github repository for the solutions at  https://app.greenhouse.io/tests/8ca6f4f5a99085bce156b490d88cd85f




IV. Result:


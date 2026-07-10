# Data extraction

The search results for this subjects did not exceed the maximum number of records 
allowed by the Scopus web interface (20,000 records per export). 
The complete dataset for the study period (2008-2025) was exported as a single CSV file. (``<Subject>_1.csv``)
```
SUBJAREA ( MATH ) AND SUBJTERMS ( "Subject" ) AND PUBYEAR > 2007 AND PUBYEAR < 2026
````
To estimate the scientific community growth before the study period, an additional export covering the years 2003-2007 was also performed. (``0_<Subject>_1.csv``)
```
SUBJAREA ( MATH ) AND SUBJTERMS ( "Subject" ) AND PUBYEAR > 2002 AND PUBYEAR < 2008
````

| Subject | Exported files |
|---------|----------------|
| Algebra and number theory| ``0_Algebra_and_Number_Theory_1.csv``, ``Algebra_and_Number_Theory_1.csv`` |
| Computational mathematics | ``0_Computational_Mathematics_1.csv``, ``Computational_Mathematics_1.csv``|
| Geometry and topology | ``0_Geometry_and_Topology_1.csv``, ``Geometry_and_Topology_1.csv``|
| Miscellaneous | ``0_Miscellaneous_1.csv``, ``Miscellaneous_1.csv``|

All subjects in this document were using the same methodology.

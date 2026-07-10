# Data extraction

The search results for this subjects exceeded the maximum number of records that can be exported from the Scopus web interface (20,000 records per export).
Therefore, the results were divided into publication-year intervals, ensuring that export remained below the export limit. (``<Subject>_1.csv``)
```
SUBJAREA ( MATH ) AND SUBJTERMS ( "Subject" ) AND PUBYEAR > 2007 AND PUBYEAR < 2026
````
To estimate the scientific community growth before the study period, an additional export covering the years 2003-2007 was also performed. (``0_<Subject>_1.csv``)
```
SUBJAREA ( MATH ) AND SUBJTERMS ( "Subject" ) AND PUBYEAR > 2002 AND PUBYEAR < 2008
````
## Analysis
| Query | Years | File |
|-------|-------|------|
| ``SUBJAREA(MATH) AND SUBJTERMS("Analysis") AND PUBYEAR > 2002 AND PUBYEAR < 2008`` | 2003-2007 | ``0_Analysis_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Analysis") AND PUBYEAR > 2007 AND PUBYEAR < 2014`` | 2008-2013 | ``Analysis_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Analysis") AND PUBYEAR > 2013 AND PUBYEAR < 2018`` | 2014-2017 | ``Analysis_2.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Analysis") AND PUBYEAR > 2017 AND PUBYEAR < 2021`` | 2018-2020 | ``Analysis_3.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Analysis") AND PUBYEAR > 2020 AND PUBYEAR < 2022`` | 2021 | ``Analysis_4.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Analysis") AND PUBYEAR > 2021 AND PUBYEAR < 2023`` | 2022 | ``Analysis_5.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Analysis") AND PUBYEAR > 2022 AND PUBYEAR < 2024`` | 2023 | ``Analysis_6.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Analysis") AND PUBYEAR > 2023 AND PUBYEAR < 2025`` | 2024 | ``Analysis_7.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Analysis") AND PUBYEAR > 2024 AND PUBYEAR < 2026 AND (EXCLUDE( DOCTYPE , "ar"))`` | 2025 | ``Analysis_8.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Analysis") AND PUBYEAR > 2024 AND PUBYEAR < 2026 AND (LIMIT-TO( DOCTYPE , "ar"))`` | 2025 | ``Analysis_9.csv`` |

## Applied Mathematics
| Query | Years | File |
|-------|-------|------|
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2002 AND PUBYEAR < 2005`` | 2003-2004 | ``0_Applied_Mathematics_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2004 AND PUBYEAR < 2007`` | 2005-2006 | ``0_Applied_Mathematics_2.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2006 AND PUBYEAR < 2008`` | 2007 | ``0_Applied_Mathematics_3.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2007 AND PUBYEAR < 2014`` | 2008 | ``Applied_Mathematics_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2008 AND PUBYEAR < 2010 AND (EXCLUDE( DOCTYPE , "cp"))`` | 2009 | ``Applied_Mathematics_2.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2008 AND PUBYEAR < 2010 AND (LIMIT-TO( DOCTYPE , "cp"))`` | 2009 | ``Applied_Mathematics_3.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2009 AND PUBYEAR < 2011 AND (EXCLUDE( DOCTYPE , "cp"))`` | 2010 | ``Applied_Mathematics_4.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2009 AND PUBYEAR < 2011 AND (LIMIT-TO( DOCTYPE , "cp"))`` | 2010 | ``Applied_Mathematics_5.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2010 AND PUBYEAR < 2012 AND (EXCLUDE( DOCTYPE , "cp"))`` | 2011 | ``Applied_Mathematics_6.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2010 AND PUBYEAR < 2012 AND (LIMIT-TO( DOCTYPE , "cp"))`` | 2011 | ``Applied_Mathematics_7.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2011 AND PUBYEAR < 2013 AND (EXCLUDE( DOCTYPE , "cp"))`` | 2012 | ``Applied_Mathematics_8.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2011 AND PUBYEAR < 2013 AND (LIMIT-TO( DOCTYPE , "cp"))`` | 2012 | ``Applied_Mathematics_9.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2012 AND PUBYEAR < 2014 AND (EXCLUDE( DOCTYPE , "cp"))`` | 2013 | ``Applied_Mathematics_10.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2012 AND PUBYEAR < 2014 AND (LIMIT-TO( DOCTYPE , "cp"))`` | 2013 | ``Applied_Mathematics_11.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2013 AND PUBYEAR < 2015 AND (EXCLUDE( DOCTYPE , "cp"))`` | 2014 | ``Applied_Mathematics_12.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2013 AND PUBYEAR < 2015 AND (LIMIT-TO( DOCTYPE , "cp"))`` | 2014 | ``Applied_Mathematics_13.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2014 AND PUBYEAR < 2016`` | 2015 | ``Applied_Mathematics_14.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2015 AND PUBYEAR < 2017`` | 2016 | ``Applied_Mathematics_15.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2016 AND PUBYEAR < 2018`` | 2017 | ``Applied_Mathematics_16.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2017 AND PUBYEAR < 2019`` | 2018 | ``Applied_Mathematics_17.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2018 AND PUBYEAR < 2020`` | 2019 | ``Applied_Mathematics_18.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2019 AND PUBYEAR < 2021`` | 2020 | ``Applied_Mathematics_19.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Applied Mathematics") AND PUBYEAR > 2020 AND PUBYEAR < 2026`` | 2021-25 | ``Applied_Mathematics_20.csv`` |

## Discrete Mathematics and Combinatorics
| Query | Years | File |
|-------|-------|------|
| ``SUBJAREA(MATH) AND SUBJTERMS("Discrete Mathematics and Combinatorics") AND PUBYEAR > 2002 AND PUBYEAR < 2008`` | 2003-2007 | ``0_Discrete_Mathematics_and_Combinatorics_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Discrete Mathematics and Combinatorics") AND PUBYEAR > 2007 AND PUBYEAR < 2025`` | 2008-2024 | ``Discrete_Mathematics_and_Combinatorics_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Discrete Mathematics and Combinatorics") AND PUBYEAR > 2024 AND PUBYEAR < 2026`` | 2025 | ``Discrete_Mathematics_and_Combinatorics_2.csv`` |

## Logic
| Query | Years | File |
|-------|-------|------|
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2002 AND PUBYEAR < 2006`` | 2003-2005 | ``0_Logic_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2005 AND PUBYEAR < 2008`` | 2006-2007 | ``0_Logic_2.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2007 AND PUBYEAR < 2010`` | 2008-2009 | ``Logic_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2009 AND PUBYEAR < 2012`` | 2010-2011 | ``Logic_2.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2011 AND PUBYEAR < 2014`` | 2012-2013 | ``Logic_3.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2013 AND PUBYEAR < 2016`` | 2014-2015 | ``Logic_4.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2015 AND PUBYEAR < 2018`` | 2016-2017 | ``Logic_5.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2017 AND PUBYEAR < 2020`` | 2018-2019 | ``Logic_6.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2019 AND PUBYEAR < 2022`` | 2020-2021 | ``Logic_7.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2021 AND PUBYEAR < 2023`` | 2022 | ``Logic_8.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2022 AND PUBYEAR < 2024`` | 2023 | ``Logic_9.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2023 AND PUBYEAR < 2025`` | 2024 | ``Logic_10.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Logic") AND PUBYEAR > 2024 AND PUBYEAR < 2026`` | 2025 | ``Logic_11.csv`` |

## Probability
| Query | Years | File |
|-------|-------|------|
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2002 AND PUBYEAR < 2008`` | 2003-2007 | ``0_Probability_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2007 AND PUBYEAR < 2011`` | 2008-2010 | ``Probability_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2010 AND PUBYEAR < 2013`` | 2011-2012 | ``Probability_2.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2012 AND PUBYEAR < 2015`` | 2013-2014 | ``Probability_3.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2014 AND PUBYEAR < 2017`` | 2015-2016 | ``Probability_4.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2016 AND PUBYEAR < 2019`` | 2017-2018 | ``Probability_5.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2018 AND PUBYEAR < 2020`` | 2019 | ``Probability_6.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2019 AND PUBYEAR < 2021`` | 2020 | ``Probability_7.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2020 AND PUBYEAR < 2022`` | 2021 | ``Probability_8.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2021 AND PUBYEAR < 2023`` | 2022 | ``Probability_9.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2022 AND PUBYEAR < 2024`` | 2023 | ``Probability_10.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2023 AND PUBYEAR < 2025`` | 2024 | ``Probability_11.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Probability") AND PUBYEAR > 2024 AND PUBYEAR < 2026`` | 2025 | ``Probability_12.csv`` |

## Statistics
| Query | Years | File |
|-------|-------|------|
| ``SUBJAREA(MATH) AND SUBJTERMS("Statistics") AND PUBYEAR > 2002 AND PUBYEAR < 2008`` | 2003-2007 | ``0_Statistics_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Statistics") AND PUBYEAR > 2007 AND PUBYEAR < 2011`` | 2008-2010 | ``Statistics_1.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Statistics") AND PUBYEAR > 2010 AND PUBYEAR < 2014`` | 2011-2013 | ``Statistics_2.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Statistics") AND PUBYEAR > 2013 AND PUBYEAR < 2017`` | 2014-2016 | ``Statistics_3.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Statistics") AND PUBYEAR > 2016 AND PUBYEAR < 2019`` | 2017-2018 | ``Statistics_4.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Statistics") AND PUBYEAR > 2018 AND PUBYEAR < 2021`` | 2019-2020 | ``Statistics_5.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Statistics") AND PUBYEAR > 2020 AND PUBYEAR < 2022`` | 2021 | ``Statistics_6.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Statistics") AND PUBYEAR > 2021 AND PUBYEAR < 2023`` | 2022 | ``Statistics_7.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Statistics") AND PUBYEAR > 2022 AND PUBYEAR < 2024`` | 2023 | ``Statistics_8.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Statistics") AND PUBYEAR > 2023 AND PUBYEAR < 2025`` | 2024 | ``Statistics_9.csv`` |
| ``SUBJAREA(MATH) AND SUBJTERMS("Statistics") AND PUBYEAR > 2024 AND PUBYEAR < 2026`` | 2025 | ``Statistics_10.csv`` |





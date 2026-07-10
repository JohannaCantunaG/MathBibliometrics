# Data 
This repository does not include the original Scopus data due to Elsevier's licensing restrictions.
Create the following directory structure:

```text
data/
├── Algebra_and_Number_Theory/
    ├── Algebra_and_Number_Theory_1.csv
├── Analysis/
├── Applied_Mathematics/
├── ...
└── Statistics/
```
Place every CSV exported from Scopus inside its correspongind subject folder.
The preprocessing scripts automatically merge all CSV files found within each subject directory.

Further details about the Scopus search strategy are available in the `queries/` directory.
## Reproducibility note 

Scopus is a dynamic database that is continuously update. Consequently, executing the same search query at a different date may return a different number of records due to newly indexed publications, metadata corrections, or database updates. 
Therefore, the exact number of retrieved records may differ from those used in this study. 

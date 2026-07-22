# A bibliometric study of scientific production in mathematics
This repository contains the code used to reproduce the bibliometric analyses presented in our study on the evolution of Mathematics research based on the Scopus database. The repository includes data preprocessing, bibliometric indicators, growth-model fitting, community analyses, Bradford's low analyses, country analyses, and figure generation. 

The analysis pipeline is organized into reusable modules for data loading, bibliometric indicators, model fitting, and visualization. 

## Repository structure
```text
data/
  Instructions for organizing Scopus exports.

src/
  Python modules implementing the analysis. 

Bibliometric_Analysis.ipynb
  Main notebook reproducing all analyses and figures. 

Country_dic_types.ipynb
  Notebook used to build and validate the country dictionary. 
```
## Data

The original Scopus records are not distributed because they are subject to Elsevier's License.
Intructions for downloading the data are available in:  `data/queries/`

## Reproducibility

The complete analysis can be reproduced by executing `Bibliometric_Analysis.ipynb`
after organizing the Scopus CSV exports as described in `data/README.md`.

## Related publication
The manuscript is currently under review. The citation will be update once the paper become available.

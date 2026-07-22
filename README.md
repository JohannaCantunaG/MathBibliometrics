# A bibliometric study of scientific production in Mathematics

This repository contains the code used to reproduce the bibliometric analyses presented in our study on the evolution of Mathematics research based on the Scopus database. This includes data preprocessing, bibliometric indicators, growth-model fitting, community analyses, Bradford's law analyses, country analyses, and figure generation.

The analysis pipeline is organized into reusable modules for data loading, bibliometric indicator computation, model fitting, and visualization.

## Example results
The repository reproduces all figures presented in the manuscript. 

### Publication growth 

![Publication growth](figures/Fields0825CumAnnualCombined.pdf)
Growth of scientific production across the eleven Mathematics subject areas. 

### Bradford's law

![Bradford](figures/Bradfordmath.pdf)

Bradford's law fitted to the cumulative journal productivity in Mathematics. 

## Repository structure
```text
data/
  Instructions for organizing Scopus exports.

src/
  Python modules implementing the analysis. 

Bibliometric_Analysis.ipynb
  Main notebook reproducing all analyses and figures. 

country_dic_types.ipynb
  Notebook used to build and validate the country dictionary. 
```
## Data

The original Scopus records are not distributed because they are subject to Elsevier's License.
Intructions for downloading the data are available in:  `data/README.md`

## Reproducibility

The complete analysis can be reproduced by executing `Bibliometric_Analysis.ipynb`
after organizing the Scopus CSV exports as described in `data/README.md`.

Scopus is a continuously update database. Therefore, executing the same search queries at a different date may produce slightly different retrieval counts due to newly indexed publications, metadata corrections, and database updates.

For additional information about Scopus coverage and updates, see the official Scopus Content Coverage Guide. 

## Related publication
The manuscript is currently under review. The citation will be updated once the paper become available.

## License
This project is distributed under the MIT License. 

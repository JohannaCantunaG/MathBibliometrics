# BibliometricAnalysis

## Data collection 

This repository does not include the raw Scopus data, as they are subject to Elsevier's licensing restrictions.

The bibliographic records were manually exported from the Scopus web interface using an institutional subscription. 

### Search strategy 

The following query was used as the base search:

```text
SUBJAREA(MATH) AND SUBJTERMS("FIELD") AND PUBYEAR > 2007 AND PUBYEAR < 2026
```

where `FIELD` should be replaced by the corresponding Mathematics subject (e.g, Logic, Statistics, etc.)

### Export procedure

Since the Scopus web interface limits each export to a maximum of 20,000 records, the search results were divided into smaller subsets by publication year (or ranges of years when appropriate). Each subset was exported separately as a CSV file.

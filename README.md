# Bootstrap Split Freqs Script

- Needs dendropy (and mafft/trimal/iqtree to quick the tree generation script) e.g. `conda create -n bootstrap_splits -c bioconda -c conda-forge dendropy mafft iqtree trimal`

- Activate your env `conda activate bootstrap_splits` and then you can run with `python get_bootstrap_split_frequencies.py tree/mcr.masked.afa.boottrees` (test data was just done with 10 non-parametric bootstraps, you'll want to increase this!). 

- Lots of useful functions to extend this e.g., [splits missing in ML tree](https://dendropy.org/library/treecompare.html?highlight=bipartitions#dendropy.calculate.treecompare.find_missing_bipartitions) 
or more specific [explicit symmetric differences](https://dendropy.org/_modules/dendropy/calculate/treecompare.html#symmetric_difference)

- See dendropy [documentation](https://dendropy.org/primer/bipartitions.html) for far more details

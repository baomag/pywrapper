#!/usr/bin/env bash

# echo all commands
set -x
outdir=$(mrrdir.sh)
barcode=/storage/singlecell/jeanl/organoid/data/D45_organoid_Sridhar/D45_organoid/outs/filtered_feature_bc_matrix/barcodes.tsv.gz
bam=/storage/singlecell/jeanl/organoid/data/D45_organoid_Sridhar/D45_organoid/outs/possorted_genome_bam.bam
genome=/storage/singlecell/zz4/Reference/refdata-cellranger-arc-GRCh38-2020-A/genes/genes.gtf

export TMPDIR=$outdir
slurmtaco.sh -n d03 -- python ../velocytorun.py -e velocyto -d "$outdir" -b test -c "$barcode" -g "$genome" -t 8 -- "$bam"

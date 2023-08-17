#!/bin/bash
#SBATCH --job-name=tmp.PY6ctmaD1H
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem=2G
#SBATCH --time=7-00:00:00
#SBATCH --nodelist=mhgcp-g01
#SBATCH -o out_slurm/tmp.PY6ctmaD1H-%j.out
#SBATCH -e out_slurm/tmp.PY6ctmaD1H-%j.err

start=$(date +%s)
echo "starting at $(date) on $(hostname)"

# Print the SLURM job ID.
echo "SLURM_JOBID=$SLURM_JOBID"

# Run the application
python ../velocytorun.py -e velocyto -d /storage/singlecell/maggie/pywrapper/src/velocytorun/main -b test -c /storage/singlecell/jeanl/organoid/data/D45_organoid_Sridhar/D45_organoid/outs/filtered_feature_bc_matrix/barcodes.tsv.gz -g /storage/singlecell/zz4/Reference/refdata-cellranger-arc-GRCh38-2020-A/genes/genes.gtf -t 8 -- /storage/singlecell/jeanl/organoid/data/D45_organoid_Sridhar/D45_organoid/outs/possorted_genome_bam.bam

end=$(date +%s)
echo "ended at $(date) on $(hostname). Time elapsed: $(date -u -d @$((end-start)) +'%H:%M:%S')"
exit 0

#!/usr/bin/env python3
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import os
import sys
from exeBash.exeBash import exeBash
from pathlib import Path
import click

CONTEXT_SETTINGS=dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--outdir', type=click.Path(resolve_path=True), default='.', show_default=True, help='Outdir.')
@click.option('-b', '--bname', type=click.STRING, required=True, help='Bname.')
@click.option('-e', '--condaenv', type=click.STRING, help='Conda environment.')
@click.option('-c', '--barcode', type=click.Path(exists=True), required=True, help='Valid barcode.')
@click.option('-g', '--gtf', type=click.Path(exists=True), required=True, help='GTF.')
@click.option('-t', '--numthreads', type=click.INT, default=8, help='Number of threads.')
@click.argument('infile', type=click.Path(exists=True, resolve_path=True))
def main(outdir, bname, condaenv, barcode, gtf, numthreads, infile):
	"""
Run velocyto function to calculate RNA velocity.

INFILE is the BAM file.
OUTFILE is LOOM file.

\b
Example:
 bname=D45_organoid_Sridhar
 barcode=/storage/singlecell/jeanl/organoid/data/D45_organoid_Sridhar/D45_organoid/outs/filtered_feature_bc_matrix/barcodes.tsv.gz
 ban=/storage/singlecell/jeanl/organoid/data/D45_organoid_Sridhar/D45_organoid/outs/possorted_genome_bam.bam
  velocytorun -d "$outdir" -b "$bname" -e velocyto -c "$barcode" -g /storage/singlecell/zz4/Reference/refdata-cellranger-arc-GRCh38-2020-A/genes/genes.gtf -t 8 -- xx.bam

\b
Note:
 Samtools may produce temporary files and requires writing access of input directory
 To solve this, create a temporary copy of the input files to the working directory and delete it at the end of the code

\b
See also:
  Depends:
    Velocyto

\b
Date: 2023/08/23
Authors: Yourong Bao <maggiemaizibao@gmail.com>
"""
	Path(f"{outdir}/{bname}").mkdir(parents=True, exist_ok=True)
	inbname=Path(infile).name
	tmpfile=Path(outdir) / bname / inbname
	# lnfile.hardlink_to(infile)
	# os.chdir(outdir)
	exprs=[
		f"cp {infile} {tmpfile};",
		f"cp {infile}.bai {tmpfile}.bai;",
		f"velocyto run",
		f"-o '{outdir}/{bname}'",
		f"-b '{barcode}'",
		f"-@ {numthreads}",
		f"'{tmpfile}'",
		f"'{gtf}';",
		f"rm -f {tmpfile} {tmpfile}.bai;",
		]
	return exeBash.callback(exprs, condaenv=condaenv, verbose=True)

if __name__ == "__main__":
	sys.exit(main())

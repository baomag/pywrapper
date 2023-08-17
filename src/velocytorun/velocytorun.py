#!/usr/bin/env python3
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import os
import sys
from exeBash.exeBash import exeBash
from pathlib import Path
import click

CONTEXT_SETTINGS=dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--outdir', type=click.Path(), default='.', show_default=True, help='Outdir.')
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

\b
Example:
  velocytorun -d "$outdir" -b "$bname" -- xx.bam

\b
Note:
  1. 

\b
See also:
  Depends:
    Velocyto

\b
Date: 2023/08/17
Authors: Yourong Bao <maggiemaizibao@gmail.com>
"""
	Path(outdir).mkdir(parents=True, exist_ok=True)
	absdir=Path(__file__).parent
	scriptname=Path(__file__).stem
	# os.chdir(outdir)
	exprs=[
		# f"ln -s {infile} {outdir};",
		f"velocyto run",
		f"-o '{outdir}/{bname}'",
		f"-b '{barcode}'",
		f"-@ {numthreads}",
		f"'{infile}'",
		f"'{gtf}'",
		]
	return exeBash.callback(exprs, condaenv=condaenv, verbose=True)

if __name__ == "__main__":
	sys.exit(main())

#!/u_sr/bin/env python3
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import os
import sys
from exePython.exePython import exePython
from pathlib import Path
import click

CONTEXT_SETTINGS=dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--outdir', type=click.Path(resolve_path=True), default='.', show_default=True, help='Outdir.')
@click.option('-b', '--bname', type=click.STRING, required=True, help='Bname.')
@click.option('-e', '--condaenv', type=click.STRING, help='Conda environment.')
@click.option('-t', '--numthreads', type=click.INT, default=8, help='Number of threads.')
@click.argument('infile', type=click.Path(exists=True, resolve_path=True))
def main(outdir, bname, condaenv, numthreads, infile):
	"""
Convert loom file to h5ad file.

INFILE is the loom file.
OUTFILE is the h5ad file.

\b
Example:

\b
Note:
  Simply read in the loom file and write the h5ad file
  Loom files can be read by scanpy directly or can be read using anndata package

\b
See also:
  Depends:
	  Python/Scanpy

\b
Date: 2023/08/25
Authors: Yourong Bao <maggiemaizibao@gmail.com>
"""
	absdir=Path(__file__).parent
	scriptname=Path(__file__).stem
	script=f'{absdir}/python/{scriptname}.py'
	exprs=[
		f"-o '{outdir}/{bname}'",
		f"-b '{barcode}'"],
		f"-@ {numthreads}",
		f"'{tmpfile}'",
		f"'{gtf}';",
		f"rm -f {tmpfile} {tmpfile}.bai;",
		]
	return exeBash.callback(exprs, condaenv=condaenv, verbose=True)

if __name__ == "__main__":
	sys.exit(main())

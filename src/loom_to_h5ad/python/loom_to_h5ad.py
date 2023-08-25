import numpy as np
import pandas as pd
import scanpy as sc

ldata = sc.read_loom(infile)
ldata.obs.index = [x.split(":", 1)[0] + "_" + x.split(":", 1)[1][:-1] + "-1" for x in ldata.obs.index]
ldata.write(paste(outdir,bname,".h5ad"))

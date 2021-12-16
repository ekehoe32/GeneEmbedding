"""Testing module for sra module."""

import os
import pandas as pd
from pyrpipe import assembly
from pyrpipe.mapping import Star
from pyrpipe.qc import Trimgalore
from pyrpipe.assembly import Stringtie
from gembed.sra import ProcessSRA


# set run id
run_id = 'SRR8052833'

# set genome directory and paths
genome_dir = '/home/ekehoe/Gene2vec/genome/'
gen = os.path.join(genome_dir, 'GCF_000001405.39_GRCh38.p13_genomic.fna')
ann = os.path.join(genome_dir,'GCF_000001405.39_GRCh38.p13_genomic.gtf')
star_index = os.path.join(genome_dir, 'STAR')

# set working directory
working_dir = "/home/ekehoe/GeneEmbedding/Test/"

# set metadata
metadata = pd.read_csv("/home/ekehoe/NCBIQueries/ADSRARunTable.csv")

# set aligner
star = Star(index=star_index,genome=gen,threads=4)

# set trimmer
trim_galore = Trimgalore()

# set assembler
stringtie = Stringtie(guide=ann)

p = ProcessSRA(metadata=metadata,
                aligner=star, 
                qc=trim_galore, 
                assembly=stringtie, 
                working_dir=working_dir)


# process a run
p.process_run(run_id)
pass
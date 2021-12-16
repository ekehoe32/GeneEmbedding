"""This module contains classes and functions for automating scraping and proccessing of SRA datasets from NCBI"""

from dataclasses import dataclass, field
from pandas import DataFrame
from pyrpipe import assembly
from pyrpipe.mapping import Aligner
from pyrpipe.qc import RNASeqQC
from pyrpipe.assembly import Assembly
from pyrpipe.sra import SRA

@dataclass
class ProcessSRA:
    """Generates processed datasets from a metadata file of SRA runs."""
    
    # parameters
    metadata: DataFrame = field(compare=False, repr=False)
    aligner: Aligner = field(compare=False)
    qc: RNASeqQC = field(compare=False)
    assembly: Assembly = field(compare=False)
    working_dir: str = field(default="./", compare=False, repr=False)

    def __post_init__(self):

        # attributes
        self.sra_lib: dict = self._generate_sra_lib()

    def _generate_sra_lib(self) -> dict:
        """Generates a dictionary containing sra runs indexed by sra."""

        # extract SRA and SRR from metadata 
        df = self.metadata.filter(regex="Run|SRA").groupby("SRA Study").agg(list).reset_index()
        kv = dict(zip(df["SRA Study"], df["Run"]))

        return kv

    def process_run(self, run_id: str):
        """Processes a single run."""

        # check if run is in the metadata
        assert run_id in self.metadata["Run"].values,\
             "Run ID %s not contained in the metadata!" % run_id

        # run the pipeline
        srr_object= SRA(run_id, directory=self.working_dir)
        
        #create a pipeline using the objects
        srr_object.trim(self.qc).align(self.aligner).assemble(self.assembly)




    
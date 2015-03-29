# Aligns sequences on file opuntia.fasta
import os # needed for running commands
from Bio.Align.Applications import ClustalwCommandline
#  in windows clustalw_exe = r"C:\Program Files\Clustalw\clustalw2.exe"
clustalw_exe="/usr/bin/clustalw" # in my  linux
assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
clustalw_cline = ClustalwCommandline(clustalw_exe, infile="opuntia.fasta")
stdout, stderr = clustalw_cline() # Runs command line
# and creates files opuntia.aln and opuntia.dnd 

# Opens alignment
from Bio import AlignIO
align = AlignIO.read("opuntia.aln", "clustal")
print align

# phylogenetic tree:
from Bio import Phylo
tree = Phylo.read("opuntia.dnd", "newick")
Phylo.draw_ascii(tree)



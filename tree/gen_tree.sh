#!/bin/bash

mafft --auto mcr.fasta > mcr.afa
trimal -in mcr.afa -out mcr.masked.afa -automated1
iqtree -m LG+G -s mcr.masked.afa --boot 10

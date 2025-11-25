#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script generates Jupyter notebooks for pYPKa_Z and pYPKa_E vectors
# for the yeast pathway kit.
#
# This script reads a text file called tp_list.txt which has this format:
#
# name    RE   fp    rp    comment
#
# RPL11B  Z    646   645   OK
#
# the first element is a name which has to be a standard or systematic name
# of a gene in Saccharomyces cerevisiae uppercase or lowercase.
#
# RE is the restriction enzyme used (EcoRV or ZraI).
#
# fp and rp are primers used for the amplification. The numbers refer to
# number in a primer list.
#
# comment can be any text.
# two files are copied to the destination directory
# - pYPKa.gb
# - standard_primers.txt
#

from pydna.myprimers import PrimerList
from pydna.dseqrecord import Dseqrecord
from pydna.amplify import pcr
from Bio.Restriction import ZraI, EcoRV
from pygenome import saccharomyces_cerevisiae as sg
import nbformat
from nbconvert.preprocessors.execute import ExecutePreprocessor

import notedown
from pydna.readers import read
import os
import shutil
from pathlib import Path

cwd = os.getcwd()

outpath = Path.cwd()/"nb"  # Path(cwd).parent.joinpath("pYPKa_ZE2")

outpath.mkdir(parents=True, exist_ok=True)

shutil.copy("pYPKa.gb", outpath)
shutil.copy("standard_primers.txt", outpath)
shutil.copy("figure_pYPKa_ZE.png", outpath)

pYPKa = read("pYPKa.gb")

with open("notebook_template_pYPKa_ZE.md", "r", encoding="utf8") as f:
    t=f.read()

with open("tp_list.txt", "r") as f:
    tps = [l for l in f.read().splitlines() if l and not l.strip().startswith("#")]

tp_dict = {}

lp = PrimerList()



for insertname, letter, pf, pr, comment in ( x.split(maxsplit=4) for x in tps if x ):

    try:
        old = tp_dict[insertname]
    except KeyError:
        tp_dict[insertname] = (pf, pr, comment)
    else:
        assert (old[0], old[1]) == (pf, pr)

#os.chdir(outpath)

for insertname in sorted(tp_dict):

    newname = os.path.join(outpath, "pYPKa_ZE_{}.ipynb".format(insertname))

    if os.path.exists(newname): continue

    try:
        p = sg.stdgenes[insertname]
    except KeyError:
        try:
            p = sg.sysgenes[insertname]
        except KeyError:
            raise ValueError('No gene by that name in S.c.')

    pf, pr, comment = tp_dict[insertname]

    print(insertname, pf, pr, comment)

    fp = lp[int(pf)]
    rp = lp[int(pr)]

    gbref  = p.promoter().description
    gblink = p.cds().id

    template = Dseqrecord(p.promoter())

    templatesize = len(template)
    insertseguid = template.seguid()

    finalcseguidZ = (pYPKa.linearize(ZraI)+pcr(fp, rp, template)).looped().cseguid()
    finalcseguidE = (pYPKa.linearize(EcoRV)+pcr(fp, rp, template)).looped().cseguid()

    content =  t.format( tp                = insertname,
                         gbref             = gbref,
                         gblink            = gblink,
                         templatesize      = templatesize,
                         insertseguid      = insertseguid,
                         finalcseguidZ     = finalcseguidZ,
                         finalcseguidE     = finalcseguidE,
                         fpn=fp.name,
                         fps=fp.seq,
                         rpn=rp.name,
                         rps=rp.seq)



    obj = notedown.MarkdownReader()

    nb = obj.to_notebook(content)

    pp = ExecutePreprocessor(timeout=600, kernel_name='python3')
    pp.timeout = 120 # seconds
    pp.interrupt_on_timeout = True

    pp.preprocess(nb, resources={})

    with open(newname, 'wt') as f:
        nbformat.write(nb, f)

#os.chdir(cwd)

# with open("README_template.md", "r", encoding="utf8") as f:
#     t=f.read()

# table = "| No. | TP | Promoter vector | Terminator vector | Jupyter nb |\n"
# table+= "|-----|----|-----------------|-------------------|------------|\n"

# for no, ins in enumerate(sorted(tp_dict)):
#     fld = "pYPKa_ZE"
#     row = f"|{no} |{ins} | [pYPKa_Z_{ins}.gb]({fld}/pYPKa_Z_{ins}.gb) | [pYPKa_E_{ins}.gb]({fld}/pYPKa_E_{ins}.gb) | [nb]({fld}/pYPKa_ZE_{ins}.ipynb) |\n"
#     table+=row


# readme = t.format(number_of_tps = len( tp_dict.keys() ), number_of_vectors= len(tp_dict), table=table)


# with open("../README.md", "w", encoding="utf8") as f:
#     f.write(readme)



#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
import logging
import argparse

LOG = logging.getLogger(__name__)

__version__ = "1.0.1"
__author__ = ("Xingguo Zhang",)
__email__ = "invicoun@foxmail.com"
__all__ = []


def format_argannot(seqid):

    seqid = seqid.split()[0]
    db, gene, gbid = seqid.split("~~~", 2)
    gene = gene.split(")")
    seqid = ">%s%s) %s" % (gene[0], gene[1], gbid)

    return seqid


def format_card(seqid):

    seqid = seqid.split("~~~")
    seqid = ">%s" % " ".join(seqid[1::])

    return seqid


def format_megares(seqid):

    seqid= seqid.split("~~~")
    seqid = ">%s(%s) %s" % (seqid[2], seqid[1], seqid[3])

    return seqid


def format_ncbi(seqid):

    seqid= seqid.split("~~~")
    seqid = ">%s" % " ".join(seqid[1::])

    return seqid


def format_plasmidfinder(seqid):

    seqid= seqid.split("~~~")
    seqid = ">%s %s" % (seqid[1], seqid[2])

    return seqid


def abricate_seq2format(file):

    for line in open(file):
        line = line.strip()

        if not line:
            continue
        if line.startswith(">argannot"):
            print(format_argannot(line))
        elif line.startswith(">card~~~"):
            print(format_card(line))
        elif line.startswith(">megares~~~"):
            print(format_megares(line))
        elif line.startswith(">ncbi~~~"):
            print(format_ncbi(line))
        elif line.startswith(">plasmidfinder~~~"):
            print(format_plasmidfinder(line))
        else:
            print(line)

    return 0


def add_hlep_args(parser):

    parser.add_argument("input", metavar="FILE", type=str,
        help="Input the fasta,(fasta)")

    return parser


def main():

    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
        format="[%(levelname)s] %(message)s"
    )
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
For exmple:
        abricate_seq2format.py OXA.fasta > OXA_new.fasta

version: %s
contact:  %s <%s>\
    ''' % (__version__, " ".join(__author__), __email__))

    args = add_hlep_args(parser).parse_args()

    abricate_seq2format(args.input)


if __name__ == "__main__":

    main()

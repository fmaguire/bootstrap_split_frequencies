#!/usr/bin/env python

import argparse
import collections
import dendropy

def get_boot_splits_proportions(boot_tree_path):
    """
    Quickly generate all bipartitions in a set of IQTree boot-trees (newick formatted)

    - boot_tree_path: filepath to file containing boot trees
    """

    treelist = dendropy.TreeList()
    treelist.read_from_path(boot_tree_path, schema="newick")

    # chuck all the splits into a big ole list (not pretty or efficient)
    splits = []
    for tree in treelist:
        tree_splits = [split.split_as_newick_string(treelist.taxon_namespace) \
                        for split in tree.encode_bipartitions()]
        splits += tree_splits

    # let collections Counter object tally up the number of times each split
    # appears in the list
    split_counts = collections.Counter(splits)

    # normalise by the number of trees in the boottree file
    split_freqs = {k: v/len(treelist) for k,v in split_counts.items()}

    return split_counts, split_freqs


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=\
                                        'Quickly get split frequencies for a set'
                                        ' of IQTree/newick non-parametric '
                                        ' bootstrap trees')
    parser.add_argument('boot_tree_path', type=str,
                        help='Path to file containing newick boot-trees')

    args = parser.parse_args()

    split_counts, split_freqs = get_boot_splits_proportions(args.boot_tree_path)

    for split, freq in split_freqs.items():
        print(split, freq)

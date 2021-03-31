#! /bin/bash

set -e

dir=$PWD

# These are the folders to be modified when creating the cleared versions
# folder=../questions/CS/MarkovChainGroupActivity/MarkovChains-Intro
folder=../questions/CS/MarkovChainGroupActivity/MarkovChains-Gambler

# copy all section files to the cleared directory
# copy only if newer
rsync -q -r -u $folder/serverFilesQuestion/ $folder/serverFilesQuestion/cleared/

# go to the folder in the cleared directory
# clear marked cells and their output
cd $folder/serverFilesQuestion/cleared/
for f in *.ipynb; do
    # remove cells with clear
    $dir/prepare-ipynb clear-marked-add-grade-key clear-output "$f" "$f"
done
cd $dir

echo "[[... syncing $folder/serverFilesQuestion/cleared/ with $folder/workspace ...]]"

# copy all section files to the upload directory
# copy only if newer
rsync -q -r -u $folder/serverFilesQuestion/cleared/ $folder/workspace

rm -r $folder/serverFilesQuestion/cleared/

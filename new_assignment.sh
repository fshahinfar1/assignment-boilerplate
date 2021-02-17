#!/bin/bash
# This scrip initializes the environment for a new assignment
# Currently the only supported environment is `Latex` with two language `fa` or
# `en.
#
# For ease at using this script add a soft link to this file at ~/.local/bin/
# > ln -s ~/.local/bin/nass ./new_assignment.sh
# after that you can use the script every where with `nass arg1 arg2`

function usage()
{
    scriptname=new_assignment.sh
    echo "Usage: $scriptname <language> <environment_name>"
    echo "* language: either 'fa' or 'en'"
    echo "* environment_name: name of the assignment. A new folder with this name will be made at target directory."
    echo "* [tagrget directory is the current working directory. Changing the target directory is  not yet implemented.]"
}


# Check if arguments are flawed
if [ $# -lt 2 ]
then
    usage
    exit 1
fi
if [ $1 != 'fa' ] && [ $1 != 'en']
then
    usage
    exit 1
fi
if [ $2 == "" ]
then
    usage
    exit
fi


# get directory where this script is placed in
# curfiledir=`dirname $0`
# curfiledir=`realpath $curfiledir`
curfiledir=/home/hawk/Workplace/Git/simple_assignment_solution_tex

# create directory
target_dir=`pwd`
target_path="$target_dir/$2"
target_path=`realpath $target_path`
# mkdir -p $target_path

# Check if target path does not exists
if [ -d "$target_path" ]
then
    echo "A directory with the given name exists."
    echo "Trying to create environment at:"
    echo "        $target_path"
    exit 1
fi

srcdir="$curfiledir/$1"
cp -r "$srcdir" "$target_path/"


# Assignment Boilerplate
Simple latex enviromnet and startup files for getting started with
my university assigments.

The templates are plain and simple as possible.


# Tools

## nass

### Setup nass
You may use `new_assignment.sh` to quickly setup a new environment.
The `new_assignment.sh` can be installed using following command.

```
cp -s `pwd`/new_assignment.sh ~/.local/bin/nass
```

**Issue:** currently `curfiledir=` should be updated inside the `new_assignment.sh`


### Using nass
After setting up `nass`, you can create an environment based on a template
as shown in the example.

For example, `nass fa solution` will generate a new environment in the
current working directory based on `fa` template in this repo.

```
Usage: new_assignment.sh <language> <environment_name>
* language: either 'fa' or 'en'
* environment_name: name of the assignment. A new folder with this name will be made at target directory.
* [tagrget directory is the current working directory. Changing the target directory is  not yet implemented.]
```


# TODOs:

* Implement support for placeholders in templates
* Extend the template structure and support more templates


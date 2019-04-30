# Progli!
User installed program/alias manager. Store installed programs, aliases, or common commands along with description, most useful command, and any additional notes, for reference at a later time.

## Getting Started
Clone this repository then cd into the created directory

### Installation
Run the installation script as root (root needs permissions to write into /usr/local/bin, among other things)

*Assuming you're in the cloned directory:*
```
$ sudo ./install.sh
```
**NOTE:** If you are updating from an old version, save the *program_list* file (in *~/.progli*) to somewhere outside the .progli folder, then copy it back. When running *install.sh*, to re-install it will delete the entire *.progli* file, then copy everything from cloned directory.

### Errors
For the most part, the installation script will deal with any errors it encounters. There are some times where user interaction is required. Just accept everything.

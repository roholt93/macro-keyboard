# Macro Watcher

## What is it?
I've been looking to some fancy macro keyboards, and could no decide which one to buy.

Therefore I've decided to first create a small script that is able to catch shortcuts you've defined in config.yml and execute the appropriate script which is also defined in config.yml.

Later on I still will be able to create/buy a physical macro keyboard and repurpose this script.

## BIG FAT NOTE
You must run this as root, as it attaches to /dev/input/* which is only accessible by root. I've tried to overcome this, but for now that is okay.
As a side effect, all scripts executed by this application will be run as
root.

## Installation

Only tested on Ubuntu: 

    $ lsb_release -a
    Description:    Ubuntu 18.04.4 LTS
    Release:        18.04
    Codename:       bionic

### Dependencies
- Python 3
- $ pip3 install -r requirements.txt

### Running

    Execute:
    ``` 
    ./run.sh
    ```


# Macro Watcher

## What is it?
I've been looking to some fancy macro keyboards, and could no decide which one to buy.

Therefore I've decided to first create a small script that is able to catch shortcuts you've defined in config.yml and execute the appropriate script which is also defined in config.yml.

Later on I still will be able to create/buy a physical macro keyboard and repurpose this script.

## Installation

Only tested on Ubuntu: 

    $ lsb_release -a
    Distributor ID: Ubuntu
    Description:    Ubuntu 22.04.3 LTS
    Release:        22.04
    Codename:       jammy
### Dependencies

- Python 3

### Running

    Execute:
    ``` 
    sudo ./run-macro-keyboard.sh
    ```


### Installation

    Execute:
    ``` 
    ./install.sh
    ```

    The installation will create a systemd service file that directs to the location of where this repo is.

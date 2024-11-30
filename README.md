# POTA Local Parks Progress

POTA Local Parks Progress is a simple Python script that queries the Parks on the Air API to find your closest parks,
prints them in a list starting from the closest, and includes the status of whether you have activated them yet or not.
The output looks like this:

<p align="center">
  <img src="docs/output.png" alt="Screenshot showing the output" />
</p>

## What?

[Parks on the Air](https://parksontheair.com/) is an Amateur Radio activity where radio operators set up portable
stations in country parks, nature reserves, etc. to enjoy the great outdoors alongside their hobby.

There is a set list of parks world-wide which count for the program, which is regularly updated to include new locations
by a team of volunteers.

"Activating" a park consists of going there, setting up a portable radio station, and making at least 10 contacts with
other radio stations around the world, following the [POTA Rules](https://docs.pota.app/docs/rules.html).

This software helps POTA activators keep track of their progress through their local parks, find the closest park they
haven't activated yet, etc.

## Usage

There are multiple ways to install Python scripts, but it will work fine wherever you use Python and however you like to
manage it. See the pipx and virtual environment examples below for two examples.

### pipx

`pipx` is a tool to help you install and run end-user applications written in Python. It creates an isolated environment
for each application and its associated packages and makes the apps available in your shell.

A complete example for Debian & derivatives such as Ubuntu is shown below:

```bash
sudo apt install python3 python3-pip python3-venv pipx
git clone https://github.com/ianrenton/pota-local-progress.git
cd pota-local-progress
pipx install .
pota-local-progress <num_parks> <callsign> [ <grid> | <lat> <lon> ]
```

If `pipx install` warns you about your path and running `pipx ensurepath`, do that before running the application.

### Virtual Environment

If you don't want to use `pipx`, using `venv` and `pip` is a well accepted alternative, and should be used in preference
to installing packages system-wide.

A complete example for Debian & derivatives such as Ubuntu is shown below:

```bash
sudo apt install python3 python3-pip python3-venv
git clone https://github.com/ianrenton/pota-local-progress.git
cd pota-local-progress
python3 -m venv .venv
source .venv/bin/activate
pip install .
pota-local-progress <num_parks> <callsign> [ <grid> | <lat> <lon> ]
deactivate
```

### General Execution

To run the script:

```bash
pota-local-progress <num_parks> <callsign> <grid>
```

or:

```bash
pota-local-progress <num_parks> <callsign> <lat> <lon>
```

You will need to set the three or four command-line arguments appropriately for your query, as follows:

* `num_parks` tells the script to consider this number of parks closest to you.
* `callsign` is your amateur radio callsign, with which the script will look up your stats using the POTA API.
* `grid` is your Maidenhead Grid location
* Alternatively, you can supply a more accurate `lat` and `lon` in decimal degrees.

So I might for example run:

```bash
pota-local-progress 10 M0TRT IO90br
```

or:

```bash
pota-local-progress 20 M0TRT 50.71407 -1.87479
```

> [!WARNING]
> Always do your own research to find out if it is possible and legal to activate a park, regardless of whether it appears
> within this software or on the POTA website, and abide by the POTA rules.
>
> This software makes a number of queries to the "public but unofficial" POTA API. It caches the result for one day, to
> avoid overloading the servers with repeated requests. Please do not abuse the API by hammering it with an undue number
> of requests.

![The night garden before anything is named: leaf litter and fern in the lower frame with silvered edges and a red cast from an unseen headlamp, a moonflower open at the path edge visited and left and visited again, and layered dark behind, with no text, no letters, no wordmark, and no logo](intro-banner.png)
# crypto-entropy-analyzer
Title block: the name above is set in Big Shoulders Text SC in fern silver upon a bark brown plate ruled as a specimen label, with a fine line beneath and a small moonflower beside the first heading only; later headings keep the plate and the rule without the bloom.
![A single moonflower with its white trumpet fully open, lit from one side by the dull red of a headlamp, moss underfoot and leaf litter at the stem, and the name lettered beneath by hand in the herbarium manner on a specimen label plate](logo.png)
![A garden path walked only after full dark, with moonflowers first and largest where the path begins and night scented stations opening in sequence, hawkmoths working the upper air, smaller moths arriving and settling nearer the soil, and the wooden tally board at the garden gate carrying the name in pale ink on dark timber](banner.png)
![The night garden in three bands: layered stems swaying by a fraction and recovering in the far band, a moonflower opening slowly to a full trumpet in the middle band while moths arrive in unevenly spaced hovering visits and the bloom begins its slow closing very late, and leaf litter in the near band across which the red cast of an unseen headlamp travels slowly](scene.svg)
![Major separator](sep-heavy.svg)
# crypto-entropy-analyzer
Analyzes the entropy of a given data source to assess its suitability for use as a seed for cryptographic operations. - Focused on Basic cryptographic operations

> Census note: A run must offer exactly one of the file option or the data option; the parser requires that choice.
![Minor separator](sep-light.svg)
## Install
`git clone https://github.com/ShadowGuard-AI/crypto-entropy-analyzer`

> Census note: The program gives no verdict upon suitability for use as a seed; it measures and reports one figure only.
![Minor separator](sep-light.svg)
## Usage
`python3 main.py (-f FILE | -d DATA)`

> Census note: Logging is already configured at import time, so a later attempt to redirect it to a file is liable to have no effect.
![Minor separator](sep-light.svg)
## Parameters
- `-f`, `--file`: Path to the file to analyze. Exactly one of `-f` and `-d` is required.
- `-d`, `--data`: Data to analyze (string).
- `-h`: Show help message and exit
- `-l`, `--log`: Path to the log file. If not specified, logs to the console.

> Census note: The installation line is preserved exactly as printed in its own chapter; any fault in it is flagged on the website, never silently corrected here.
![Minor separator](sep-light.svg)
## License
Licensed under the terms in LICENSE.
![Major separator](sep-heavy.svg)
## Facts from the code, stated in the prose
This record names: Shannon entropy, bits per byte, python3 main.py, -f, --file, -d, --data, -l, --log, four decimal places, mutually exclusive, nought for empty input.
### One Source, One Figure

The program takes one data source, whether that source arrives as the contents of a file read in binary form or as a string supplied directly and encoded before measurement, and it returns the Shannon entropy of that source as a single figure in bits per byte. The figure is logged to four decimal places. Empty input, by an explicit guard in the calculation, yields a figure of nought rather than an error.
### No Verdict Is Given

The README frames the figure as bearing upon suitability for use as a seed for cryptographic operations. The program itself delivers no verdict upon that suitability: it pronounces nothing suitable and nothing unsuitable, since no threshold, no comparison, and no judgement of any kind is built into its code.
### A Choice the Parser Requires

The working form is python3 main.py with exactly one of the file option or the data option, followed where wanted by the log option. That choice is held in a mutually exclusive group that the parser requires, so a run offering neither and a run offering both are each refused before any measurement begins. The file option is -f and --file; the data option is -d and --data; the log option is -l and --log.
### Columns of the Count

The help option, -h and --help, shows a help message and exits. The file is read whole as bytes. The data string is encoded before counting. Where the log option is not supplied, the logs stay upon the console. A caution from the code: logging is already configured at import time in the module, so the later attempt to redirect it towards a file is liable to have no effect. The calculation uses only arithmetic from the standard library, while a requirements file in the repository nevertheless names an external cryptography package, a discrepancy recorded here without resolution.
### When the Run Ends

A successful measurement ends without an explicit code, which is to say at nought. A missing file, a file that cannot be read, a type failure, and any unexpected failure each print an error and end the run at one. A parser refusal ends in the usual parser manner. The program offers no table of byte frequencies, no breakdown by character, and no comparison against a second source.

![Banner](banner.png)

# crypto-entropy-analyzer
Analyzes the entropy of a given data source to assess its suitability for use as a seed for cryptographic operations. - Focused on Basic cryptographic operations

## Install
`git clone https://github.com/ShadowGuard-AI/crypto-entropy-analyzer`

## Usage
`python3 main.py (-f FILE | -d DATA)`

## Parameters
- `-f`, `--file`: Path to the file to analyze. Exactly one of `-f` and `-d` is required.
- `-d`, `--data`: Data to analyze (string).
- `-h`: Show help message and exit
- `-l`, `--log`: Path to the log file. If not specified, logs to the console.

## License
Licensed under the terms in LICENSE.

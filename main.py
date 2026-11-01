import argparse
import logging
import math

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_entropy(data):
    """
    Calculates the Shannon entropy of a byte string.

    Args:
        data: The byte string to analyze.

    Returns:
        The Shannon entropy in bits per byte.
    """
    if not isinstance(data, bytes):
        raise TypeError("Input data must be a byte string.")

    if not data:
        return 0.0  # Avoid log(0) error for empty data

    # This is a per-byte frequency estimate, capped at 8 bits by
    # construction. A short input cannot reach that cap: n distinct bytes
    # give at most log2(n), so a low score on a few bytes says more about
    # the sample size than about the source the bytes came from.
    entropy = 0
    data_length = len(data)
    probability_map = {}

    # Calculate the probability of each byte
    for byte in data:
        if byte not in probability_map:
            probability_map[byte] = 0
        probability_map[byte] += 1

    # Calculate the Shannon entropy
    for count in probability_map.values():
        probability = float(count) / data_length
        entropy -= probability * math.log2(probability)

    return entropy

def read_file_data(file_path):
    """
    Reads the content of a file as a byte string.

    Args:
        file_path: The path to the file.

    Returns:
        The content of the file as a byte string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there is an error reading the file.
    """
    try:
        with open(file_path, 'rb') as f:
            # I read the whole file in one go. That keeps the counting
            # simple, and it means a file bigger than the free memory
            # fails here instead of being scored in pieces.
            data = f.read()
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except IOError as e:
        logging.error(f"Error reading file: {file_path} - {e}")
        raise

def analyze_data_source(data_source, is_file=False):
    """
    Analyzes the entropy of a given data source.

    Args:
        data_source: The data source to analyze. Can be a file path or a byte string.
        is_file: A boolean indicating whether the data source is a file path.

    Returns:
        The Shannon entropy of the data source.

    Raises:
        ValueError: If the data source is invalid.
        FileNotFoundError: If the specified file does not exist.
        IOError: If an error occurs while reading the file.
        TypeError: If the input data is not a byte string when is_file is false.
    """

    try:
        if is_file:
            logging.info(f"Analyzing entropy of file: {data_source}")
            data = read_file_data(data_source)
        else:
            if isinstance(data_source, str):
                # I score the encoded bytes, not the characters. A string of
                # accented letters scores on its two byte UTF-8 forms, which
                # is a different number than the text alone would suggest.
                data = data_source.encode('utf-8') #encoding string input
            elif isinstance(data_source, bytes):
                data = data_source
            else:
                raise TypeError("Data source must be a file path, a string, or a byte string.")


            logging.info("Analyzing entropy of provided data.")

        entropy = calculate_entropy(data)
        logging.info(f"Entropy: {entropy:.4f} bits per byte")
        return entropy

    except FileNotFoundError:
        raise
    except IOError:
        raise
    except TypeError:
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

def setup_argparse():
    """
    Sets up the argument parser for the command line interface.

    Returns:
        An argparse.ArgumentParser object.
    """
    parser = argparse.ArgumentParser(description="Analyzes the entropy of a given data source to assess its suitability for use as a seed for cryptographic operations.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Path to the file to analyze.")
    group.add_argument("-d", "--data", help="Data to analyze (string or bytes).")
    parser.add_argument("-l", "--log", help="Path to the log file. If not specified, logs to the console.")

    return parser

def main():
    """
    The main function of the script.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    # Configure logging to file if specified
    if args.log:
        # basicConfig only takes effect on the first call, and the module
        # level call above already configured console logging, so without
        # force=True the --log file was silently never created.
        logging.basicConfig(filename=args.log, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', force=True)

    try:
        # is-not-None, not truthiness: -d "" is a real request to score the
        # empty input (entropy 0.0), and the truthiness check used to fall
        # through both branches and exit 0 having analyzed nothing.
        if args.file is not None:
            # I throw the returned number away here. The only place the
            # entropy lands is the log line inside analyze_data_source,
            # so a caller who only watches stdout sees no result at all.
            analyze_data_source(args.file, is_file=True)
        elif args.data is not None:
            analyze_data_source(args.data, is_file=False)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)
    except IOError as e:
        print(f"Error: {e}")
        exit(1)
    except TypeError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()

#Usage Examples
# python crypto_entropy_analyzer.py -f random_data.bin
# python crypto_entropy_analyzer.py -d "This is a test string"
# python crypto_entropy_analyzer.py -f random_data.bin -l entropy.log
# python crypto_entropy_analyzer.py -d "short" -l entropy.log
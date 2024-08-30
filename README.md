# File Search Script - Sabueso

This Python script allows users to search for a specified file within a directory tree. It utilizes depth-first search to traverse directories and find the target file.

## Features

- Recursively searches through all directories and subdirectories.
- Allows specifying a target file and the starting directory.
- Prompts the user for input if the target file or location is not specified.

## Prerequisites

- Python 3.x
- Basic knowledge of using command-line interfaces.

## Usage

### Command-Line Interface

You can run the script directly from the command line. Here’s the syntax:

```bash
python file_search.py --target <filename> --loc <directory>
```

- `--target`: (required) The name of the file you are searching for.
- `--loc`: (optional) The directory in which to start the search. If not provided, the current working directory is used.

### Example

To search for a file named `example.txt` in the `/path/to/directory`:

```bash
python file_search.py --target example.txt --loc /path/to/directory
```

If you want to search for the file in the current directory, you can omit the `--loc` argument:

```bash
python file_search.py --target example.txt
```

If the `--target` argument is not provided, the script will prompt you to enter the filename interactively.

## How It Works

1. The script uses the `os` module to walk through the directory tree.
2. It checks each directory for the presence of the target file.
3. If the file is found, it returns the complete path.
4. If the file is not found after searching all directories, it informs the user.

## Installation

Simply clone this repository or download the script file. Ensure that you have Python 3 installed on your system.

```bash
git clone https://github.com/SergiFuster/sabueso
cd sabueso
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Sergi Fuster

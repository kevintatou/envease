# Envease

Envease is a Python script designed to replace placeholders in files and directories with unique markers based on a configuration file. It can also reverse the replacements, restoring the original placeholders.

## Features

- Replace placeholders in files and directory names with unique markers.
- Reverse the replacements to restore the original placeholders.
- Process entire directories recursively.



## Placeholders

The script replaces the following placeholders:

- `${{ values.namespace }}`
- `${{ values.name }}`

These placeholders will be replaced with unique markers based on the values provided in the [`config.json`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fkagz%2Fgithub%2FEnvEase%2Fconfig.json%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%223d2590c2-2e85-4c21-9020-c5b8aacd8b73%22%5D "/Users/kagz/github/EnvEase/config.json") file.


## Example

1. Create a [`config.json`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fkagz%2Fgithub%2FEnvEase%2Fconfig.json%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%223d2590c2-2e85-4c21-9020-c5b8aacd8b73%22%5D "/Users/kagz/github/EnvEase/config.json") file with your desired values, check below structure:
    ```json
    {
        "namespace": "your_namespace",
        "name": "your_name"
    }
    ```

2. Run the script to replace placeholders:

    ```bash
    python envease.py --directory /path/to/directory
    ```

3. To reverse the replacements, use the `--reverse` flag:

    ```bash
    python envease.py --directory /path/to/directory --reverse
    ```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License. See the LICENSE file for details.
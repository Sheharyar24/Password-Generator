# Password Generator v2.0

A simple, user-friendly desktop application for generating secure passwords with customizable length and quantity options.

## Features

- **Customizable Password Length**: Generate passwords between 4-128 characters
- **Bulk Generation**: Create multiple passwords at once
- **Save to File**: Export generated passwords to a text file
- **Clean Interface**: Simple and intuitive GUI built with tkinter

## Requirements

- Python 3.x
- tkinter (usually included with Python)

## Installation

1. Ensure Python 3.x is installed on your system
2. Download the `password_generator.py` file
3. Run the application:
   ```bash
   python password_generator.py
   ```

## Usage

1. **Set Password Length**: Enter desired password length (4-128 characters)
2. **Set Quantity**: Enter how many passwords you want to generate
3. **Generate**: Click the "Generate" button to create passwords
4. **View Results**: Generated passwords appear in the list below
5. **Save (Optional)**: Click "Save" to export passwords to a text file
6. **Clear**: Use the "Clear" button to reset all fields

## Character Set

Generated passwords include:
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Numbers (0-9)
- Special characters (!@#$%^&*()_+-?)

## Version History

### v2.0
- **Major Interface Upgrade**: Migrated from CLI to GUI using tkinter
- Enhanced layout with improved grid system and responsive design
- Better visual organization with column weights and proper spacing
- Improved error handling and input validation with message boxes
- Updated file save functionality with file dialog
- Code refactoring for better maintainability
- Streamlined user experience with buttons and visual feedback

### v1.0
- Command-line interface (CLI) implementation
- Core password generation functionality
- Customizable password length and quantity
- File saving capabilities
- Password history viewing feature - allowed users to view previously generated passwords
- Basic input validation and error handling

## Technical Details

- **Framework**: tkinter for GUI
- **Password Generation**: Uses Python's `random.choices()` for cryptographically secure randomness
- **Architecture**: Object-oriented design with Password class
- **File I/O**: Built-in file dialog for save operations

## License

This project is open source and available under standard usage terms.

## Support

For issues or feature requests, please ensure you're using Python 3.x with tkinter support.

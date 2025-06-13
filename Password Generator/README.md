# Password Generator

A simple command-line password generator built in Python that creates secure, random passwords with customizable length and saves them to a text file.

## Features

- **Customizable Length**: Generate passwords between 4-128 characters
- **Multiple Passwords**: Generate multiple passwords at once
- **Secure Character Set**: Uses uppercase letters, lowercase letters, numbers, and special characters
- **Save to File**: Export generated passwords to a text file for easy access
- **User-Friendly CLI**: Simple command-line interface with clear menu options

## Character Set

The password generator uses the following character sets:
- **Uppercase Letters**: A-Z
- **Lowercase Letters**: a-z
- **Numbers**: 0-9
- **Special Characters**: `!@#$%^&*()_+-?`

## Example Output

```
=== Password Generator ===
1. Generate Password
2. Exit
==========================

Select option: 1

Enter password length (min 4, max 128): 12
How many passwords would you like to generate: 3

Generated Password:

1. Kx9@mP2$vQwE
2. 7nB#fR5!wEyT
3. Y3$zL9@kM4pL

Do you want to save these passwords to a file? (y/n): y
Passwords saved to file!
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created as a simple utility for generating secure passwords with file export functionality.

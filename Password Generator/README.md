# Password Generator 

A Python command-line password generator that creates secure, random passwords with customizable length, session history tracking, and file export capabilities.

## Features

- **Customizable Length**: Generate passwords between 4-128 characters
- **Bulk Generation**: Create multiple passwords at once
- **Session History**: View all passwords generated during the current session
- **Secure Character Set**: Uses uppercase letters, lowercase letters, numbers, and special characters
- **File Export**: Save generated passwords to a text file

## Character Set

The password generator uses a comprehensive character set for maximum security:
- **Uppercase Letters**: A-Z (26 characters)
- **Lowercase Letters**: a-z (26 characters)  
- **Numbers**: 0-9 (10 characters)
- **Special Characters**: `!@#$%^&*()_+-?` (14 characters)

**Total Character Pool**: 76 unique characters

## Example Session

```
=== Password Generator ===
1. Generate Password
2. View History
3. Exit
==========================

Select option: 1

Enter password length (min 4, max 128): 16
How many passwords would you like to generate: 3

Generated Password:

1. Kx9@mP2$vQwE7nB#
2. fR5!wEyTY3$zL9@k
3. M4pLq8%xN6&jH2^s

Do you want to save these passwords to a file? (y/n): y
Passwords saved to file!

=== Password Generator ===
1. Generate Password
2. View History
3. Exit
==========================

Select option: 2

Previously Generated Passwords:
===============================
1. Kx9@mP2$vQwE7nB#
2. fR5!wEyTY3$zL9@k
3. M4pLq8%xN6&jH2^s
```

## Future Enhancements

Potential improvements for future versions:
- Password strength scoring
- Custom character set options
- Encrypted file export
- Persistent history with encryption
- Password policy compliance checking
- Multiple export formats (CSV, JSON)
- Graphical User Interface

## License

This project is open source and available under the MIT License.

## Author

A simple yet powerful utility for generating secure passwords with session management capabilities.
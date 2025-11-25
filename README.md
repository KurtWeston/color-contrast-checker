# color-contrast-checker

CLI tool to check color contrast ratios for WCAG accessibility compliance

## Features

- Calculate contrast ratio between two colors using WCAG formula
- Check if color pair meets WCAG AA standard (4.5:1 for normal text, 3:1 for large text)
- Check if color pair meets WCAG AAA standard (7:1 for normal text, 4.5:1 for large text)
- Parse hex color codes (#RRGGBB and #RGB formats)
- Parse RGB color values (rgb(r, g, b) format)
- Support CSS named colors (red, blue, white, etc.)
- Display results with clear pass/fail indicators
- Show the calculated contrast ratio with precision
- Suggest lightening/darkening adjustments when colors fail compliance
- Colorized terminal output showing the actual color pair
- Support both foreground/background color input order

## Installation

```bash
# Clone the repository
git clone https://github.com/KurtWeston/color-contrast-checker.git
cd color-contrast-checker

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Built With

- python

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Deck Web Converter

Convert pitch deck PPT (.pptx) or PDF (.pdf) into beautiful, responsive, self-contained HTML presentations.

## Features

- **Single HTML file**: No external dependencies, works offline
- **Keyboard navigation**: Arrow keys (← →) to navigate slides
- **Touch/Swipe support**: Mobile-friendly gesture controls
- **Progress bar**: Visual progress indicator at top
- **Fullscreen mode**: Press 'F' to toggle
- **Print friendly**: CSS optimized for printing
- **Dark theme**: Professional dark mode default

## Usage

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Convert PowerPoint
cd skills/deck-web-converter
python scripts/convert_deck.py --input my_pitch.pptx

# Convert PDF
python scripts/convert_deck.py --input my_deck.pdf

# Custom output path and color
python scripts/convert_deck.py --input pitch.pptx --output index.html --color="#ff6b6b"
```

### Command Line Options

```bash
python scripts/convert_deck.py --help

# Required:
#   --input, -i   Input PPTX or PDF file path

# Optional:
#   --output, -o  Output HTML file path (default: {input_name}_presentation.html)
#   --color, -c   Accent color hex code (default: #1a73e8)
```

### Controls

Once the HTML is generated, open it in any browser:

| Key/Action | Function |
|------------|----------|
| ← (Left Arrow) | Previous slide |
| → (Right Arrow) | Next slide |
| Space | Next slide |
| F | Toggle fullscreen |
| Escape | Exit fullscreen |
| Swipe Left/Right | Navigate (mobile) |
| Click dots | Jump to slide |

### Supported Input

| Format | Notes |
|--------|-------|
| .pptx | Full support - extracts text, images, layouts |
| .pdf | Text and image extraction via PyMuPDF |

### HTML Output Structure

The generated HTML includes:

1. **Progress bar** - Shows progress through the deck
2. **Slide container** - 16:9 slides with smooth transitions
3. **Navigation dots** - Jump to any slide
4. **Arrow buttons** - Previous/Next navigation
5. **Slide counter** - "3 / 10" format indicator
6. **Fullscreen button** - Toggle full presentation mode

### Customization

Change the accent color:

```bash
# Default tech blue
python scripts/convert_deck.py -i deck.pptx

# Custom colors
python scripts/convert_deck.py -i deck.pptx -c "#ff6b6b"  # Red
python scripts/convert_deck.py -i deck.pptx -c "#4ecdc4"  # Teal
python scripts/convert_deck.py -i deck.pptx -c "#f7b731"  # Yellow
```

### Example Workflow

```bash
# 1. Generate pitch deck with pitch-deck-creator
cd ../pitch-deck-creator
python scripts/generate_pitch_deck.py -i startup.json

# 2. Convert to web format
cd ../deck-web-converter
python scripts/convert_deck.py -i ../pitch-deck-creator/MyStartup_BP.pptx

# 3. Share the HTML file
# The _presentation.html file is self-contained and can be:
# - Emailed as attachment
# - Hosted on any static site
# - Opened directly in browser
```

## Dependencies

- Python 3.7+
- python-pptx >= 0.6.21 (for PPTX files)
- pymupdf >= 1.23.0 (for PDF files)

## Browser Support

- Chrome/Edge 80+
- Firefox 75+
- Safari 13+
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

MIT © UniqueClub

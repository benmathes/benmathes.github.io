# Learnings

## Project Structure
- Single-page HTML apps in their own directories (e.g., `/musical-scratchpad/index.html`)
- Main index.html links to projects in the Projects section
- Projects are self-contained with inline CSS/JS, using CDNs for libraries

## Styling Patterns
- Musical scratchpad uses Tailwind CSS via CDN + dark theme
- Main site uses vanilla CSS with Inter font, light theme
- Each project can have its own distinct style

## Key Dependencies Used
- Tailwind CSS (CDN): `https://cdn.tailwindcss.com`
- Inter font: Google Fonts
- LZ-String for URL compression (when needed)

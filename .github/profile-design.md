# Profile artwork

The README uses GitHub-supported HTML, Markdown, and six local SVG images. All
illustrations are original vector artwork; the cards are conceptual illustrations,
not product screenshots. There are no external image generators or runtime services.

Edit the copy and links in `README.md`. Edit the artwork in
`scripts/build_assets.py`, then regenerate it with Python 3:

```sh
python3 scripts/build_assets.py
```

The generator uses only Python's standard library. Commit the generated files in
`assets/` alongside changes to the generator. No GitHub Action, token, package
installation, or network connection is needed to keep the profile working.

The hero's CSS animation is decorative and respects `prefers-reduced-motion`.
Every image has descriptive alt text, and the project details and destinations are
also available as ordinary text links. Artwork uses system font fallbacks.

Biographical and project details came from the public portfolios at
<https://ritvikgoyal.com> and <https://app.ritvikgoyal.com>, plus the linked project
repositories and Dealify's Devpost. WealthSnaps is explicitly marked in development.

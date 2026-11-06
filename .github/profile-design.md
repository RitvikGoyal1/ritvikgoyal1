# Profile artwork

The README uses GitHub-supported HTML, Markdown, and local SVG images. All
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

Project illustrations use `<picture>` to select a compact crop below 600px and a
wide composition on desktop, keeping the native text in a single column.

The introduction is a Shopify / York / Toronto strip. Community work is presented
as four linked SVG cards: CUTC, Hack Canada, Scrapyard Toronto, and Daydream Toronto.
Each has a desktop composition and a simpler mobile composition, selected through
`<picture>`. Original event symbols are illustrations rather than official logos.
The README keeps project credits, award details, development status, and navigation
as native text; longer biographical notes are collapsed to prioritize the artwork.

The hero's CSS animation is decorative and respects `prefers-reduced-motion`.
Every image has descriptive alt text, and the project details and destinations are
also available as ordinary text links. Artwork uses system font fallbacks.

Biographical and project details came from the public portfolios at
<https://ritvikgoyal.com> and <https://app.ritvikgoyal.com>, plus the linked project
repositories and Dealify's Devpost. WealthSnaps is explicitly marked in development.

CUTC's [organizer listing](https://cutc.ca/) identifies Ritvik on the operations
team. Hack Canada's [public team page](https://hackcanada-website-vx2n.vercel.app/)
lists Ritvik among its organizers; the [2026 event page](https://hack-canada-2026.devpost.com/)
documents the 36-hour event at Waterloo's SPUR Innovation Centre. The README uses
the general title "Organizer" rather than an unverified executive title. CUTC and
Hack Canada appear before the project showcase to reflect their importance to Ritvik.

The official [Scrapyard Toronto](https://scrapyard.hackclub.com/toronto) and
[Daydream Toronto](https://daydream.hackclub.com/toronto) pages provide their event
descriptions and destinations. The user identified their organizing work on both.

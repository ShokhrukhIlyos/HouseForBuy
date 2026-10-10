"""Build site/index.html from src/template.html and the knowledge-base JSON files."""
from pathlib import Path

ROOT = Path(__file__).parent
KB = ROOT / "qorasuv-knowledge-base"
DATA = {
    "__DATA3__": KB / "karasu-realtor-channel.json",
    "__DATA2__": KB / "mirzo-ulugbek-additional-listings.json",
    "__DATA__": KB / "listings.json",
}

html = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
for marker, path in DATA.items():
    html = html.replace(marker, path.read_text(encoding="utf-8").strip())

out = ROOT / "site" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8", newline="\n")
print(f"Wrote {out}")

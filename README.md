# PySSED Interactive

A fork of [PySSED](https://github.com/iain-mcdonald/PySSED) (Python Stellar Spectral Energy Distributions) by Iain McDonald et al., extended to include an integrated interactive H-R diagram visualisation pipeline. PySSED is a stellar SED fitting tool developed at the University of Manchester; this fork was produced as part of a research project building on that work.

> **Development history:** This integration was preceded by a set of standalone post-processing visualisation scripts. Those can be found in [PySSED_Bolt_Ons](https://github.com/A-Hollings/PySSED_Bolt_Ons), which documents the earlier stages of this work.

---

## What's New in This Fork

The core PySSED pipeline is unchanged. The following has been added in `src/pyssedinteractive.py`:

- **Integrated interactive H-R diagram** — produced directly as part of the PySSED pipeline run rather than as a post-processing step, built with Plotly
- **HTML export** — outputs a self-contained `.html` file via JavaScript that retains all interactive features, designed to be run from the terminal without needing a persistent server or web application
- **Hover tooltips** — hovering over any datapoint in the exported HTML displays the star's SED image (where available), name, effective temperature, luminosity, and distance
- **Evolutionary stage classification** — stars are automatically categorised into main sequence, white dwarf, and red giant branch populations
- **Dockerfile** — containerised deployment for running the full pipeline without a local Python environment

---

## Running with Docker

Pre-built images are available on [Docker Hub](https://hub.docker.com/r/ahollings/pyssed_images). The interactive image runs the full pipeline from the terminal and outputs a self-contained HTML file:

```bash
# Pull the interactive image
docker pull ahollings/pyssed_images:pyssedinteractive

# View test commands included in the image
docker run -it ahollings/pyssed_images:pyssedinteractive cat /test_commands.txt
```

---

## Running Locally

PySSED should work out of the box with Python 3:

```bash
pip install -r requirements.txt
cd src/
python3 pyssed.py single "Betelgeuse" simple setup.ness
```

The interactive visualisation runs as part of the standard pipeline and outputs a self-contained `Interactive_HR_Diagram.html` file to the output directory, which can be opened directly in any browser — no server or persistent process required.

Full installation instructions and filter configuration details can be found in `doc/Pyssed_manual.pdf`.

---

## Original PySSED Usage

For documentation on the base PySSED pipeline, filter setup, and running the NESS models, refer to the [original PySSED repository](https://github.com/iain-mcdonald/PySSED) and its accompanying manual.

Original reference: McDonald et al., 2024, RASTI, 3, 89.

---

## Related

- [PySSED](https://github.com/iain-mcdonald/PySSED) — original PySSED repository by Iain McDonald et al.
- [PySSED_Bolt_Ons](https://github.com/A-Hollings/PySSED_Bolt_Ons) — standalone predecessor visualisation scripts
- [Docker Hub](https://hub.docker.com/r/ahollings/pyssed_images) — pre-built Docker images for both PySSED and PySSED Interactive

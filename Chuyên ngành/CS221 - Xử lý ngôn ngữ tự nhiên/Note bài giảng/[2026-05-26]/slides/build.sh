#!/usr/bin/env bash
set -euo pipefail

pdflatex -interaction=nonstopmode -halt-on-error main.tex

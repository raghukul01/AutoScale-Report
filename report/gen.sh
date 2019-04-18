#!/bin/bash

docker exec latex /bin/sh -c "cd /report;
                            pdflatex report.tex;
                            rm *.log *.aux"

# evince hw.pdf

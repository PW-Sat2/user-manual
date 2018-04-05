# PW-Sat2 User Manual

## Content
Proposed content of User Manual [available here](https://team.pw-sat.pl/w/system/user-manual/).

## Build
### Build requirements
1. [MikTeX](https://miktex.org/download)
2. Some perl distribution (e.g. https://www.activestate.com/activeperl)
3. Python 2.7

### How to build
1. Go to folder with cloned repository
2. Ensure that required tools are added to path (python, perl and MikTeX)
3. Run `latexmk`

### Watch mode
1. Open PDF with non-locking PDF viewer (e.g. Sumatra PDF, https://www.sumatrapdfreader.org/free-pdf-reader.html)
2. Run `latexmk -pvc` (if your default PDF viewer is opened - close it so output will not be locked)

# PrimeNumbers

Installation instructions for Ubuntu for Python >= 3.7.4:

1. Clone git repo: https://github.com/TeddyTeddy/PrimeNumbers.git
2. cd to the project root in (1)
3. Install and activate a Python virtual environment; under 'venv' folder under the project root
4. This project uses primesieve-python library, which requires g++ installed on your computer
   https://github.com/kimwalisch/primesieve-python
   Follow the instructions, and install g++ & the primesieve-python under the active virtual environment:
        sudo apt install g++ python-dev
        pip install primesieve
5. Using requirements.txt install the other required dependencies
6. Once 5 is done, at the project root, we need to run:
    python prime_number_generator.py

Note that step 6 needs to be done only once.

### How to run the program:

Go to project root in command line, and run:
   python prime_factors_solution.py

It will take about 5-10 secs to load up the necessary data into the variables, after that program is ready for use.
Example:

Loading prime numbers...
Give me a number between 2 and 99999989: 823648463
[11, 199, 587, 641]
Prime factor found: 11
Prime factor found: 199
Prime factor found: 587
Prime factor found: 641
It took 0.39691925048828125000 seconds to find those
Do you want to have another iteration? (Y/N): y
Give me a number between 2 and 99999989: 349563
[3, 109, 1069]
Prime factor found: 3
Prime factor found: 109
Prime factor found: 1069
It took 0.00477242469787597656 seconds to find those
Do you want to have another iteration? (Y/N): n

The program's output can be verified using:
https://www.calculatorsoup.com/calculators/math/prime-factors.php

This program is done in 5 hours 45 mins. Note that the program uses a single thread.
If given extra time, one could extend the program using paralel processing in Python:
https://stackabuse.com/parallel-processing-in-python/





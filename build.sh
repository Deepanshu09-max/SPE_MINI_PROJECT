#!/bin/bash
echo "Running tests..."
python -m unittest test_calculator.py
if [ $? -eq 0 ]; then
    echo "Tests passed. Packaging application..."
    # For example, you could zip the source code
    zip -r scientific_calculator.zip calculator.py test_calculator.py README.md
    echo "Build successful."
else
    echo "Tests failed. Build aborted."
    exit 1
fi

# Student Course Analyzer

This is a Python-based project that reads student and course data from a CSV file (`data.csv`) and generates an HTML report based on user input. The output is saved as `output.html`.

## Features

- Display student-wise course details and total marks
- Display course-wise student marks, average and max marks
- Generates a histogram plot (as `histogram.png`) for course-wise analysis

## Requirements

- Python 3
- matplotlib
- pyhtml
## Usage
To display data for a student:
python app.py -s 101
To display data for a course:
python app.py -c 201


You can install the required libraries using:

```bash
pip install matplotlib pyhtml


# Siemens-Internship-Assignments-2024 - Assignment 1

> [!important]
> This readme contains only instructions of how to run and test the assignment.
> for more about this assignment and my approach to it please check the
> [Report here](./docs/report.md).

## Setup Instructions

### Prerequisites

- Python

### Clone the repo

```sh
git clone https://github.com/amir-kedis/Siemens-Internship-Assignments-2024.git
cd Assigment1
```

### Install Dependencies

1. **Create virtual Env** (optional)

```sh
python -m venv venv
source venv/bin/activate    # on win10 use `venv\Scripts\activate`
```

2. **Install Python dependencies**

```sh
pip install -r requirements.txt
```

### Running the assignment normally

- **To run the assignment with a certain testcase
  adjust the `input.txt` and the output will be in `output.csv`**

```sh
python src/main.py
```

- **To Run against all input files in `tests/inputs`**

```sh
python src/main.py test
```

> [!NOTE]
> if input is valid a CSV file will be made in `tests/outputs` if not it
> will be printed to the standard output that it has invalid input.

### Running the Input Validation And Client-Server Unit tests

```sh
python -m unittest src/tests/*.py
```

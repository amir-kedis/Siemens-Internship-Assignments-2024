# Siemens-Internship-Assignments-2024 - Assignment 2

> [!important]
> This readme contains only instructions of how to run and test the assignment.
> for more about this assignment and my approach to it please check the
> [Report here](./docs/report.md).

## Setup Instructions

### Prerequisites

- CMake 3.14 or higher
- A C++ compiler supporting C++17

### Clone the repo

```sh
git clone https://github.com/amir-kedis/Siemens-Internship-Assignments-2024.git
cd Assigment2
```

### Install Dependencies

- **Generate the build files using `CMake`**

```sh
cmake -S . -B build
```

- **building the project**

```sh
cmake --build build
```

### Running the assignment

- **Running the assignment**:

```sh
./build/PacketTester
```

> [!NOTE]
> a CSV file will be created holding the results.

### Running the unit tests

- **To run the unit tests**:

```sh
./build/PacketTesterTests
```

- or

```sh
cd build
ctest
```

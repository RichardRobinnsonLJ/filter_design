# Filter Design Tool

This repository contains a Python program for designing RL, RC, or LC filters, including Low-Pass Filter (LPF), High-Pass Filter (HPF), Band-Pass Filter (BPF), and Band-Stop Filter (Notch Filter). The tool allows users to either fix the frequency and one component value to find the other, or vice versa.

## Features
- Supports the design of RL, RC, and LC filter types.
- Calculates values based on fixed frequency and one component (e.g., resistance, inductance, or capacitance).
- Designs filters for various types:
  - Low-Pass Filter (LPF)
  - High-Pass Filter (HPF)
  - Band-Pass Filter (BPF)
  - Band-Stop Filter (Notch Filter)

## Usage
### Prerequisites
- Python 3.6 or higher

### Installation
1. Clone this repository:
   ```bash
   git clone  https://github.com/RichardRobinnsonLJ/filter_design.git
   cd filter_design
   ```

### Running the Program
1. Execute the Python script:
   ```bash
   python filter_design.py
   ```
2. Follow the on-screen prompts to specify the filter type, frequency, and known component value.

### Example Workflow
1. Select the filter type (e.g., LPF, HPF, BPF, or Band-Stop Filter).
2. Enter the frequency (in Hz) and the known component value (e.g., resistance or capacitance).
3. The program calculates the remaining component value and displays the results.

## Input/Output
### Input
- Filter Type: Select from LPF, HPF, BPF, or Band-Stop Filter.
- Frequency: Provide the cutoff or center frequency in Hz.
- Known Component Value: Provide one of the following values:
  - Resistance (R) in ohms
  - Capacitance (C) in farads
  - Inductance (L) in henries

### Output
- The calculated component value (R, L, or C).
- Relevant filter design details, such as:
  - Filter equations used
  - Calculated cutoff frequency
  - Other related parameters

## Code Structure
- `passive_filter_design.py`: The main script containing the logic for filter design.
- `README.md`: Documentation for understanding and using the tool.

## Future Enhancements
- Add graphical visualization of filter response (Bode plots).
- Support for advanced filter designs (e.g., Butterworth, Chebyshev).
- GUI for interactive filter design.

## Contributing
Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any questions or suggestions, feel free to contact:
- **Name:** Richard Robinnson L J
- **GitHub:** [RichardRobinnsonLJ](https://github.com/RichardRobinnsonLJ)


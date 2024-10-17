# Minimum Detectable Effect (MDE) Calculator

## Description

This application calculates the Minimum Detectable Effect (MDE) for conversion rate tests based on the statistical significance level and power, number of weeks in the experiment, control conversion rate, sample size per week, and number of variants. If you have any questions about how the calculation was made, visit the **'Calculation'** page. To learn more about the concepts used in this app, visit the **'Concepts and Definitions'** page.

## Features

- **MDE Calculator**: Allows you to calculate the MDE based on specific parameters.
- **Graphical Visualization**: Generates interactive charts to visualize the MDE over the weeks.

## Technologies Used

- **Python**
- **Pandas**
- **Matplotlib**
- **Streamlit**
- **Bokeh**

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/luisdzanetta/minimum-detectable-effect-calculator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-repository
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - For Windows:
        ```bash
        venv\Scripts\activate
        ```
    - For macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1. Run the application:
    ```bash
    streamlit run app.py
    ```
2. Open your browser and navigate to:
    ```
    http://localhost:8501
    ```

## Project Structure

```plaintext
.
├── .streamlit            # Streamlit configurations
├── docs                  # Documents
├── pages                 # Additional pages for Streamlit
├── README.md             # Project documentation
├── app.py                # Main application
├── requirements.txt      # Project dependencies
└── LICENSE               # Project license

```

# Contributing
Fork the project.
Create a branch for your feature (git checkout -b feature/MyFeature).
Commit your changes (git commit -m 'Add MyFeature').
Push to the branch (git push origin feature/MyFeature).
Open a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
**Name:** Luís D`Avoglio Zanetta

**Email:** luis.dzanetta@gmail.com

**GitHub:** luisdzanetta





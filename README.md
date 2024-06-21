### BI Report Generation

This project generates BI (Business Intelligence) reports from CSV data files based on configurations provided in JSON format. It includes functionalities to load data, perform data merging, generate plots, and visualize insights.

## Project Structure

The project consists of the following main components:

# Main Scripts:

main.py: Entry point of the application. It orchestrates the loading of configurations, data files, data merging, and plot generation.
data_loader.py: Module responsible for loading CSV files from a specified directory and merging dataframes based on configuration.
plot_generator.py: Module containing functions to generate various types of plots (bar plots, scatter plots, histograms) based on provided data and plot configurations.
data_plotter.py: Module with plotting functions (plot_bar, plot_scatter, plot_histogram) used by plot_generator.py.
Configuration Files:

config.json: JSON configuration file specifying directory paths, file types, required files, data keys, merge configurations, and plot configurations.
Report Configuration:

report_conf/: Directory containing JSON files that specify individual report configurations. Each JSON file defines how data should be processed, merged, and plotted.
Dataset:

dataset/: Directory where CSV data files (orders.csv, customers.csv, etc.) are stored. These files contain the raw data used for generating reports.
Getting Started

To run the project locally, follow these steps:

Prerequisites
Python 3.x installed on your system.
Required Python packages installed. You can install them using pip:
Copy code
pip install pandas matplotlib seaborn
Installation
Clone the repository to your local machine:

bash
Copy code
git clone <repository-url>
cd BI-Report
Ensure your dataset folder (dataset/) contains the necessary CSV files (orders.csv, customers.csv, etc.) required by your report configurations.

Running the Project
Navigate to the project directory containing main.py.

Run the project:

css
Copy code
python main.py
The script will iterate through each report configuration file (*.json) in report_conf/, load the specified datasets, perform data merging, generate plots, and save them as specified in each report configuration.

Configuration
config.json: Modify this file to specify the directory path, file type, required files, data keys, merge configurations, and plot configurations.

Report Configuration Files (*.json): Each JSON file in report_conf/ defines a specific report configuration, including which datasets to use (df1, df2), how to merge them, and what plots to generate.

Troubleshooting

Missing Files: Ensure all required CSV files are present in the dataset/ directory.

Key Errors: If you encounter KeyError: 'number_of_orders', check the column names in your merged DataFrame (report_data). Adjust the merge operation in merge_dataframes() in data_loader.py if necessary.

Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please submit an issue or a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.


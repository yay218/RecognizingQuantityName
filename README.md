Recognizing Quantity Names for Tabular Data
==========

This is the Python code for recognizing quantity names for tabular data.

Prepare for the Dataset
------------------------
Since the size of datasets used in this experiments is too large, we share our datasets by providing a CSV file, which contains dataset ID, CSV ID, and download URL for each individual dataset in each row. 
In our experiment, we put all the datasets in a folder named 'data', and name the dataset folder as its dataset ID, and CSV file folder as its CSV ID. 

The structure is shown below:

	|___ data
	|___ dataset ID
    		|___ CSV ID
        		|___ data.csv
        |___ dataset ID
    		|___ CSV ID
        		|___ data.csv
        |___ dataset ID
    		|___ CSV ID
        		|___ data.csv
        ......
                
In each of the six .txt files name starts with 'quantity', there is a list of dataset IDs, CSV IDs, and column names that consist of our dataset for training and testing for each quantity name.

Run the Code
------------------------
There are two Python files in this repository, first run:

	python feature_build.py
This process is relatively slow, since it needs to parse all the datasets list in those txt files.
The index along with a message 'ok' will be printed if that dataset is successfully read. If only the index is printed, it means there's an error reading the dataset.

After it is finished, run:

	python cross_validation.py
The results will be printed then.
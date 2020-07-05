Recognizing Quantity Names for Tabular Data
==========

This is the datasets and Python code for **Recognizing Quantity Names for Tabular Data**. The paper can be found [here](http://ceur-ws.org/Vol-2127/paper1-datasearch.pdf). The presentation slides can be found [here](https://drive.google.com/file/d/1tHRPQPCGPon7IhUeJw6lOVkSQ_vRAfyp/view?usp=sharing).


Prepare for the Dataset
------------------------
Since the size of datasets used in this experiments is too large, we share our datasets by providing a CSV file called id_url.csv, which contains dataset ID, CSV ID, and download URL for each individual dataset in each row. 
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
This process is relatively slow, since it needs to parse all the datasets list in those text files.
The index along with a message 'ok' will be printed if that dataset is successfully read. If only the index is printed, it means there's an error reading the dataset.

After it is finished, six CSV files will be created containing the features of instances. Then run:

	python cross_validation.py
Since we have already provided six CSV files here, this command can also be run individually.

The results will be printed then.
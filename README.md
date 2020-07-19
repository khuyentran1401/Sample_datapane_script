# Sample Datapane Script

This is the example code to show how to create [this script](https://datapane.com/khuyentran1401/scripts/visualization_medium/) with Datapane. This script shows the ranks of the author and publications on Medium with respect to publishing frequency last year. 

Find the instruction to create a script with Datapane [here](https://docs.datapane.com/tutorials/tut-deploying-a-script) and options to set up the parameters [here](https://docs.datapane.com/reference/scripts/parameters)

## Descriptions of files in this repo
* [Visualization.ipynb](https://github.com/khuyentran1401/Sample_datapane_script/blob/master/Visualization.ipynb):
  * Visualize data
  * Save graphs and list to create scripts in script.py
* [script.py](https://github.com/khuyentran1401/Sample_datapane_script/blob/master/visualization.py): 
  * Load the graphs and list to show on the script
  * Load parameters to input the information
  * Create the script with Datapane
* [datapane.yaml](https://github.com/khuyentran1401/Sample_datapane_script/blob/master/datapane.yaml):
  * Config file for parameters and the files to include in the script
* publication_count, publication_rank, author_count: pickle files used for the script

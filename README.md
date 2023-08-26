# What is this?
This project is used to create the https://huggingface.co/datasets/NVMSH/opensubtitle_informal2formal_dataset dataset.
It is used to convert informal persian text into formal persian text.

# How to use?
First, make sure your resources are in the right place. You need to download the OpenSubtitles corpus from https://opus.nlpl.eu/OpenSubtitles.php. 
for more details see the `resources/README.md` file.

Then, you need to install the requirements using `pip install -r requirements.txt` command. 

Use `batch_divider.py` script to read and preprocess the data and create the batches in the `xlxs` directory. 

We used the batches in `xlxs/english` files as input for Google Translate. each file has been translated
from english to persian in order to create the `xlxs/translated` files.

Then, we used the `batch_merger.py` script to join the translated files and create the `OpenSubtitles-Informal2Formal.csv` 
file and finally created the huggingface dataset.

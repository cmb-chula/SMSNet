# SMSNet

## Sequence-Mask-Search framework and SMSNet model for Protein Identification.

The pre-trained model can be downloaded from here:

\[Link\]

## Dependencies
This project uses Python 3.5.2, with the following lib dependencies:
* [Tensorflow 1.4](https://www.tensorflow.org/) (compatible up to 1.11)
* [Keras 2.2.4](https://keras.io/)

A list of all python packages can be found in ```requirement.txt```


## Instructions
### Decode
```
python run.py --model_dir <model_directory> --inference_input_file <input_file_directory/input_file.mgf> --rescore
```
```<model_directory>``` is the directory of the model (can be downloaded from the link above).

```<input_file_directory/input_file.mgf>``` is the path to the input file.

Using --rescore flag will generate another probability file with suffix “_rescore” in the same directory. The output will be in “<input_file_directory>_output/”.

Other options can be found in "run.py".

Model parameters (including possible amino acids) can be found in "nmt/input_config.py".

### Note
* In order to generate the report file, the ```TITLE``` lines in .mgf file must end with "scan=<number>".


### Outputs
* For each input file, three output files will be generated in the output directory: ```<input_file>```, ```<input_file>_prob``` and, ```<input_file>_rescore```. They are the output sequences, probabilities of each amino acid, and probabilities of each amino acid after rescoring, respectively.
* The report summarizing the outputs in .tsv format will be in the same parent directory as the input.

## Example
Decoding “test_decode/test_file.mgf” with a model in "model/m_mod/".
```

python run.py --model_dir model/m_mod/ --inference_input_file test_decode/test_file.mgf --rescore
```
The report will be in test_decode_output.

The model will also produce three files:
```
test_decode_output/test_file (sequence)
test_decode_output/test_file_prob (score)
test_decode_output/test_file_rescore (score after rescoring with post-processing model)
```

## Database search
For database searching, change the file name in ```utils_masking/SMSNet_final_database_search.py```, then run ```python utils_masking/SMSNet_final_database_search.py```
    
    
## Acknowledgement
This code is based on TensorFlow Neural Machine Translation [GNMT](https://github.com/tensorflow/nmt). 

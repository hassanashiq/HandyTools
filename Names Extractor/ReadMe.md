# Extract Names from group of Emails

This Python script extracts the names from a list of emails and names. Given a list like 

## Usage

To use the script, simply run `Names Extractor.py` and provide the list of emails and names in the console. You will be required to give the common pattern that you want to remove as well. In below example our common pattern is Test_Acc. The script will then extract the names and output them to the console.

## Example

Suppose you have a list of emails and names like this:

<Test_Acc Aamir Abbass aamir.abbass@random.com;
Test_Acc Allah Baksh allah.baksh@random.com;
Test_ACC Asrar Munsif asrar.munsif@random.com;
Test_ACC Awais Riaz awais.riaz@random.com;
Test_ACC Faisal Masood faisal.masood@random.com;
Test_ACC Gulbahar Akhtar gulbahar@random.com;
Test_ACC Hassan Mukhtar hassan.mukhtar@random.com;
Test_ACC Huzaifa Ahmed huzaifa.ahmed@random.com;

It will return only the names i.e.
Aamir Abbas Aamir 
Allah Baksh 
Munsif Asrar
and so on.


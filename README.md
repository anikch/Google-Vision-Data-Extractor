# Google-Vision-Data-Extractor
This python code can be used to extract data from Google Vision output file. After you process your file for OCR using Google Vision, 
the generated text extraction can be structured, and attributes can be identified by using this code. FeatureExtractor Class has two methods, 
get_all_text() will create a list of dictionary objects, where in dictionary, 'description' key has identified texts as value and 'bounding_poly' key has bounding box co-ordinates of the identified texts.
get_features() method can be used to build a custom template to get values of different attributes in the extraction and it returns a dictionary object. 
In this method you can add all your required templates.

>> fe= FeatureExtractor(template='TEMPLATE1', path=inp1)
>> 
>> fe.get_features()

{'Mail': 'xxxxxxx@gmail.com',
 'Phone': '91xx83xx64xx',
 'Bank IFSC': 'xxFBO0xx1xx',
 'Customer ID': 'xxxxxx4728',
 'Account No.': 'xxxx20x9xxx'}

get_features() works for only those templates where all text co-ordinates are fixed (digitally generated forms, bank statements, invoices etc.). 
For Scanned images extracted texts can be identified by using custom nearest neighbor method. I'll create a separate solution for that.



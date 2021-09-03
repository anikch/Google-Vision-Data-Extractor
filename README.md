# Google-Vision-Data-Extractor
This python code can be used to extract data from Google Vision output. After you process your file for OCR using Google Vision, 
the generated text extraction can be structured, and attributes can be identified by using this code. FeatureExtractor Class has two methods, 
get_all_text() will create a list of dictionary objects, where in dictionary, 'description' key has identified text as value and 'bounding_poly' key has bounding box co-ordinate of the identified text.
get_features() method can be used to build a custom template to find different attribute values in the extraction and will present it as a dictionary. 
Within this method you can create all your templates using co-ordinates.

{'Mail': 'xxxxxxx@gmail.com',
 'Phone': '91xx83xx64xx',
 'Bank IFSC': 'xxFBO0xx1xx',
 'Customer ID': 'xxxxxx4728',
 'Account No.': 'xxxx20x9xxx'}

get_features() works for on ly those templates where all text co-ordinates are fixed (digitally generated forms, bank statements, invoice etc.). 
For Scanned images extracted texts can be identified by using custom nearest neighbor method. I have a separate solution for that.



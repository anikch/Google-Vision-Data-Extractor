import ast
import re

class FeatureExtractor:
    
    page_ident= re.compile(r'\[([^][]+)\]')
    change_tup= (('y:', ','),('bounding_poly', ', "bounding_poly":'),(r'\n', ''),(r'{', '['),(r'}', '],'),
                         ('vertices', ''), (r'], ], ', ']]}'), (r'description', '{"description"'), (r' ', ''), (r'x:', ''))
       
    def __init__(self, bank, path):
        self.path= path
        self.bank= bank
        with open (self.path, "r") as f:
            self.data= ' '.join([line for line in f.readlines()])
        self.pages= re.findall(FeatureExtractor.page_ident, self.data)
        if self.bank== 'TEMPLATE1':
            self.cust_id= [[1212, 330],[1209, 417],[1198, 417],[1201, 330]]
            self.account= [[1199, 329],[1196, 424],[1185, 424],[1188, 329]]
            self.mail= [[309, 877],[316,595],[340,596],[333, 878]]
            self.phone= [[335, 880],[336, 735],[356, 735],[355, 880]]
            self.ifsc= [[354, 886],[355, 745],[377, 745],[376, 886]]
            self.supported_features= {'Customer ID': self.cust_id, 'Account No.': self.account,'Mail': self.mail,
                                      'Phone': self.phone, 'Bank IFSC': self.ifsc}
        else:
            raise ValueError("Invalid template")

            
    def __text_cleanup(self, page):
        self.var_text= page
        for el in FeatureExtractor.change_tup:
            self.var_text= re.sub(el[0], el[1], self.var_text)
        return ast.literal_eval(self.var_text)
 

    def get_all_text(self):
        '''This method returns a List of all identified text as List of dictionary.
        Usage:
        fe= FeatureExtractor(bank='IDFC', path='extract1.txt')
        fe.get_all_text()
        '''
        self.page_list=[]
        for self.page in self.pages:
            self.desc_list=[]
            self.pg_li= self.page.split(', ')
            self.all_items= list(filter(lambda x: x.startswith('description'), self.pg_li))
            for self.item in self.all_items:
                self.a_dict= self.__text_cleanup(self.item)
                self.desc_list.append(self.a_dict)
            self.page_list.append(self.desc_list)
        return self.page_list
  

    def get_features(self):
        self.data_list= self.get_all_text()
        self.final_dict={}
        for self.item in self.data_list:
            for self.en in self.item:
                for self.n, self.feature in enumerate(list(self.supported_features.values())):
                    if self.en['bounding_poly'] == self.feature:
                        self.final_dict[list(self.supported_features.keys())[self.n]]= self.en['description']            
        return self.final_dict
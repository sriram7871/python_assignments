from datetime import datetime,timedelta
class Library_Mgmt:  
    
    def __init__(self):                          
        self.books=['book1','book2','book3','book4']
        self.name=[]
        
    def check_in(self,*name):                    
        checkin=name
        self.name.append(checkin)
        chk_intime=datetime.now()
        return chk_intime
    
    def per_details(self,name,area,ph_no):
        details={'name':name,'area':area,'ph_no':ph_no}
        return details
    
    def add_book(self,*books):                   
        print('library catlog')
        for book in books:
            self.books.append(book)
            return self.books
            
    def search_booksection(self,num):
        if type(num) is str:
            return 'invalid input'
        
        else:
             match num:
                case 1:
                    return 'economics'
                case 2:
                    return 'civics'
                case 3:
                    return 'psychology' 
            
                
    def borrow_book(self,book_name):              
        if book_name in self.books:
            index=self.books.index(book_name)
            pop=self.books.pop(index)
            return'you can borrow',pop 
        
        else:
            return"its not there"
    
    
    def return_book(self,book_name):        
        if book_name not in self.books:
            self.books.append(book_name)
            return 'return a book,done!'
        else:
            return 'return crt book!!!'
            
    def last_date(self):
         today=datetime.now()
         last_day=today+timedelta(14)
         return last_day  
      
                    
    
obj1=Library_Mgmt()


time=obj1.check_in('sriram','jai')
print('check_in time : ',time)  

details=obj1.per_details(name='sriram',area='salavenpet',ph_no=2384803292)
print('about person : ',details)

updated_list=obj1.add_book('book5')
print('updated_list : ',updated_list)

section=obj1.search_booksection(3)
print('section: ',section)

res1=obj1.borrow_book('book3')
print('borrowed book : ',res1)

res2=obj1.return_book('book3')
print('return book : ',res2)

end_date=obj1.last_date()
print('last day to return : ',end_date)

print('Check_in names',obj1.name)

"""
time=obj1.check_in('sriram','jai')
print('check_in time : ',time)  
OUTPUT: 2021-04-18 20:15:21

details=obj1.per_details(name='sriram',area='salavenpet',ph_no=2384803292)
print('about person : ',details)
OUTPUT: {'name': 'sriram','area':'salavenpet','ph_no':2384803292}

updated_list=obj1.add_book('book5')
print('updated_list : ',updated_list)
OUTPUT: ['book1','book2','book3','book4','book5']

section=obj1.search_booksection(3)
print('section: ',section)
OUTPUT: section: psychology

res1=obj1.borrow_book('book3')
print('borrowed book : ',res1)
OUTPUT: borrowed book: ('you can borrow','book3')

res2=obj1.return_book('book3')
print('return book : ',res2)
OUTPUT: return book:return a book,done!

end_date=obj1.last_date()
print('last day to return : ',end_date)
OUTPUT: last day to return : 2024-04-18

print('Check_in names',obj1.name)
OUTPUT:Check_in names [('sriram','jai')]
"""

return a book : return a book,done!
last day to return : 2024-04-15 
check_in  names ['sriram','jai']
"""

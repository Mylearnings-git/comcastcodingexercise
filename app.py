import string, re
from flask import Flask
from flask import request

app = Flask(__name__)

seen_strings = {}

@app.route('/')
def root():
    return '''
    <pre>
    Welcome to the Stringinator 3000 for all of your string manipulation needs.
    GET / - You're already here!
    POST /stringinate - Get all of the info you've ever wanted about a string. Takes JSON of the following form: {"input":"your-string-goes-here"}
    GET /stats - Get statistics about all strings the server has seen, including the longest and most popular strings.
    </pre>
    '''.strip()

@app.route('/stringinate', methods=['GET','POST'])
def stringinate():
    input = ''
    if request.method == 'POST':
        input = request.json['input']
    else:     
        input = request.args.get('input', '')
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        empty = ' ' 
        for char in input:
             if char in punc:
                 input = input.replace(char, "")
        for char in input:
             if char in empty:
                 input = input.replace(char, "")  
        #input1 = input.replace
        #input1 = re.sub(r'[^\w\s]','',input)   
        #input1 = re.sub('[^A-za-z0-9]', '', input)
        d = {}  
     
     
        for ch in input: 
            d[ch] = d.get(ch,0)+1 
            
            res = max(d, key = d.get)  
            collection = d.values()
            maxvalue = max(collection)   
    
        return {
           "Maximum occurence of a character in the given string": res,
           "No of occurence": maxvalue
        }    
      
    if input in seen_strings:
        seen_strings[input] += 1
    else:
        seen_strings[input] = 1

    return {
        "input": input,
        "length": len(input),
    }

@app.route('/stats')
def string_stats():
    
        v = list(seen_strings.values())
        k = list(seen_strings.keys())
        long_key = max(seen_strings, key=len) 
        
        return {
           "most_popular key in the given string input": k[v.index(max(v))],
           "longest_input_received key in the given input": long_key
           }
       
    #return {
     #   "inputs": seen_strings,
      #}
 
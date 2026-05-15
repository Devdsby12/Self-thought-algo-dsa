#Making React mock code 

def React (props):
    return f"<div> hiii {props["name"]} i know you are {props["age"]} Young <div/>"


string =   '<    React name = "dev"  ok bye age = "99" /  >'
error_string = "<hello this is >"

def ReactDecoder(param):
    try:
        newstring = param.strip(" ")
        stripstring = newstring.split(" ")
        params = [x for x in stripstring if x != ""]
    except:
        raise "syantax error "
    hash  = {}
    if params[0] == "<" and params[-1] == ">" and params[-2] == "/" :
        for index ,value in enumerate(params):
            if value == "=":
                list =[]
                new1 , new2 = [ params[(index -1)].replace('"',""),  params[(index+1)].replace('"',"")]
                hash[new1]=new2
        return hash
 





        
    else:
        raise "syantax error "


propss = ReactDecoder(string)
print(React(propss))

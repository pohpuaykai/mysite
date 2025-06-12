from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    found, tagStr, tagId = False, "", None
    tagId__tagStr = {}
    def makeStr(self, tag, attrs):
        attrStr = ""
        for attr in attrs:
            if attr[0].startswith('inkscape:') or attr[0].startswith('sodipodi:') or attr[0].startswith('transform'):
                continue
            attrStr += f' {attr[0]}="{attr[1]}"'
        tag = f'<{tag} {attrStr}>'
        return tag
        
    
    def handle_starttag(self, tag, attrs):
        if tag == 'g' and 'transform' in dict(attrs) and dict(attrs)['id'].startswith('g'):
            self.found = True
            self.tagId = dict(attrs)['id']
            #print("Encountered a start tag:", tag, dict(attrs))
            #print(self.makeStr(tag, attrs))
            self.tagStr +=self.makeStr(tag, attrs)
        elif self.found:
            self.tagStr +=self.makeStr(tag, attrs)

    def handle_endtag(self, tag):
        if self.found:
            self.tagStr+=f'</{tag}>'
        if tag == 'g':
            self.tagId__tagStr[self.tagId] = self.tagStr
            self.found, self.tagStr = False, ""
        

    #def handle_data(self, data):
    #    if self.found:
    #        print("Encountered some data  :", data)
    

if __name__=='__main__':
    parser = MyHTMLParser()
    with open('D:\\p\\mysite\\foundation\\nDisplay\\svg\\Electrical_symbols_library.svg', 'r') as file:
        parser.feed(file.read())
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(parser.tagId__tagStr)
    import os
    outputfileDIR = 'D:\\p\\mysite\\foundation\\nDisplay\\svg\\TEMP'
    if not os.path.isdir(outputfileDIR):
        os.makedirs(outputfileDIR)
    for tagId, tagStr in parser.tagId__tagStr.items():
        #
        
        #
        filepath = os.path.join(outputfileDIR, f'{tagId}.svg')
        with open(filepath, 'w') as file:
            #file.write(f'<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="1800" height="1500" viewBox="0 0 1800 1500" version="1.1" id="svg8" inkscape:version="0.92.0 r">{tagStr}</svg>')
            file.write(f'<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg"  width="1800" height="1500" viewBox="0 0 1800 1500" version="1.1" >{tagStr}</svg>')
       
   
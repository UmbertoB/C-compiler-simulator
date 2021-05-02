from lexical_analysis import LexicalAnalysis 
from syntax_analysis import Parser 

def main():
    al = LexicalAnalysis()

    alL = LexicalAnalysis()
    parser = Parser(alL)

    print('-------- Lex --------')
    while True:
        try:
            token = al.nextToken()

            if (token == None):
                break
            else:
                print(token)
        except Exception as e:
            print(e)
    
    print('\n-------- Syntax --------')
    try:
        parser.execute()
        print('Successfully Parsed')
    except Exception as e:
        print(e)

    print()
    
if (__name__ == '__main__'):
    main()
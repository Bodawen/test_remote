
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='convert text to right form')
parser.add_argument("--inputflie", "-i", type=str, help="The Path to converted text file", required=True,)
parser.add_argument("--outputflie", "-o", type=str, help="The Path to output text file", required=True,)
parser.add_argument("--dictionary", "-d", type=str, help="The Path to dictionary csv file", required=True,)


args = parser.parse_args()

def conversion(inputfile, outputfile, dic):
    print(1)
    dic = pd.read_csv(dic)
    with open(outputfile,"w", encoding='utf8') as out:
        with open(inputfile, "r", encoding='utf8') as f:
             while True:
                line = f.readline()
                for word in range(len(dic)):
                    line = line.replace(dic["original"][word], (dic["new"][word]))
                print(line)
                out.write(line)
                if not line:
                    break

if __name__ == '__main__':
    conversion(args.inputflie,args.outputflie,args.dictionary)
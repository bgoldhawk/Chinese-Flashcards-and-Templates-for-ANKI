import json
import csv
import urllib.parse
import argparse

def urlencode(str):
    return urllib.parse.quote(str)


def writeToCsvFile(importFileName, exportFileName):
    f = open(importFileName)

    data = json.load(f);

    f.close;

    with open(exportFileName, 'w') as exportFile:
        writer = csv.writer(exportFile)
        for i in  data:
            if i["chinese"] != "" :
                writer.writerow(["chinese", "pinyin", "english", "encodedcard"])
                writer.writerow([i['chinese'] , i['pinyin'] , i['english'] , urlencode(json.dumps(i, ensure_ascii=False))])

parser = argparse.ArgumentParser("Export Json to CSV")

parser.add_argument("ifile", help="input file")
parser.add_argument("ofile", help="output file")

args = parser.parse_args()

writeToCsvFile(args.ifile, args.ofile)













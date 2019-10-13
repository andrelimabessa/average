import sys

from . import translation_delivered_generate, Translation_Delivered, Average_Calc

def help():
    print("--window_size : Define the average window size. Mandatory argument")
    print("--input_file  : Input file path. Mandatory argument")

def process_args(argv):
    result = {}
    
    if "--window_size" in argv and "--input_file" in argv:
        result["window_size"] = argv[argv.index("--window_size") + 1]  
        result["input_file"] = argv[argv.index("--input_file") + 1]
    else:
        help()
    
    return result

def main():
    args = process_args(sys.argv)
    
    if len(args) > 0:
        average_calc = Average_Calc(args["window_size"])
        for item in translation_delivered_generate(args["input_file"]):
            average_calc.add_tranlation_delivered(item)
        average_calc.cal_avg_delivered_time()
    
main()
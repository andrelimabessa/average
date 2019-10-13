from pathlib import Path
from ast import literal_eval
from . import average

def test_case_file_one_input():
    result_expected = []
    result = []
    data_folder = Path("testfile/")
    average_calc = average.AverageCalc(10)

    with open(data_folder/"result01.txt") as result_file:
        for item in result_file:
            result_expected.append(literal_eval(item))

    for item in average.translation_delivered_parser(data_folder/"events01.json"):
        average_calc.add_tranlation_delivered(item)

    for item in average_calc.cal_avg_delivered_time():
        result.append(item)

    assert result_expected == result
    

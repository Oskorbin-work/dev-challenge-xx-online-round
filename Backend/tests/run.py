import os

def run_tests():
    #print(os.popen("pytest Backend/tests/tests_views.py -s").read())
    tests_dir = os.path.dirname(os.path.realpath(__file__))

    data_tests = os.popen(f"pytest {tests_dir}/tests_views.py -s").read()

    text = data_tests.replace('\n', '<br>')
    return text


if __name__=="__main__":
    print(run_tests())
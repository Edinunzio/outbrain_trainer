from json import dumps
from collections import Counter

class Trainer():
    def __init__(self):
        self.q_file = 'data/query_groups.txt'
        self.i_file = 'data/input_groups_2.txt'
        self.final_output = []

    def read_file(self, filename):
        groups = []
        f = open(filename, 'r')
        for line in f:
            line = line.strip()
            line = line.split(',')
            groups.append(line)
        f.close()
        return groups

    def get_query(self):
        queries = self.read_file(self.q_file)
        for q_group in queries:
            yield set(q_group)

    def get_inputs(self):
        inputs = self.read_file(self.i_file)
        for i_group in inputs:
            yield set(i_group)

    def match_query_input(self):
        inputs = self.get_inputs()
        container = []
        for input_set in inputs:
            q_group = self.get_query()
            for query_set in q_group:
                data = self.query_check(query_set, input_set)
                if data != None:
                    for d in data:
                        container.append((d, tuple(query_set)))
        x = tuple(container)

        container = Counter(x)
        m_c = container.most_common()
        results = [{item[0][0]:item[1]}for item in m_c]

        return self.output(results)


    def query_check(self, qlist, ilist):
        result = all([qs in ilist  for qs in qlist])
        if result:
            new_words = ilist - qlist
            result = [word for word in new_words]
            return result



    @staticmethod
    def output(dictionary):
        result = dumps(dictionary, sort_keys=True)
        print result
        return result

tr = Trainer()
tr.match_query_input()
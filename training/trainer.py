from json import dumps
from collections import Counter


class Trainer():
    """
    to run inside python console:
    >>> tr = Trainer()
    >>> print tr.match_query_input('data/query_groups.txt', 'data/input_groups.txt')
    """

    def __init__(self):
        pass

    @staticmethod
    def read_file(filename):
        """
        reads txt files and outputs a list of a set of strings
        :param filename: <string>
        :return: groups as <list>
        """
        groups = []
        f = open(filename, 'r')
        for line in f:
            line = line.strip()
            line = line.split(',')
            groups.append(line)
        f.close()
        return groups

    def get_list(self, filename):
        """
        returns generator of the list read from passed file
        :param filename: <string>
        :return: <generator>
        """
        _lists = self.read_file(filename)
        for _list in _lists:
            yield set(_list)

    def match_query_input(self, qfile, ifile):
        """
        returns formatted output of new words from queries matched against input groups
        :param qfile: query_groups.txt <string>
        :param ifile: input_groups.txt <string>
        :return:
        """
        inputs = self.get_list(ifile)
        container = []
        qs = set()
        for input_set in inputs:
            q_group = self.get_list(qfile)
            for query_set in q_group:
                data = self.query_check(query_set, input_set)
                if data is not None:
                    for d in data:
                        container.append((d, tuple(query_set)))
                        qs.add(tuple(query_set))

        cnt = tuple(container)
        container = Counter(cnt)
        m_c = container.most_common()  # provides count with a minimum of 1
        res = []
        for q in qs:
            q_group_results = {}
            for item in m_c:
                if item[0][1] == q:
                    q_group_results[item[0][0]] = item[1]
            if len(q_group_results) != 0:
                q_group_results = self.output(q_group_results)
                res.append(q_group_results)
        return res

    @staticmethod
    def query_check(qlist, ilist):
        """
        set comparison if all items in query group are in input group
        :param qlist:
        :param ilist:
        :return: new words per query matched per input group <list>
        """
        result = all([qs in ilist for qs in qlist])
        if result:
            new_words = ilist - qlist
            result = [word for word in new_words]
            return result


    @staticmethod
    def output(dictionary):
        """
        json dumps output
        :param dictionary:
        :return: count of new words per matched query <string>
        """
        result = dumps(dictionary, sort_keys=True)
        return result

# uncomment below to run script
tr = Trainer()
print tr.match_query_input('data/query_groups.txt', 'data/input_groups.txt')
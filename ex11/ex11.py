############################################################
# FILE : ex11.py
# WRITER : Yair Shtern
# EXERCISE : intro2cs1 ex11 2020
# DESCRIPTION: Diagnoses Trees
############################################################

import itertools


class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


def _sub_trees_are_equal(root1, root2):
    if root1.negative_child is None:
        return root1.data, root2.data
    try:
        if root1.negative_child.data != root2.negative_child.data or \
                root1.positive_child.data != root2.positive_child.data:
            return False
        else:
            x, y = _sub_trees_are_equal(root1.negative_child, root2.negative_child)
            z, w = _sub_trees_are_equal(root1.positive_child, root2.positive_child)
            if x == y and z == w:
                return True
    except:
        return False


class Diagnoser:
    def __init__(self, root: Node):
        self.root = root

    def diagnose(self, symptoms):
        """
        This function diagnose the illness a cording to the symptoms
        :param symptoms: list of symptoms
        :return: the diagnosed illness
        """
        current_root = self.root
        while current_root.negative_child is not None:
            if current_root.data in symptoms:
                current_root = current_root.positive_child
                continue
            current_root = current_root.negative_child
        return current_root.data

    def calculate_success_rate(self, records):
        """
        Thos function calculates the success rate of the tree
        :param records: list pf Records object
        :return: if not equal to zero - the success rate
        """
        right_result = 0
        for record in records:
            if self.diagnose(record.symptoms) == record.illness:
                right_result += 1
        try:
            return right_result / len(records)
        except ZeroDivisionError:
            raise ValueError("Error: records is empty")

    def all_illnesses(self):
        """
        :return: list of all the illnesses of the tree
        """
        lst = self._all_illnesses_helper(self.root, [])
        illnesses_list = []
        for illness in lst:
            if illness not in illnesses_list:
                illnesses_list.append(illness)
        return illnesses_list

    def _all_illnesses_helper(self, current_root, illnesses_list):
        """
        help func to find all the illnesses
        :param current_root: the current node we are in
        :param illnesses_list: list of all the illnesses
        :return: sorted list of all the illnesses (with repetitions)
        """
        if current_root.negative_child is None:
            illnesses_list.append(current_root.data)

        if current_root.negative_child is not None:
            self._all_illnesses_helper(current_root.negative_child, illnesses_list)
            self._all_illnesses_helper(current_root.positive_child, illnesses_list)
        return sorted(illnesses_list, key=lambda x: -illnesses_list.count(x))

    def paths_to_illness(self, illness):
        """
        :param illness: illness to find a path for
        :return: list with the path on the tree to a given illness
        """
        return self._paths_to_illness_helper(illness, self.root, [], [])

    def _paths_to_illness_helper(self, illness, current_root, current_path, paths):
        """
        :param illness: illness to find a path for
        :param current_root: the current node we are in
        :param current_path: the current path we have
        :param paths: all paths we gat
        :return:
        """
        if current_root.data == illness:
            paths.append(current_path)

        if current_root.negative_child is not None:
            self._paths_to_illness_helper(illness, current_root.positive_child, current_path + [True], paths)
            self._paths_to_illness_helper(illness, current_root.negative_child, current_path + [False], paths)
        return paths

    def minimize(self, remove_empty=False):
        """
        This function minimize the tree and if remove_empty ==True its
         minimize also all the sub trees with a path to None
        :param remove_empty: True or False
        :return: None
        """
        self._minimize_false(self.root)

        if remove_empty is True:
            if not self.all_illnesses():
                self.root = Node(None)
            else:
                self._minimize_true(self.root)
            self._minimize_false(self.root)

    def _minimize_false(self, current_root):
        """

        :param current_root:
        :return:
        """
        if current_root.positive_child is None:
            return
        self._minimize_false(current_root.positive_child)
        self._minimize_false(current_root.negative_child)
        if current_root.negative_child.data == current_root.positive_child.data and \
                _sub_trees_are_equal(current_root.positive_child, current_root.negative_child):
            self._delete_current_root(current_root)

    def _delete_current_root(self, current_root):
        """
        removes a Node from the tree
        :param current_root: the Node to remove
        :return: None
        """
        current_root.data = current_root.positive_child.data
        current_root.positive_child = current_root.positive_child.positive_child
        current_root.negative_child = current_root.negative_child.negative_child

    def _minimize_true(self, current_root):
        """

        :param current_root:
        :return:
        """
        if current_root.negative_child is None:
            return
        self._minimize_true(current_root.positive_child)
        self._minimize_true(current_root.negative_child)
        if current_root.negative_child.data is None:
            current_root.data = current_root.positive_child.data
            if current_root.positive_child.positive_child is not None:
                x = current_root.positive_child.positive_child
                y = current_root.positive_child.negative_child
                current_root.positive_child = x
                current_root.negative_child = y

            else:
                current_root.positive_child = None
                current_root.negative_child = None
        elif current_root.positive_child.data is None:
            current_root.data = current_root.negative_child.data
            if current_root.negative_child.negative_child is not None:
                x = current_root.negative_child.negative_child
                y = current_root.negative_child.positive_child
                current_root.negative_child = x
                current_root.positive_child = y
            else:
                current_root.negative_child = None
                current_root.positive_child = None


def _build_tree_helper(current_root, symptoms, records, ind):
    """

    :param current_root:
    :param symptoms:
    :param records:
    :param ind:
    :return:
    """
    positive_records = []
    negative_records = []
    for record in records:

        if current_root.data in record.symptoms:
            positive_records.append(record)
        else:
            negative_records.append(record)
    if ind == len(symptoms):
        _add_node(current_root, negative_records, positive_records)
        return
    current_root.positive_child = Node(symptoms[ind])
    current_root.negative_child = Node(symptoms[ind])
    ind += 1
    _build_tree_helper(current_root.positive_child, symptoms, positive_records, ind)
    _build_tree_helper(current_root.negative_child, symptoms, negative_records, ind)


def _add_node(current_root, negative_records, positive_records):
    """

    :param current_root:
    :param negative_records:
    :param positive_records:
    :return:
    """
    positive_illnesses = []
    for record in positive_records:
        positive_illnesses.append(record.illness)
    if positive_illnesses:
        positive_illnesses = sorted(positive_illnesses, key=lambda x: -positive_illnesses.count(x))
        current_root.positive_child = Node(positive_illnesses[0])
    else:
        current_root.positive_child = Node(None)
    negative_illnesses = []
    for record in negative_records:
        negative_illnesses.append(record.illness)
    if negative_illnesses:
        negative_illnesses = sorted(negative_illnesses, key=lambda x: -negative_illnesses.count(x))
        current_root.negative_child = Node(negative_illnesses[0])
    else:
        current_root.negative_child = Node(None)


def build_tree(records, symptoms):
    """
    This func build a tree
    :param records: list of records to build the tree from
    :param symptoms: list of symptoms to build the tree from
    :return: None
    """
    if _check_exceptions(records, symptoms):
        if not symptoms:
            lst = []
            for record in records:
                lst.append(record.illness)
            most_appear = sorted(lst, key=lambda x: -lst.count(x))
            return Diagnoser(Node(most_appear[0]))
        my_tree = Diagnoser(Node(symptoms[0]))
        _build_tree_helper(my_tree.root, symptoms, records, 1)
        return my_tree
    else:
        raise TypeError("symptoms should contain only string and record only Record objects")


def _check_exceptions(records, symptoms):
    """
    checks for exceptions
    :param records: list of records that should contain only records
    :param symptoms: list of symptoms that should contain only strings
    :return: True if there is no exceptions otherwise False
    """
    for record in records:
        if type(record) != Record:
            return False
    for symptom in symptoms:
        if type(symptom) != str:
            return False
    return True


def optimal_tree(records, symptoms, depth):
    """
    
    :param records:
    :param symptoms:
    :param depth:
    :return:
    """
    if _check_exceptions(records, symptoms):
        if 0 > depth or depth > len(symptoms):
            raise ValueError("depth has to be 0 <= depth <= len(symptoms)")
        else:
            my_optimal_tree = Diagnoser(Node(None))
            for sub_symptoms in itertools.combinations(symptoms, depth):
                my_tree = build_tree(records, sub_symptoms)
                if my_tree.calculate_success_rate(records) > my_optimal_tree.calculate_success_rate(records):
                    my_optimal_tree = my_tree
            return my_optimal_tree
    else:
        raise TypeError("symptoms should contain only string and record only Record objects")

# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = cat_data_from_dict(json.loads(json_string))


def from_str(x):
    assert isinstance(x, str)
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x):
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Choice:
    def __init__(self, choice, risks, recommendations):
        self.choice = choice
        self.risks = risks
        self.recommendations = recommendations

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        choice = from_str(obj.get("choice"))
        risks = from_list(from_str, obj.get("risks"))
        recommendations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("recommendations"))
        return Choice(choice, risks, recommendations)

    def to_dict(self):
        result = {}
        result["choice"] = from_str(self.choice)
        result["risks"] = from_list(from_str, self.risks)
        result["recommendations"] = from_union([lambda x: from_list(from_str, x), from_none], self.recommendations)
        return result


class Question:
    def __init__(self, question, choices, topic):
        self.question = question
        self.choices = choices
        self.topic = topic

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        question = from_union([from_str, from_none], obj.get("question"))
        choices = from_list(Choice.from_dict, obj.get("choices"))
        topic = from_union([from_str, from_none], obj.get("topic"))
        return Question(question, choices, topic)

    def to_dict(self):
        result = {}
        result["question"] = from_union([from_str, from_none], self.question)
        result["choices"] = from_list(lambda x: to_class(Choice, x), self.choices)
        result["topic"] = from_union([from_str, from_none], self.topic)
        return result


class Pillar:
    def __init__(self, pillar, questions):
        self.pillar = pillar
        self.questions = questions

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        pillar = from_str(obj.get("pillar"))
        questions = from_list(Question.from_dict, obj.get("questions"))
        return Pillar(pillar, questions)

    def to_dict(self):
        result = {}
        result["pillar"] = from_str(self.pillar)
        result["questions"] = from_list(lambda x: to_class(Question, x), self.questions)
        return result


class CatData:
    def __init__(self, pillars):
        self.pillars = pillars

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        pillars = from_list(Pillar.from_dict, obj.get("pillars"))
        return CatData(pillars)

    def to_dict(self):
        result = {}
        result["pillars"] = from_list(lambda x: to_class(Pillar, x), self.pillars)
        return result


def cat_data_from_dict(s):
    return CatData.from_dict(s)


def cat_data_to_dict(x):
    return to_class(CatData, x)

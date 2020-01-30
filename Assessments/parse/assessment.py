# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = assessment_from_dict(json.loads(json_string))


def from_str(x):
    assert isinstance(x, str)
    return x


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


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Choice:
    def __init__(self, id, title, answer_tooltip, output, priority, heading):
        self.id = id
        self.title = title
        self.answer_tooltip = answer_tooltip
        self.output = output
        self.priority = priority
        self.heading = heading

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        answer_tooltip = from_union([from_str, from_none], obj.get("answer_tooltip"))
        output = from_union([from_str, from_none], obj.get("output"))
        priority = from_union([from_str, from_none], obj.get("priority"))
        heading = from_union([from_str, from_none], obj.get("heading"))
        return Choice(id, title, answer_tooltip, output, priority, heading)

    def to_dict(self):
        result = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["answer_tooltip"] = from_union([from_str, from_none], self.answer_tooltip)
        result["output"] = from_union([from_str, from_none], self.output)
        result["priority"] = from_union([from_str, from_none], self.priority)
        result["heading"] = from_union([from_str, from_none], self.heading)
        return result


class Question:
    def __init__(self, id, title, explanation, context, type, choices, display_logic, heading):
        self.id = id
        self.title = title
        self.explanation = explanation
        self.context = context
        self.type = type
        self.choices = choices
        self.display_logic = display_logic
        self.heading = heading

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        explanation = from_union([from_str, from_none], obj.get("explanation"))
        context = from_union([from_str, from_none], obj.get("context"))
        type = from_union([from_str, from_none], obj.get("type"))
        choices = from_union([lambda x: from_list(Choice.from_dict, x), from_none], obj.get("choices"))
        display_logic = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("display_logic"))
        heading = from_union([from_none, from_str], obj.get("heading"))
        return Question(id, title, explanation, context, type, choices, display_logic, heading)

    def to_dict(self):
        result = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["explanation"] = from_union([from_str, from_none], self.explanation)
        result["context"] = from_union([from_str, from_none], self.context)
        result["type"] = from_union([from_str, from_none], self.type)
        result["choices"] = from_union([lambda x: from_list(lambda x: to_class(Choice, x), x), from_none], self.choices)
        result["display_logic"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.display_logic)
        result["heading"] = from_union([from_none, from_str], self.heading)
        return result


class Category:
    def __init__(self, id, name, questions):
        self.id = id
        self.name = name
        self.questions = questions

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        questions = from_union([lambda x: from_list(Question.from_dict, x), from_none], obj.get("questions"))
        return Category(id, name, questions)

    def to_dict(self):
        result = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["questions"] = from_union([lambda x: from_list(lambda x: to_class(Question, x), x), from_none], self.questions)
        return result


class Assessment:
    def __init__(self, id, title, category):
        self.id = id
        self.title = title
        self.category = category

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        category = from_union([lambda x: from_list(Category.from_dict, x), from_none], obj.get("category"))
        return Assessment(id, title, category)

    def to_dict(self):
        result = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["category"] = from_union([lambda x: from_list(lambda x: to_class(Category, x), x), from_none], self.category)
        return result


def assessment_from_dict(s):
    return Assessment.from_dict(s)


def assessment_to_dict(x):
    return to_class(Assessment, x)

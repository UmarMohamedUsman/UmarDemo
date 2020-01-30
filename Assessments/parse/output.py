# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = output_from_dict(json.loads(json_string))


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


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


def from_bool(x):
    assert isinstance(x, bool)
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


class ControlConfig:
    def __init__(self, height="10%"):
        self.height = height

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        height = from_union([from_str, from_none], obj.get("height"))
        return ControlConfig(height)

    def to_dict(self):
        result = {}
        result["height"] = from_union([from_str, from_none], self.height)
        return result


class OutputElement:
    def __init__(self, logic, type="html", content="", control_config=ControlConfig()):
        self.type = type
        self.content = content
        self.logic = logic
        self.control_config = control_config

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        content = from_union([from_str, from_none], obj.get("content"))
        logic = from_union([from_str, from_none], obj.get("logic"))
        control_config = from_union([ControlConfig.from_dict, from_none], obj.get("control_config"))
        return OutputElement(type, content, logic, control_config)

    def to_dict(self):
        result = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["content"] = from_union([from_str, from_none], self.content)
        result["logic"] = from_union([from_str, from_none], self.logic)
        result["control_config"] = from_union([lambda x: to_class(ControlConfig, x), from_none], self.control_config)
        return result


class Output:
    def __init__(self, asssessment_id, output_id, display_summary, output_elements):
        self.asssessment_id = asssessment_id
        self.output_id = output_id
        self.display_summary = display_summary
        self.output_elements = output_elements

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        asssessment_id = from_union([from_str, from_none], obj.get("asssessment_id"))
        output_id = from_union([from_str, from_none], obj.get("output_id"))
        display_summary = from_union([from_bool, from_none], obj.get("display_summary"))
        output_elements = from_union([lambda x: from_list(OutputElement.from_dict, x), from_none], obj.get("output_elements"))
        return Output(asssessment_id, output_id, display_summary, output_elements)

    def to_dict(self):
        result = {}
        result["asssessment_id"] = from_union([from_str, from_none], self.asssessment_id)
        result["output_id"] = from_union([from_str, from_none], self.output_id)
        result["display_summary"] = from_union([from_bool, from_none], self.display_summary)
        result["output_elements"] = from_union([lambda x: from_list(lambda x: to_class(OutputElement, x), x), from_none], self.output_elements)
        return result


def output_from_dict(s):
    return Output.from_dict(s)


def output_to_dict(x):
    return to_class(Output, x)

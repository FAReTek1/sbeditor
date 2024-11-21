
class Mutation(ProjectItem):
    def __init__(self, tag_name: str = "mutation", children: list = None,
                 proc_code: str = None, argument_ids: list[str] = None, warp: bool = None,
                 argument_names: list[str] = None, argument_defaults: list = None,
                 has_next: bool = None, *, _id: str = None):
        """
        Mutation for Control:stop block and procedures
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Mutations
        """
        # It's helpful to store the opcode with it
        if children is None:
            children = []

        super().__init__(_id)
        assert tag_name == "mutation"

        self.tag_name = tag_name
        self.children = children

        self.proc_code = proc_code
        self.argument_ids = argument_ids
        self.warp = warp

        self.argument_names = argument_names
        self.argument_defaults = argument_defaults

        self.has_next = has_next

    @staticmethod
    def from_json(data, _id: str = None):
        def load(key):
            value = data.get(key)
            if isinstance(value, str):
                return json.loads(value)
            return value

        return Mutation(
            data["tagName"],

            data["children"],
            # Seems to always be an empty array.

            data.get("proccode"),
            load("argumentids"),
            load("warp"),
            #  ^^ Same as 'run without screen refresh'

            load("argumentnames"),
            load("argumentdefaults"),

            load("hasnext"), _id=_id
        )

    def parse_proc_code(self):
        token = ''
        tokens = []
        last_char = ''

        for char in self.proc_code:
            if last_char == '%':
                if char in "sb":
                    # If we've hit an %s or %b
                    token = token[:-1]
                    # Clip the % sign off the token

                    if token != '':
                        # Make sure not to append an empty token
                        tokens.append(token)

                    # Add the parameter token
                    tokens.append(f"%{char}")
                    token = ''
                    continue

            token += char
            last_char = char

        if token != '':
            tokens.append(token)

        return tokens

    def obfuscate_proc_code(self):

        proc_code = ''
        for token in self.parse_proc_code():
            if token not in ("%s", "%b"):
                proc_code += obfuscate_str(token)
            else:
                proc_code += ' ' + token + ' '
        self.proc_code = proc_code

    def obfuscate_argument_names(self):
        for i, argument_name in enumerate(self.argument_names):
            self.argument_names[i] = obfuscate_str(argument_name)

    def __repr__(self):
        return f"Mutation<{self.id}>"

    @property
    def json(self):
        ret = {
            "tagName": self.tag_name,
            "children": self.children,
        }

        if self.proc_code is not None:
            ret["proccode"] = self.proc_code
            ret["argumentids"] = json.dumps(self.argument_ids)
            ret["warp"] = json.dumps(self.warp)

            if self.argument_names is not None:
                ret["argumentnames"] = json.dumps(self.argument_names)
                ret["argumentdefaults"] = json.dumps(self.argument_defaults)
        if self.has_next is not None:
            ret["hasnext"] = json.dumps(self.has_next)

        return ret

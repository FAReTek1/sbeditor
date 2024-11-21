from .projectitem import ProjectItem

class Target(ProjectItem):
    def __init__(self, is_stage: bool = False, name: str = '', variables: list[Variable] = None,
                 lists: list[List] = None, broadcasts: list[Broadcast] = None, blocks: list[Block] = None,
                 comments: list[Comment] = None, current_costume: int = 0, costumes: list[Costume] = None,
                 sounds: list[Sound] = None,
                 layer_order: int = 1, volume: int | float = 100, tempo: int | float = 60, video_state: str = "off",
                 video_transparency: int | float = 50, text_to_speech_language: str = "en", visible: bool = True,
                 x: int | float = 0,
                 y: int | float = 0, size: int | float = 100, direction: int | float = 90, draggable: bool = False,
                 rotation_style: str = "all around", project: 'Project' = None):
        """
        Represents a sprite or the stage
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Targets
        """
        if name is None:
            name = ''
        elif name in ("_random_", "_mouse_", "_edge_", "_myself_", "_stage_"):
            raise ValueError(f"Sprite is not allowed to be called '{name}'")

        if variables is None:
            variables = []
        if lists is None:
            lists = []
        if broadcasts is None:
            broadcasts = []
        if blocks is None:
            blocks = []
        if comments is None:
            comments = []
        if costumes is None:
            costumes = [Costume()]
        if sounds is None:
            sounds = [Sound()]

        super().__init__(f"{int(is_stage)}{name}")

        self.is_stage = is_stage
        self.name = name
        self.variables = variables
        self.lists = lists
        self.broadcasts = broadcasts
        self.blocks = blocks
        for block in self.blocks:
            block.target = self

        self.comments = comments
        self.current_costume = current_costume
        self.costumes = costumes
        self.sounds = sounds
        self.layer_order = layer_order
        self.volume = volume
        self.tempo = tempo
        self.video_state = video_state
        self.video_transparency = video_transparency
        self.text_to_speech_language = text_to_speech_language
        self.visible = visible
        self.x, self.y = x, y
        self.size = size
        self.direction = direction
        self.draggable = draggable
        self.rotation_style = rotation_style

        self.project = project

    def set_asset_load_method(self, load_method: str | list[str] = "url"):
        for asset in self.assets():
            asset.load_method = load_method

    @staticmethod
    def from_json(data, _id: str = None):
        is_stage = data["isStage"]
        name = data["name"]

        json_variables = data["variables"]
        variables = []
        for var_id, array in json_variables.items():
            variables.append(Variable.from_json(array, var_id))

        json_lists = data["lists"]
        lists = []
        for list_id, list_array in json_lists.items():
            lists.append(List.from_json(list_array, list_id))

        json_broadcasts = data["broadcasts"]
        broadcasts = []
        for broadcast_id, broadcast_name in json_broadcasts.items():
            broadcasts.append(Broadcast.from_json(broadcast_name, broadcast_id))

        json_blocks = data["blocks"]
        blocks = []
        for block_id, block in json_blocks.items():
            blocks.append(Block.from_json(block, block_id))

        json_comments = data["comments"]
        comments = []
        for comment_id, comment in json_comments.items():
            comments.append(Comment.from_json(comment, comment_id))

        current_costume = data["currentCostume"]

        json_costumes = data["costumes"]
        costumes = []
        for costume in json_costumes:
            costumes.append(Costume.from_json(costume))

        json_sounds = data["sounds"]
        sounds = []
        for sound in json_sounds:
            sounds.append(Sound.from_json(sound))

        layer_order = data.get("layerOrder")
        if layer_order is None:
            layer_order = 1

        volume = data["volume"]

        tempo, video_state, video_transparency, text_to_speech_language = (None,) * 4
        visible, x, y, size, direction, draggable, rotation_style = (None,) * 7

        if is_stage:
            tempo = data["tempo"]
            video_state = data["videoState"]
            video_transparency = data["videoTransparency"]
            text_to_speech_language = data["textToSpeechLanguage"]

        else:
            visible = data["visible"]
            x = data["x"]
            y = data["y"]
            size = data["size"]
            direction = data["direction"]
            draggable = data["draggable"]
            rotation_style = data["rotationStyle"]
        return Target(is_stage, name, variables, lists, broadcasts, blocks, comments, current_costume, costumes, sounds,
                      layer_order, volume, tempo, video_state, video_transparency, text_to_speech_language, visible, x,
                      y, size, direction, draggable, rotation_style)

    def assets(self):
        return self.costumes + self.sounds

    def get_broadcast_by_name(self, name: str):
        for broadcast in self.broadcasts:
            if broadcast.name == name:
                return broadcast

    def get_broadcast_by_id(self, _id: str):
        if _id is None:
            return

        for broadcast in self.broadcasts:
            if broadcast.id == _id:
                return broadcast

    def get_blocks_by_opcode(self, opcode: str):
        if opcode is None:
            return
        blocks = []
        for block in self.blocks:
            if block.opcode == opcode:
                blocks.append(block)
        return blocks

    def get_block_by_id(self, block_id: str):
        if not isinstance(block_id, str):
            raise TypeError(f"block_id '{block_id}' is not <type 'str'>, but {type(block_id)}")

        for block in self.blocks:
            if block.id == block_id:
                return block

    def __repr__(self):
        if self.is_stage:
            return f"Stage<Bg #{self.current_costume}>"
        else:
            return f"Sprite<'{self.name}' @({self.x}, {self.y})>"

    @staticmethod
    def from_sprite3(fp: str):
        with ZipFile(fp, "r") as spr3:
            sprite_json = json.loads(spr3.read("sprite.json"))

        target = Target.from_json(sprite_json)
        target.set_asset_load_method(["zip", fp])
        return target

    def export(self, fp: str, make_zip: bool = True):
        os.makedirs(fp, exist_ok=True)

        for asset in self.assets():
            asset.download(f"{fp}\\{asset.id}")

        with open(f"{fp}\\sprite.json", "w", encoding="utf-8") as sprite_json_file:
            json.dump(self.json, sprite_json_file)

        if not make_zip:
            return

        with ZipFile(f"{fp}.sprite3", "w") as achv:
            for file in os.listdir(fp):
                achv.write(f"{fp}\\{file}", arcname=file)

    @property
    def json(self):
        _json = {
            "isStage": self.is_stage,
            "name": self.name,
            "currentCostume": self.current_costume,
            "volume": self.volume,
            "layerOrder": self.layer_order,
        }

        if self.is_stage:
            _json["tempo"] = self.tempo
            _json["videoTransparency"] = self.video_transparency
            _json["videoState"] = self.video_state
            _json["textToSpeechLanguage"] = self.text_to_speech_language
        else:
            _json["visible"] = self.visible

            _json["x"] = self.x
            _json["y"] = self.y
            _json["size"] = self.size
            _json["direction"] = self.direction

            _json["draggable"] = self.draggable
            _json["rotationStyle"] = self.rotation_style

        variables = {}
        for variable in self.variables:
            var_json = variable.json
            variables[var_json[1]] = var_json[0]
        _json["variables"] = variables

        lists = {}
        for list_ in self.lists:
            list_json = list_.json
            lists[list_json[0]] = list_json[1]
        _json["lists"] = lists

        broadcasts = {}
        for broadcast in self.broadcasts:
            broadcast_json = broadcast.json
            broadcasts[broadcast_json[0]] = broadcast_json[1]
        _json["broadcasts"] = broadcasts

        blocks = {}
        for block in self.blocks:
            block_json = block.json
            blocks[block_json[0]] = block_json[1]
        _json["blocks"] = blocks

        comments = {}
        for comment in self.comments:
            comment_json = comment.json
            comments[comment_json[0]] = comment_json[1]
        _json["comments"] = comments

        costumes = []
        for costume in self.costumes:
            costumes.append(costume.json)
        _json["costumes"] = costumes

        sounds = []
        for sound in self.sounds:
            sounds.append(sound.json)
        _json["sounds"] = sounds

        return _json

    @staticmethod
    def new_stage(tts_lang: str = "English"):
        return Target(is_stage=True, name="Stage", text_to_speech_language=tts_lang, layer_order=0)

    @staticmethod
    def new_sprite(name: str = "Blank"):
        return Target(name=name)

    def broadcast_ids(self):
        ids = []
        for broadcast in self.broadcasts:
            ids.append(broadcast.id)
        return ids

    def variable_ids(self):
        ids = []
        for variable in self.variables:
            ids.append(variable.id)
        return ids

    def list_ids(self):
        ids = []
        for list_ in self.lists:
            ids.append(list_.id)
        return ids

    def block_ids(self):
        ids = []
        for block in self.blocks:
            if hasattr(block, "id"):
                ids.append(block.id)
        return ids

    def comment_ids(self):
        ids = []
        for comment in self.comments:
            ids.append(comment.id)
        return ids

    def all_ids(self):
        return self.variable_ids() + self.list_ids() + self.block_ids() + self.comment_ids() + self.broadcast_ids()

    def project_ids(self):
        ids = []
        for target in self.project.targets:
            ids += target.all_ids()
        return ids

    def new_id(self):
        i = 0
        all_ids = self.project_ids()

        new_id = None
        while new_id in all_ids \
                or new_id is None:
            new_id = b10_to_base(i, ID_BASE, digits=ID_DIGITS)
            i += 1

        return new_id

    def add_block(self, new_block: Block):
        """
        Adds a block. Will not attach it to other scripts
        """
        new_block.target = self

        new_block.id = self.new_id()

        self.blocks.append(new_block)
        new_block.link_inputs()

        return new_block

    def link_chain(self, *_chain: [Block], ret_first: bool = True) -> Block | list[Block]:
        """
        Attaches a chain together so that the parent/next attributes are linked to the relevant blocks.

        Useful for chains that are a substack of a C-Mouth, to input the chain's first item while simultaneously linking
        the chain together without setting variables

        :param ret_first: Whether to return the first block in the chain or the whole chain
        :param _chain: Blockchain (List/tuple of blocks)
        :return: The first item of the blockchain if ret_first, else the chain you gave in
        """
        self.add_block(_chain[0])
        _chain[0].attach_chain(
            _chain[1:]
        )

        for block in full_flat(_chain[0].subtree):
            if hasattr(block, "on_linked"):
                block.on_linked()

        return _chain[0] if ret_first \
            else _chain

    def add_variable(self, name: str, value=0, is_cloud_var: bool = False, _id: str = None):
        if _id is None:
            var_id = self.new_id()
        else:
            var_id = _id
        var = Variable(name, value, is_cloud_var, var_id)
        self.variables.append(var)

        return var

    def get_list_by_name(self, name: str):
        for list_ in self.lists:
            if list_.name == name:
                return list_

    def get_list_by_id(self, _id: str):
        for list_ in self.lists:
            if list_.id == _id:
                return list_

    def get_var_by_id(self, _id: str):
        for var in self.variables:
            if var.id == _id:
                return var

    def add_list(self, name: str, value: list = None):
        possible_list = self.get_list_by_name(name)
        if possible_list is not None:
            return possible_list

        if value is None:
            value = []

        list_id = self.new_id()
        _list = List.from_json([name, value], list_id)
        self.lists.append(_list)

        return _list

    def add_broadcast(self, name):
        broadcast_id = self.new_id()
        broadcast = Broadcast(name, broadcast_id)
        self.broadcasts.append(broadcast)
        return broadcast

    def obfuscate(self, del_comments: bool = True, hide_all_blocks: bool = True):
        for variable in self.variables:
            variable.name = obfuscate_str(variable.name)

        for list_ in self.lists:
            list_.name = obfuscate_str(list_.name)

        for block in self.blocks:
            block.x, block.y = 0, 0

            if block.type == "Normal":
                if hide_all_blocks:
                    # You can only set normal blocks to shadow blocks
                    # Variable/list reporters are not normal, and do not have a shadow attribute.
                    # If you use them as an input, they do get a shadow index, however
                    block.is_shadow = True

                if block.opcode == "procedures_prototype":
                    block.mutation.obfuscate_proc_code()
                    block.mutation.obfuscate_argument_names()

                elif block.opcode == "procedures_call":
                    if block.mutation.proc_code not in (
                            "​​log​​ %s",
                            "​​breakpoint​​",
                            "​​error​​ %s",
                            "​​warn​​ %s"
                    ):
                        block.mutation.obfuscate_proc_code()

                elif block.opcode in ("argument_reporter_string_number",
                                      "argument_reporter_boolean"):
                    for field in block.fields:
                        if field.id == "VALUE":
                            if field.value not in ("is compiled?", "is turbowarp?", "is forkphorus?"):
                                field.value = obfuscate_str(field.value)
                block.comment_id = None
        if del_comments:
            new_comments = []
            for i, comment in enumerate(self.comments):
                if self.is_stage:
                    if (comment.text.startswith(
                            "Configuration for https://turbowarp.org/\n"
                            "You can move, resize, and minimize this comment, but don't edit it by hand. "
                            "This comment can be deleted to remove the stored settings.")
                            and comment.text.endswith(" // _twconfig_")):
                        new_comments.append(comment)

            self.comments = new_comments

    def get_custom_blocks(self):
        blocks = []
        for block in self.blocks:
            if block.mutation is not None:
                if block.mutation.proc_code is not None:
                    blocks.append(block)
        return blocks

    @property
    def all_chains(self):
        chains = []
        for block in self.blocks:
            p_chain = block.parent_chain

            ff = list(map(
                lambda x: x.id,
                full_flat(chains)))

            if p_chain[0].id not in ff:
                chains.append(p_chain[0].subtree)

        return chains


class Sprite(Target):
    pass
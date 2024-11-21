from .projectitem import ProjectItem

class Project(ProjectItem):
    def __init__(self, targets: list[Target] = None, extensions: list[Extension] = None, monitors: list[Monitor] = None,
                 meta: Meta = None, _id: int | str = None):
        """
        Represents a whole project. Has targets, monitors, extensions, and metadata
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Projects
        """
        if targets is None:
            targets = [Target.new_stage()]
        if extensions is None:
            extensions = []
        if monitors is None:
            monitors = []
        if meta is None:
            meta = Meta()

        self.targets = targets
        for target in self.targets:
            target.project = self

        self.extensions = extensions
        self.monitors = monitors
        self.meta = meta
        super().__init__(_id)

    def set_asset_load_method(self, load_method: str | list[str] = "url"):
        for target in self.targets:
            target.set_asset_load_method(load_method)

    @staticmethod
    def from_json(data, _id: str = "json"):
        json_targets = data["targets"]
        json_monitors = data["monitors"]
        json_extensions = data["extensions"]
        json_meta = data["meta"]

        targets = []
        for target in json_targets:
            target_obj = Target.from_json(target)
            targets.append(target_obj)

        extensions = []
        for extension in json_extensions:
            extensions.append(Extension(extension))

        monitors = []
        for monitor in json_monitors:
            monitors.append(Monitor.from_json(monitor))

        meta = Meta.from_json(json_meta)

        return Project(targets, extensions, monitors, meta, _id)

    @staticmethod
    def from_sb3(fp: str):
        with ZipFile(fp) as sb3:
            project = Project.from_json(json.loads(sb3.read("project.json")), fp)

        project.set_asset_load_method(["zip", fp])
        return project

    @staticmethod
    def from_id(project_id: int):
        project_token = requests.get(f"https://api.scratch.mit.edu/projects/{project_id}").json()["project_token"]
        response = requests.get(f"https://projects.scratch.mit.edu/{project_id}?token={project_token}")
        try:
            return Project.from_json(
                response.json(), project_id)

        except json.JSONDecodeError:
            raise exceptions.InvalidProjectError(
                f"Project {project_id} does not seem to contain any JSON. Response text: {response.text}")

    @property
    def json(self):
        _json = {
            "meta": self.meta.json
        }
        extensions = []
        for extension in self.extensions:
            extensions.append(extension.json)
        _json["extensions"] = extensions

        monitors = []
        for monitor in self.monitors:
            monitors.append(monitor.json)
        _json["monitors"] = monitors

        targets = []
        for target in self.targets:
            targets.append(target.json)
        _json["targets"] = targets

        return _json

    def assets(self):
        assets = []
        for target in self.targets:
            assets += target.assets()
        return assets

    def export(self, fp: str, make_zip: bool = True, auto_open: bool = False):
        if os.path.isdir(fp):
            try:
                shutil.rmtree(fp)
            except PermissionError as e:
                warnings.warn(f"Permission error ignored: {e}")

        os.makedirs(fp, exist_ok=True)

        for asset in self.assets():
            asset.download(f"{fp}\\{asset.id}")

        with open(f"{fp}\\project.json", "w", encoding="utf-8") as project_json_file:
            json.dump(self.json, project_json_file)

        if not make_zip:
            return

        with ZipFile(f"{fp}.sb3", "w") as achv:
            for file in os.listdir(fp):
                achv.write(f"{fp}\\{file}", arcname=file)

        if auto_open:
            # os.system(f"cd {os.getcwd()}")
            os.system(f"explorer.exe \"{fp}.sb3\"")

    def get_target(self, name: str) -> Target | None:
        for target in self.targets:
            if target.name == name:
                return target

    def add_target(self, target: Target):
        target.project = self
        self.targets.append(target)
        return target

    @property
    def stage(self):
        for target in self.targets:
            if target.is_stage:
                return target

    def obfuscate(self, del_comments: bool = True, hide_all_blocks: bool = True):
        for target in self.targets:
            target.obfuscate(del_comments, hide_all_blocks)

    def add_monitor(self, monitor: Monitor) -> Monitor:
        self.monitors.append(monitor)
        return monitor

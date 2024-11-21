from .projectitem import ProjectItem
import re

EDIT_META = True
META_SET_PLATFORM = False

DEFAULT_META_VM = "0.1.0"
DEFAULT_META_AGENT = "Python: sbeditor.py by https://scratch.mit.edu/users/faretek1/"


class Meta(ProjectItem):
    def __init__(self, semver: str = "3.0.0", vm: str = DEFAULT_META_VM, agent: str = DEFAULT_META_AGENT,
                 platform: dict = None):
        """
        Represents metadata of the project
        https://en.scratch-wiki.info/wiki/Scratch_File_Format#Metadata
        """

        # Thanks to TurboWarp for this pattern ↓↓↓↓, I just copied it
        if re.match("^([0-9]+\\.[0-9]+\\.[0-9]+)($|-)", vm) is None:
            raise ValueError(
                f"\"{vm}\" does not match pattern \"^([0-9]+\\.[0-9]+\\.[0-9]+)($|-)\" - maybe try \"0.0.0\"?")

        self.semver = semver
        self.vm = vm
        self.agent = agent
        self.platform = platform

        super().__init__(semver)

    def __repr__(self):
        return f"Meta<{self.semver} : {self.vm} : {self.agent}>"

    @property
    def json(self):
        _json = {
            "semver": self.semver,
            "vm": self.vm,
            "agent": self.agent
        }

        if self.platform is not None:
            _json["platform"] = self.platform
        return _json

    @staticmethod
    def from_json(data, _id: str = None):
        semver = data["semver"]
        vm = data.get("vm")
        agent = data.get("agent")
        platform = data.get("platform")

        if EDIT_META or vm is None:
            vm = DEFAULT_META_VM
        if EDIT_META or agent is None:
            agent = DEFAULT_META_AGENT
        if META_SET_PLATFORM and (EDIT_META or platform is None):
            platform = {
                "name": "sbeditor.py",
                "url": "https://github.com/FAReTek1/sbeditor"
            }

        return Meta(semver, vm, agent, platform)
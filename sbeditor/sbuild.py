from .sbeditor import *


class Motion:
    class MoveSteps(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_movesteps", shadow=shadow, pos=pos)

        def set_steps(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("STEPS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class TurnRight(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_turnright", shadow=shadow, pos=pos)

        def set_degrees(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DEGREES", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class TurnLeft(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_turnleft", shadow=shadow, pos=pos)

        def set_degrees(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DEGREES", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class GoTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_goto", shadow=shadow, pos=pos)

        def set_to(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                   input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("TO", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class GoToMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_goto_menu", shadow=shadow, pos=pos)

        def set_to(self, value: str = "_random_", value_id: str = None):
            return self.add_field(Field("TO", value, value_id))

    class GoToXY(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_gotoxy", shadow=shadow, pos=pos)

        def set_x(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("X", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_y(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("Y", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class GlideTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_glideto", shadow=shadow, pos=pos)

        def set_secs(self, value, input_type: str | int = "positive number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("SECS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_to(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                   input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("TO", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class GlideToMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_glideto_menu", shadow=shadow, pos=pos)

        def set_to(self, value: str = "_random_", value_id: str = None):
            return self.add_field(Field("TO", value, value_id))

    class GlideSecsToXY(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_glidesecstoxy", shadow=shadow, pos=pos)

        def set_x(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("X", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_y(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("Y", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_secs(self, value, input_type: str | int = "positive number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("SECS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class PointInDirection(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_pointindirection", shadow=shadow, pos=pos)

        def set_direction(self, value, input_type: str | int = "angle", shadow_status: int = 1, *,
                          input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DIRECTION", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class PointTowards(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_pointtowards", shadow=shadow, pos=pos)

        def set_towards(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("TOWARDS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class PointTowardsMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_pointtowards_menu", shadow=shadow, pos=pos)

        def set_towards(self, value: str = "_mouse_", value_id: str = None):
            return self.add_field(Field("TOWARDS", value, value_id))

    class ChangeXBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_changexby", shadow=shadow, pos=pos)

        def set_dx(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                   input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("DX", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ChangeYBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_changeyby", shadow=shadow, pos=pos)

        def set_dy(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                   input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("DY", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetX(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_setx", shadow=shadow, pos=pos)

        def set_x(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("X", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetY(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_sety", shadow=shadow, pos=pos)

        def set_y(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("Y", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class IfOnEdgeBounce(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_ifonedgebounce", shadow=shadow, pos=pos)

    class SetRotationStyle(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_setrotationstyle", shadow=shadow, pos=pos)

        def set_style(self, value: str = "all around", value_id: str = None):
            return self.add_field(Field("STYLE", value, value_id))

    class XPosition(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_xposition", shadow=shadow, pos=pos)

    class YPosition(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_yposition", shadow=shadow, pos=pos)

    class Direction(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_direction", shadow=shadow, pos=pos)

    class ScrollRight(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_scroll_right", shadow=shadow, pos=pos)

        def set_distance(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DISTANCE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ScrollUp(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_scroll_up", shadow=shadow, pos=pos)

        def set_distance(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DISTANCE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class AlignScene(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_align_scene", shadow=shadow, pos=pos)

        def set_alignment(self, value: str = "bottom-left", value_id: str = None):
            return self.add_field(Field("ALIGNMENT", value, value_id))

    class XScroll(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_xscroll", shadow=shadow, pos=pos)

    class YScroll(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_yscroll", shadow=shadow, pos=pos)


class Looks:
    class SayForSecs(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_sayforsecs", shadow=shadow, pos=pos)

        def set_message(self, value="Hello!", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("MESSAGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

        def set_secs(self, value=2, input_type: str | int = "positive integer", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SECS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

    class Say(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_say", shadow=shadow, pos=pos)

        def set_message(self, value="Hello!", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("MESSAGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

    class ThinkForSecs(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_thinkforsecs", shadow=shadow, pos=pos)

        def set_message(self, value="Hmm...", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("MESSAGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

        def set_secs(self, value=2, input_type: str | int = "positive integer", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SECS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

    class Think(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_think", shadow=shadow, pos=pos)

        def set_message(self, value="Hmm...", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("MESSAGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

    class SwitchCostumeTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_switchcostumeto", shadow=shadow, pos=pos)

        def set_costume(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("COSTUME", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Costume(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_costume", shadow=shadow, pos=pos)

        def set_costume(self, value: str = "costume1", value_id: str = None):
            return self.add_field(Field("COSTUME", value, value_id))

    class NextCostume(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_nextcostume", shadow=shadow, pos=pos)

    class SwitchBackdropTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_switchbackdropto", shadow=shadow, pos=pos)

        def set_backdrop(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("BACKDROP", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Backdrops(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_backdrops", shadow=shadow, pos=pos)

        def set_backdrop(self, value: str = "costume1", value_id: str = None):
            return self.add_field(Field("BACKDROP", value, value_id))

    class SwitchBackdropToAndWait(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_switchbackdroptoandwait", shadow=shadow, pos=pos)

        def set_backdrop(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("BACKDROP", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class NextBackdrop(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_nextbackdrop", shadow=shadow, pos=pos)

    class ChangeSizeBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_changesizeby", shadow=shadow, pos=pos)

        def set_change(self, value="10", input_type: str | int = "number", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("CHANGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetSizeTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_setsizeto", shadow=shadow, pos=pos)

        def set_size(self, value="100", input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SIZE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ChangeEffectBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_changeeffectby", shadow=shadow, pos=pos)

        def set_change(self, value="100", input_type: str | int = "number", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("CHANGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_effect(self, value: str = "COLOR", value_id: str = None):
            return self.add_field(Field("EFFECT", value, value_id))

    class SetEffectTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_seteffectto", shadow=shadow, pos=pos)

        def set_value(self, value="0", input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_effect(self, value: str = "COLOR", value_id: str = None):
            return self.add_field(Field("EFFECT", value, value_id))

    class ClearGraphicEffects(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_cleargraphiceffects", shadow=shadow, pos=pos)

    class Hide(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_hide", shadow=shadow, pos=pos)

    class Show(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_show", shadow=shadow, pos=pos)

    class GoToFrontBack(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_gotofrontback", shadow=shadow, pos=pos)

        def set_front_back(self, value: str = "front", value_id: str = None):
            return self.add_field(Field("FRONT_BACK", value, value_id))

    class GoForwardBackwardLayers(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_goforwardbackwardlayers", shadow=shadow, pos=pos)

        def set_num(self, value="1", input_type: str | int = "positive integer", shadow_status: int = 1, *,
                    input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_fowrward_backward(self, value: str = "forward", value_id: str = None):
            return self.add_field(Field("FORWARD_BACKWARD", value, value_id))

    class CostumeNumberName(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_costumenumbername", shadow=shadow, pos=pos)

        def set_number_name(self, value: str = "string", value_id: str = None):
            return self.add_field(Field("NUMBER_NAME", value, value_id))

    class BackdropNumberName(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_backdropnumbername", shadow=shadow, pos=pos)

        def set_number_name(self, value: str = "number", value_id: str = None):
            return self.add_field(Field("NUMBER_NAME", value, value_id))

    class Size(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_size", shadow=shadow, pos=pos)

    class HideAllSprites(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_hideallsprites", shadow=shadow, pos=pos)

    class SetStretchTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_setstretchto", shadow=shadow, pos=pos)

        def set_stretch(self, value="100", input_type: str | int = "number", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("STRETCH", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ChangeStretchBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_changestretchby", shadow=shadow, pos=pos)

        def set_change(self, value="10", input_type: str | int = "number", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("CHANGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))


class Sounds:
    class Play(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_play", shadow=shadow, pos=pos)

        def set_sound_menu(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                           input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SOUND_MENU", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SoundsMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_sounds_menu", shadow=shadow, pos=pos)

        def set_sound_menu(self, value: str = "pop", value_id: str = None):
            return self.add_field(Field("SOUND_MENU", value, value_id))

    class PlayUntilDone(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_playuntildone", shadow=shadow, pos=pos)

        def set_sound_menu(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                           input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SOUND_MENU", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class StopAllSounds(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_stopallsounds", shadow=shadow, pos=pos)

    class ChangeEffectBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_changeeffectby", shadow=shadow, pos=pos)

        def set_value(self, value="10", input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_effect(self, value: str = "PITCH", value_id: str = None):
            return self.add_field(Field("EFFECT", value, value_id))

    class SetEffectTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_seteffectto", shadow=shadow, pos=pos)

        def set_value(self, value="100", input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_effect(self, value: str = "PITCH", value_id: str = None):
            return self.add_field(Field("EFFECT", value, value_id))

    class ClearEffects(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_cleareffects", shadow=shadow, pos=pos)

    class ChangeVolumeBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_changevolumeby", shadow=shadow, pos=pos)

        def set_volume(self, value="-10", input_type: str | int = "number", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VOLUME", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetVolumeTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_setvolumeto", shadow=shadow, pos=pos)

        def set_volume(self, value="100", input_type: str | int = "number", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VOLUME", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Volume(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_volume", shadow=shadow, pos=pos)


class Events:
    class WhenFlagClicked(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenflagclicked", shadow=shadow, pos=pos)

    class WhenKeyPressed(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenkeypressed", shadow=shadow, pos=pos)

        def set_key_option(self, value: str = "space", value_id: str = None):
            return self.add_field(Field("KEY_OPTION", value, value_id))

    class WhenThisSpriteClicked(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenthisspriteclicked", shadow=shadow, pos=pos)

    class WhenStageClicked(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenstageclicked", shadow=shadow, pos=pos)

    class WhenBackdropSwitchesTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenbackdropswitchesto", shadow=shadow, pos=pos)

        def set_backdrop(self, value: str = "backdrop1", value_id: str = None):
            return self.add_field(Field("BACKDROP", value, value_id))

    class WhenGreaterThan(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whengreaterthan", shadow=shadow, pos=pos)

        def set_value(self, value="10", input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_when_greater_than_menu(self, value: str = "LOUDNESS", value_id: str = None):
            return self.add_field(Field("WHENGREATERTHANMENU", value, value_id))

    class WhenBroadcastReceived(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenbroadcastreceived", shadow=shadow, pos=pos)

        def set_broadcast_option(self, value="message1", value_id: str = "I didn't get an id..."):
            return self.add_field(Field("BROADCAST_OPTION", value, value_id))

    class Broadcast(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_broadcast", shadow=shadow, pos=pos)

        def set_broadcast_input(self, value="message1", input_type: str | int = "broadcast", shadow_status: int = 1, *,
                                input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("BROADCAST_INPUT", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class BroadcastAndWait(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_broadcastandwait", shadow=shadow, pos=pos)

        def set_broadcast_input(self, value="message1", input_type: str | int = "broadcast", shadow_status: int = 1, *,
                                input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("BROADCAST_INPUT", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class WhenTouchingObject(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whentouchingobject", shadow=shadow, pos=pos)

        def set_touching_object_menu(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("TOUCHINGOBJECTMENU", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class TouchingObjectMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_touchingobjectmenu", shadow=shadow, pos=pos)

        def set_touching_object_menu(self, value: str = "_mouse_", value_id: str = None):
            return self.add_field(Field("TOUCHINGOBJECTMENU", value, value_id))


class Control:
    class Wait(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_wait", shadow=shadow, pos=pos)

        def set_duration(self, value="1", input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DURATION", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Forever(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_forever", shadow=shadow, pos=pos, can_next=False)

        def set_substack(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                         input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

    class If(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_if", shadow=shadow, pos=pos)

        def set_substack(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                         input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_condition(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("CONDITION", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

    class IfElse(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_if_else", shadow=shadow, pos=pos)

        def set_substack1(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_substack2(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("SUBSTACK2", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_condition(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("CONDITION", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

    class WaitUntil(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_wait_until", shadow=shadow, pos=pos)

        def set_condition(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                          input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("CONDITION", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class RepeatUntil(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_repeat_until", shadow=shadow, pos=pos)

        def set_substack(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                         input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_condition(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("CONDITION", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

    class While(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_while", shadow=shadow, pos=pos)

        def set_substack(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                         input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_condition(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("CONDITION", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

    class Stop(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_stop", shadow=shadow, pos=pos, mutation=Mutation())

        def set_stop_option(self, value: str = "all", value_id: str = None):
            return self.add_field(Field("STOP_OPTION", value, value_id))

        def set_hasnext(self, has_next: bool = True):
            self.mutation.has_next = has_next
            return self

    class StartAsClone(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_start_as_clone", shadow=shadow, pos=pos)

    class CreateCloneOf(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_create_clone_of", shadow=shadow, pos=pos)

        def set_clone_option(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                             input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("CLONE_OPTION", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class CreateCloneOfMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_create_clone_of_menu", shadow=shadow, pos=pos)

        def set_clone_option(self, value: str = "_myself_", value_id: str = None):
            return self.add_field(Field("CLONE_OPTION", value, value_id))

    class DeleteThisClone(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_delete_this_clone", shadow=shadow, pos=pos, can_next=False)

    class ForEach(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_for_each", shadow=shadow, pos=pos)

        def set_substack(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                         input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_value(self, value="5", input_type: str | int = "positive integer", shadow_status: int = 1, *,
                      input_id: str = None):
            inp = Input("VALUE", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_variable(self, value: str = "i", value_id: str = None):
            return self.add_field(Field("VARIABLE", value, value_id))

    class GetCounter(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_get_counter", shadow=shadow, pos=pos)

    class IncrCounter(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_incr_counter", shadow=shadow, pos=pos)

    class ClearCounter(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_clear_counter", shadow=shadow, pos=pos)

    class AllAtOnce(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_all_at_once", shadow=shadow, pos=pos)

        def set_substack(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                         input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)


class Sensing:
    class TouchingObject(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_touchingobject", shadow=shadow, pos=pos)

        def set_touching_object_menu(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("TOUCHINGOBJECTMENU", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class TouchingObjectMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_touchingobjectmenu", shadow=shadow, pos=pos)

        def set_touching_object_menu(self, value: str = "_mouse_", value_id: str = None):
            return self.add_field(Field("TOUCHINGOBJECTMENU", value, value_id))

    class TouchingColor(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_touchingcolor", shadow=shadow, pos=pos)

        def set_color(self, value="#0000FF", input_type: str | int = "color", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("COLOR", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ColorIsTouchingColor(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_coloristouchingcolor", shadow=shadow, pos=pos)

        def set_color1(self, value="#0000FF", input_type: str | int = "color", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("COLOR", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_color2(self, value="#00FF00", input_type: str | int = "color", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("COLOR2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class DistanceTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_distanceto", shadow=shadow, pos=pos)

        def set_distance_to_menu(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                                 input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DISTANCETOMENU", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class DistanceToMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_distancetomenu", shadow=shadow, pos=pos)

        def set_distance_to_menu(self, value: str = "_mouse_", value_id: str = None):
            return self.add_field(Field("DISTANCETOMENU", value, value_id))

    class Loud(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_loud", shadow=shadow, pos=pos)

    class AskAndWait(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_askandwait", shadow=shadow, pos=pos)

        def set_question(self, value="What's your name?", input_type: str | int = "string", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("QUESTION", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

    class Answer(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_answer", shadow=shadow, pos=pos)

    class KeyPressed(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_keypressed", shadow=shadow, pos=pos)

        def set_key_option(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                           input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("KEY_OPTION", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class KeyOptions(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_keyoptions", shadow=shadow, pos=pos)

        def set_key_option(self, value: str = "space", value_id: str = None):
            return self.add_field(Field("KEY_OPTION", value, value_id))

    class MouseDown(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_mousedown", shadow=shadow, pos=pos)

    class MouseX(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_mousex", shadow=shadow, pos=pos)

    class MouseY(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_mousey", shadow=shadow, pos=pos)

    class SetDragMode(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_setdragmode", shadow=shadow, pos=pos)

        def set_drag_mode(self, value: str = "draggable", value_id: str = None):
            return self.add_field(Field("DRAG_MODE", value, value_id))

    class Loudness(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_loudness", shadow=shadow, pos=pos)

    class Timer(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_timer", shadow=shadow, pos=pos)

    class ResetTimer(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_resettimer", shadow=shadow, pos=pos)

    class Of(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_of", shadow=shadow, pos=pos)

        def set_object(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OBJECT", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_property(self, value: str = "backdrop #", value_id: str = None):
            return self.add_field(Field("PROPERTY", value, value_id))

    class OfObjectMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_of_object_menu", shadow=shadow, pos=pos)

        def set_object(self, value: str = "_stage_", value_id: str = None):
            return self.add_field(Field("OBJECT", value, value_id))

    class Current(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_current", shadow=shadow, pos=pos)

        def set_current_menu(self, value: str = "YEAR", value_id: str = None):
            return self.add_field(Field("CURRENTMENU", value, value_id))

    class DaysSince2000(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_dayssince2000", shadow=shadow, pos=pos)

    class Username(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_username", shadow=shadow, pos=pos)

    class UserID(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_userid", shadow=shadow, pos=pos)


class Operators:
    class Add(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_add", shadow=shadow, pos=pos)

        def set_num1(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_num2(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Subtract(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_subtract", shadow=shadow, pos=pos)

        def set_num1(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_num2(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Multiply(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_multiply", shadow=shadow, pos=pos)

        def set_num1(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_num2(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Divide(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_divide", shadow=shadow, pos=pos)

        def set_num1(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_num2(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Random(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_random", shadow=shadow, pos=pos)

        def set_from(self, value="1", input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("FROM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_to(self, value="10", input_type: str | int = "number", shadow_status: int = 1, *,
                   input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("TO", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class GT(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_gt", shadow=shadow, pos=pos)

        def set_operand1(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OPERAND1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_operand2(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OPERAND2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class LT(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_lt", shadow=shadow, pos=pos)

        def set_operand1(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OPERAND1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_operand2(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OPERAND2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Equals(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_equals", shadow=shadow, pos=pos)

        def set_operand1(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OPERAND1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_operand2(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OPERAND2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class And(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_and", shadow=shadow, pos=pos)

        def set_operand1(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OPERAND1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_operand2(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OPERAND2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Or(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_or", shadow=shadow, pos=pos)

        def set_operand1(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OPERAND1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_operand2(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OPERAND2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Not(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_not", shadow=shadow, pos=pos)

        def set_operand(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("OPERAND", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Join(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_join", shadow=shadow, pos=pos)

        def set_string1(self, value="apple ", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("STRING1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_string2(self, value="banana", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("STRING2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class LetterOf(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_letter_of", shadow=shadow, pos=pos)

        def set_letter(self, value="1", input_type: str | int = "positive integer", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("LETTER", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_string(self, value="apple", input_type: str | int = "string", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("STRING", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Length(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_length", shadow=shadow, pos=pos)

        def set_string(self, value="apple", input_type: str | int = "string", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("STRING", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Contains(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_contains", shadow=shadow, pos=pos)

        def set_string1(self, value="apple", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("STRING1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_string2(self, value="a", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("STRING2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Mod(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_mod", shadow=shadow, pos=pos)

        def set_num1(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM1", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_num2(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM2", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Round(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_round", shadow=shadow, pos=pos)

        def set_num(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                    input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class MathOp(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "operator_mathop", shadow=shadow, pos=pos)

        def set_num(self, value='', input_type: str | int = "number", shadow_status: int = 1, *,
                    input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_operator(self, value: str = "abs", value_id: str = None):
            return self.add_field(Field("OPERATOR", value, value_id))


class Data:
    class Variable(Block):
        def __init__(self, value, input_type: str | int = "variable", shadow_status: int = None, *,
                     pos: tuple[int | float, int | float] = (0, 0)):
            inp = Input(None, value, input_type, shadow_status)
            if inp.type_str == "block":
                arr = inp.to_json()[0]
            else:
                arr = inp.to_json()[1][-1]

            super().__init__(array=arr, pos=pos)
            self.opcode = "data_variable"

    class SetVariableTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_setvariableto", shadow=shadow, pos=pos)

        def set_value(self, value="0", input_type: str | int = "string", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_variable(self, value: str | Variable = "variable", value_id: str = None):
            return self.add_field(Field("VARIABLE", value, value_id))

    class ChangeVariableBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_changevariableby", shadow=shadow, pos=pos)

        def set_value(self, value="1", input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_variable(self, value: str | Variable = "variable", value_id: str = None):
            return self.add_field(Field("VARIABLE", value, value_id))

    class ShowVariable(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_showvariable", shadow=shadow, pos=pos)

        def set_variable(self, value: str | Variable = "variable", value_id: str = None):
            return self.add_field(Field("VARIABLE", value, value_id))

    class HideVariable(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_hidevariable", shadow=shadow, pos=pos)

        def set_variable(self, value: str | Variable = "variable", value_id: str = None):
            return self.add_field(Field("VARIABLE", value, value_id))

    class ListContents(Block):
        def __init__(self, value, input_type: str | int = "list", shadow_status: int = None, *,
                     pos: tuple[int | float, int | float] = (0, 0)):
            inp = Input(None, value, input_type, shadow_status)
            if inp.type_str == "block":
                arr = inp.to_json()[0]
            else:
                arr = inp.to_json()[1][-1]

            super().__init__(array=arr, pos=pos)
            self.opcode = "data_listcontents"

    class AddToList(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_addtolist", shadow=shadow, pos=pos)

        def set_item(self, value="thing", input_type: str | int = "string", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("ITEM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_list(self, value: str | List = "list", value_id: str = None):
            return self.add_field(Field("LIST", value, value_id))

    class DeleteOfList(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_deleteoflist", shadow=shadow, pos=pos)

        def set_index(self, value="random", input_type: str | int = "positive integer", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("INDEX", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_list(self, value: str | List = "list", value_id: str = None):
            return self.add_field(Field("LIST", value, value_id))

    class InsertAtList(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_insertatlist", shadow=shadow, pos=pos)

        def set_item(self, value="thing", input_type: str | int = "string", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("ITEM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_index(self, value="random", input_type: str | int = "positive integer", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("INDEX", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_list(self, value: str | List = "list", value_id: str = None):
            return self.add_field(Field("LIST", value, value_id))

    class DeleteAllOfList(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_deletealloflist", shadow=shadow, pos=pos)

        def set_list(self, value: str | List = "list", value_id: str = None):
            return self.add_field(Field("LIST", value, value_id))

    class ReplaceItemOfList(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_replaceitemoflist", shadow=shadow, pos=pos)

        def set_item(self, value="thing", input_type: str | int = "string", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("ITEM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_index(self, value="random", input_type: str | int = "positive integer", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("INDEX", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_list(self, value: str | List = "list", value_id: str = None):
            return self.add_field(Field("LIST", value, value_id))

    class ItemOfList(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_itemoflist", shadow=shadow, pos=pos)

        def set_index(self, value="random", input_type: str | int = "positive integer", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("INDEX", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_list(self, value: str | List = "list", value_id: str = None):
            return self.add_field(Field("LIST", value, value_id))

    class ItemNumOfList(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_itemnumoflist", shadow=shadow, pos=pos)

        def set_item(self, value="thing", input_type: str | int = "string", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("ITEM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_list(self, value: str | List = "list", value_id: str = None):
            return self.add_field(Field("LIST", value, value_id))

    class LengthOfList(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_lengthoflist", shadow=shadow, pos=pos)

        def set_list(self, value: str | List = "list", value_id: str = None):
            return self.add_field(Field("LIST", value, value_id))

    class ListContainsItem(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_listcontainsitem", shadow=shadow, pos=pos)

        def set_item(self, value="thing", input_type: str | int = "string", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("ITEM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_list(self, value: str | List = "list", value_id: str = None):
            return self.add_field(Field("LIST", value, value_id))

    class ShowList(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_showlist", shadow=shadow, pos=pos)

        def set_list(self, value: str | List = "list", value_id: str = None):
            return self.add_field(Field("LIST", value, value_id))

    class HideList(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_hidelist", shadow=shadow, pos=pos)

        def set_list(self, value: str | List = "list", value_id: str = None):
            return self.add_field(Field("LIST", value, value_id))

    class ListIndexAll(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_listindexall", shadow=shadow, pos=pos)

    class ListIndexRandom(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "data_listindexrandom", shadow=shadow, pos=pos)


class Procedures:
    class Definition(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "procedures_definition", shadow=shadow, pos=pos)

        def set_custom_block(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                             input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("custom_block", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Call(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "procedures_call", shadow=shadow, pos=pos, mutation=Mutation())

        def set_proc_code(self, proc_code: str = ''):
            self.mutation.proc_code = proc_code
            return self

        def set_argument_ids(self, *argument_ids: list[str]):
            self.mutation.argument_ids = argument_ids
            return self

        def set_warp(self, warp: bool = True):
            self.mutation.warp = warp
            return self

        def set_arg(self, arg, value='', input_type: str | int = "string", shadow_status: int = 1, *,
                    input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input(arg, value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Declaration(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "procedures_declaration", shadow=shadow, pos=pos, mutation=Mutation())

        def set_proc_code(self, proc_code: str = ''):
            self.mutation.proc_code = proc_code
            return self

    class Prototype(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "procedures_prototype", shadow=shadow, pos=pos, mutation=Mutation())

        def set_proc_code(self, proc_code: str = ''):
            self.mutation.proc_code = proc_code
            return self

        def set_argument_ids(self, *argument_ids: list[str]):
            self.mutation.argument_ids = argument_ids
            return self

        def set_argument_names(self, *argument_names: list[str]):
            self.mutation.argument_names = argument_names
            return self

        def set_argument_defaults(self, *argument_defaults: list[str]):
            self.mutation.argument_defaults = argument_defaults
            return self

        def set_warp(self, warp: bool = True):
            self.mutation.warp = warp
            return self

        def set_arg(self, arg, value, input_type: str | int = "block", shadow_status: int = 1, *,
                    input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input(arg, value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))


class Arguments:
    class EditorBoolean(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "argument_editor_boolean", shadow=shadow, pos=pos, mutation=Mutation())

    class EditorStringNumber(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "argument_editor_string_number", shadow=shadow, pos=pos, mutation=Mutation())

    class ReporterBoolean(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "argument_reporter_boolean", shadow=shadow, pos=pos, mutation=Mutation())

        def set_value(self, value: str = "boolean", value_id: str = None):
            return self.add_field(Field("VALUE", value, value_id))

    class ReporterStringNumber(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "argument_reporter_string_number", shadow=shadow, pos=pos, mutation=Mutation())

        def set_value(self, value: str = "boolean", value_id: str = None):
            return self.add_field(Field("VALUE", value, value_id))


class Addons:
    class IsTurbowarp(Arguments.ReporterBoolean):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(shadow=shadow, pos=pos)
            self.set_value("is turbowarp?")

    class IsCompiled(Arguments.ReporterBoolean):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(shadow=shadow, pos=pos)
            self.set_value("is compiled?")

    class IsForkphorus(Arguments.ReporterBoolean):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(shadow=shadow, pos=pos)
            self.set_value("is forkphorus?")

    class Breakpoint(Procedures.Call):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(shadow=shadow, pos=pos)
            self.set_proc_code("​​breakpoint​​")

    class Log(Procedures.Call):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(shadow=shadow, pos=pos)
            self.set_proc_code("​​log​​ %s")
            self.set_argument_ids("arg0")

        def set_message(self, value='', input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.set_arg("arg0", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)

    class Warn(Procedures.Call):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(shadow=shadow, pos=pos)
            self.set_proc_code("​​warn​​ %s")
            self.set_argument_ids("arg0")

        def set_message(self, value='', input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.set_arg("arg0", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)

    class Error(Procedures.Call):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(shadow=shadow, pos=pos)
            self.set_proc_code("​​error​​ %s")
            self.set_argument_ids("arg0")

        def set_message(self, value='', input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.set_arg("arg0", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)


class Pen:
    class Clear(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_clear", shadow=shadow, pos=pos)

    class Stamp(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_stamp", shadow=shadow, pos=pos)

    class PenDown(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_penDown", shadow=shadow, pos=pos)

    class PenUp(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_penUp", shadow=shadow, pos=pos)

    class SetPenColorToColor(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_setPenColorToColor", shadow=shadow, pos=pos)

        def set_color(self, value="#FF0000", input_type: str | int = "color", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("COLOR", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ChangePenParamBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_changePenColorParamBy", shadow=shadow, pos=pos)

        def set_param(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("COLOR_PARAM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_value(self, value="10", input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetPenParamTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_setPenColorParamTo", shadow=shadow, pos=pos)

        def set_param(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("COLOR_PARAM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_value(self, value="10", input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ChangePenSizeBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_changePenSizeBy", shadow=shadow, pos=pos)

        def set_size(self, value="1", input_type: str | int = "positive number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SIZE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetPenSizeTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_setPenSizeTo", shadow=shadow, pos=pos)

        def set_size(self, value="1", input_type: str | int = "positive number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SIZE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetPenHueTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_setPenHueToNumber", shadow=shadow, pos=pos)

        def set_hue(self, value="1", input_type: str | int = "positive number", shadow_status: int = 1, *,
                    input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("HUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ChangePenHueBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_changePenHueBy", shadow=shadow, pos=pos)

        def set_hue(self, value="1", input_type: str | int = "positive number", shadow_status: int = 1, *,
                    input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("HUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetPenShadeTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_setPenShadeToNumber", shadow=shadow, pos=pos)

        def set_shade(self, value="1", input_type: str | int = "positive number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SHADE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ChangePenShadeBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_changePenShadeBy", shadow=shadow, pos=pos)

        def set_shade(self, value="1", input_type: str | int = "positive number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SHADE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ColorParamMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "pen_menu_colorParam", shadow=shadow, pos=pos)

        def set_color_param(self, value: str = "color", value_id: str = None):
            return self.add_field(Field("colorParam", value, value_id))


class OtherBlocks:
    class Note(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "note", shadow=shadow, pos=pos)

        def set_note(self, value: str = "60", value_id: str = None):
            return self.add_field(Field("NOTE", value, value_id))

    class Matrix(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "matrix", shadow=shadow, pos=pos)

        def set_note(self, value: str = "0101010101100010101000100", value_id: str = None):
            return self.add_field(Field("MATRIX", value, value_id))

    class RedHatBlock(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            # Note: There is no single opcode for the red hat block as the block is simply the result of an error
            # The opcode here has been set to 'redhatblock' to make it obvious what is going on

            # (It's not called red_hat_block because then TurboWarp thinks that # it's supposed to find an extension
            # called red)

            # Appendix: You **CAN** actually add comments to this block, however it will make the block misbehave in the
            # editor. The the link between the comment and the block will not be visible, but will be visible with the
            # corresponding TurboWarp addon
            super().__init__(None, "redhatblock", shadow=shadow, pos=pos)
